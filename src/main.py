import customtkinter
import tkinter as tk
from sintactico import parserSintactico, getError
from datetime import datetime

class ParseError(Exception):
    def __init__(self, error, *args):
        super().__init__(args)
        self.error = error

def button_callback():
    text = textbox.get("0.0", "end").rstrip('\n').lstrip()

    console.configure(state='normal')
    console.delete("0.0", "end")
    # console.insert("0.0", text)
    console.insert('0.0', f'[{datetime.now()}] analisys time\n')

    try:
        print('[DEBUG] The text to parse is: ', f'"{text}"')
        result = parserSintactico.parse(text, tracking=True)
        if result != None:
            raise SyntaxError('The syntax on the editor is invalid')
        sinerror, errcnt = getError()
        print(f'[DBG] result of getError(): ({sinerror}, {errcnt})')
        if sinerror:
            if errcnt is not None:
                raise ParseError(errcnt)
            else:
                raise SyntaxError(f'The code is not valid: \'{text}\'')
        console.insert("1.0", "Result: Sintaxis OK!!!\n")
        console.insert("2.0", f"[{datetime.now()}] parsed:\n")
    except SyntaxError as e:
        print('Error while parsing syntax:', e)
        console.insert("2.0", f"[{datetime.now()}] Syntax Error, {e}\n")
        # console.insert("2.0", f"Result: {e}\n")
    except ParseError as e:
        err = e.error
        if err:
            print(f'[DBGERR] The content of err: {err.__dir__()}')
            console.insert("2.0", f"[{datetime.now()}] couldn't parse token {err.type}, value '{err.value}' on line {err.lineno}, lexpos{err.lexpos}\n")
        else:
            console.insert("2.0", f"[{datetime.now()}] error: EOF Error\n")


    console.configure(state='disabled')

def load_content():
    print('Loading the file from fs')
    filename = tk.filedialog.askopenfilename()
    if not filename:
        return
    textbox.delete("0.0", "end")
    lineno = 1
    with open(filename, 'r') as f:
        data = f.read()
        textbox.insert(f"{lineno}.0", data)
        lineno += 1

app = customtkinter.CTk()

app.after(0, lambda: app.wm_state('normal'))
app.title('DartSense')

#Window size
width = app.winfo_screenwidth()
height = app.winfo_screenheight()

center_h = height//2
center_w = width//2

# app.geometry("%dx%d" % (width, height))
app.minsize(center_w, center_h)

load_button = customtkinter.CTkButton(app, text="Load from file", command=load_content)
load_button.pack(padx=10, pady=5)

button = customtkinter.CTkButton(app, text="Run", command=button_callback)
button.pack(pady=10)

textbox = customtkinter.CTkTextbox(app, width=width, height=height*(2/3), corner_radius=5)
textbox.pack(padx=5, pady=5)

label = customtkinter.CTkLabel(app, text="Console")
label.pack(padx=5, pady=5)

monospace_font = customtkinter.CTkFont(family='monospace', size=12)
console = customtkinter.CTkTextbox(app, width=width, height=height*(1/3), corner_radius=5, font=monospace_font)
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
