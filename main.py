import tkinter as tk

calculation = ""

num_button_col = "#142f44"
op_button_col = "#205b7a"
txt_fld_col = "#a2bbcf"
res_button_col = "#ff9500"
clr_button_col = "#dd2d00"
bg_col = "#1d3849"

num_button_col_press = "#0b1b28"
op_button_col_press = "#153c51"
clr_button_col_press = "#801a00"
res_button_col_press = "#b36800"

num_button_col_hover = "#060e14"

calculation_txt_col = "#000000"

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.config(fg = num_button_col)
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        # calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_result.config(fg = calculation_txt_col)
        calculation = ""
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.config(fg = num_button_col)
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("291x275")
root.configure(bg = bg_col)

text_result = tk.Text(root, height = 2, width = 16, font=("Arial", 24), bg = txt_fld_col, fg = num_button_col)
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text = "1", command=lambda: add_to_calculation(1), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(root, text = "2", command=lambda: add_to_calculation(2), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(root, text = "3", command=lambda: add_to_calculation(3), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(root, text = "4", command=lambda: add_to_calculation(4), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(root, text = "5", command=lambda: add_to_calculation(5), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(root, text = "6", command=lambda: add_to_calculation(6), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(root, text = "7", command=lambda: add_to_calculation(7), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(root, text = "8", command=lambda: add_to_calculation(8), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(root, text = "9", command=lambda: add_to_calculation(9), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(root, text = "0", command=lambda: add_to_calculation(0), width = 5, font = ("Arial", 14), bg = num_button_col, fg = txt_fld_col, activebackground=num_button_col_press, activeforeground=txt_fld_col)
btn_0.grid(row = 5, column = 2)

btn_plus = tk.Button(root, text = "+", command=lambda: add_to_calculation("+"), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(root, text = "-", command=lambda: add_to_calculation("-"), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_minus.grid(row = 3, column = 4)
btn_mul = tk.Button(root, text = "*", command=lambda: add_to_calculation("*"), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_mul.grid(row = 4, column = 4)
btn_div = tk.Button(root, text = "/", command=lambda: add_to_calculation("/"), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_div.grid(row = 5, column = 4)

btn_open = tk.Button(root, text = "(", command=lambda: add_to_calculation("("), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(root, text = ")", command=lambda: add_to_calculation(")"), width = 5, font = ("Arial", 14), bg = op_button_col, activebackground= op_button_col_press, activeforeground= txt_fld_col)
btn_close.grid(row = 5, column = 3)

btn_equals = tk.Button(root, text = "=", command=evaluate_calculation, width = 11, font = ("Arial", 14), bg = res_button_col, activebackground = res_button_col_press)
btn_equals.grid(row = 6, column = 3, columnspan=2)
btn_clear = tk.Button(root, text = "C", command=clear_field, width = 11, font = ("Arial", 14), bg = clr_button_col, activebackground = clr_button_col_press)
btn_clear.grid(row = 6, column = 1, columnspan=2)
root.mainloop()