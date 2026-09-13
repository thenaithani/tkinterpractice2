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







window.mainloop()