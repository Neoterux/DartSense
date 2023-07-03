import customtkinter
import tkinter
from sintactico import parserSintactico

def button_callback():
    text = textbox.get("0.0", "end")

    console.configure(state='normal')
    console.delete("0.0", "end")
    console.insert("0.0", text)
    console.configure(state='disabled')

app = customtkinter.CTk()

app.after(0, lambda: app.wm_state('zoomed'))
app.title('DartSense')

#Window size
width = app.winfo_screenwidth()
height = app.winfo_screenheight()

center_h = height//2
center_w = width//2

# app.geometry("%dx%d" % (width, height))
app.minsize(center_w, center_h)

button = customtkinter.CTkButton(app, text="Run", command=button_callback)
button.pack(pady=10)

textbox = customtkinter.CTkTextbox(app, width=width, height=height*(2/3), corner_radius=5)
textbox.pack(padx=5, pady=5)

label = customtkinter.CTkLabel(app, text="Console")
label.pack(padx=5, pady=5)

console = customtkinter.CTkTextbox(app, width=width, height=height*(1/3), corner_radius=5)
console.pack(padx=5, pady=5)
console.configure(state="disabled")

app.mainloop()

# while True:
#     try:
#         s = input("dart > ")
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parserSintactico.parse(s)
#     if result != None:
#         print(result)
