import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

r_arrow = '->'; c1=0; r1=2
l_arrow = '<-'; c2=2; r2=2
error = 'Check Input!'

def bin2dec():
    root.title('Bin2Dec Conversion')
    
    '''When entry cleared after first calculation'''
    if bin_entry.get() == '': l3['text']='0'; return
    
    '''Evalutes after Calculate button clicked'''
    val = bin_entry.get()
    for e in val:
        rule = 1
        if e not in '01':
            rule = 2
            break
    if rule == 1:
        length = len(val)
    
        ans = 0
        for i in range(length):
            ans += (int(val[i]))*(2**(length-i-1))
    
        l3['text']=ans
    
    else: l3['text']=error

def dec2bin():
    root.title('Dec2Bin Conversion')

    if bin_entry.get() == '': l3['text']='0'; return
    if bin_entry.get().isnumeric():
        val = int(bin_entry.get())
        ans = str(bin(val))
        l3['text']=ans[2:]
    
    else: l3['text']=error

def change():
    global c1, c2, r1, r2
    
    if b1['text'] == r_arrow:
        b1['text'] = l_arrow
        c1, r1 = 0, 2
        c2, r2 = 2, 2

    else:
        b1['text'] = r_arrow
        c1, r1 = 2, 2
        c2, r2 = 0, 2
    
    check()

def check(*args):
    if b1['text'] == r_arrow: bin2dec()
    else: dec2bin()

def copy(*args):
    if l3['text'] != error:
        root.clipboard_clear()
        ans = l3['text']
        root.clipboard_append(ans)
        
        messagebox.showinfo(message='Answer copied to clipboard')
        root.update()
    else: return

root = tk.Tk()
root.title('Bin2Dec Conversion')
mainframe = ttk.Frame(root, padding=(5, 5, 5, 5))

# Variables
bin_entry = tk.Variable()

# Display
l1 = ttk.Label(mainframe, text='Binary')
b1 = ttk.Button(mainframe, text = '->', command=change)
l2 = ttk.Label(mainframe, text='Decimal')
text_bin = ttk.Entry(mainframe, textvariable = bin_entry)
l3 = ttk.Label(mainframe, text='0')
b2 =ttk.Button(mainframe, text='Convert', command=check)

#gridding
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.W, tk.E))
l1.grid(column=0, row=0)
b1.grid(column=1, row=0)
l2.grid(column=2, row=0)
text_bin.grid(column=c1, row=r1)
l3.grid(column=c2, row=r2)
b2.grid(column=1, row=2, sticky=(tk.N, tk.S, tk.W, tk.E))

#weight
root.columnconfigure(0, weight=1, minsize=150)
root.rowconfigure(0, weight=1, minsize=75)

for i in range(3):
    mainframe.columnconfigure(i, weight=1, pad=3)
    mainframe.rowconfigure(i, weight=1, pad=3)

#key-binding
root.bind('<Return>', check)
l3.bind('<Button-1>', copy)

root.mainloop()