import tkinter as tk

def setup_window():
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("400x500")
    return root

def create_display(root):
    display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid")
    display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
    return display

def on_button_click(button_text, display):
    current_text = display.get()
    
    if button_text == "C":
        display.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button_text)

def create_buttons(root, display):
    button_texts = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]
    
    row_val = 1
    col_val = 0

    for text in button_texts:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                           command=lambda t=text: on_button_click(t, display))
        button.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

def main():
    root = setup_window()
    display = create_display(root)
    create_buttons(root, display)
    root.mainloop()

if __name__ == "__main__":
    main()
