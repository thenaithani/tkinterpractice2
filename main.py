import tkinter

window = tkinter.Tk()
window.minsize(600,600)
window.maxsize(600,600)
window.title("practice")

label = tkinter.Label(text="peanut butter")
label.pack(side="top")

answer = tkinter.Entry()
answer.pack()

def niggatron():
    label.config(text=answer.get())

button = tkinter.Button(text="change", command=niggatron)
button.pack()

def listbox_item(event):
    label.config(text=letterbox.get(letterbox.curselection()))
    print(letterbox.get(letterbox.curselection()))

Attribute = tkinter.IntVar()
letterbox = tkinter.Listbox(height=5)
stuff = ["apple", "orange", "banana", "cherry", "tangerine"]
for i in stuff:
    letterbox.insert(stuff.index(i), i)

letterbox.bind("<<ListboxSelect>>",listbox_item)
letterbox.pack()




window.mainloop()