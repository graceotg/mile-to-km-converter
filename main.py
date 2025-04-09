from tkinter import *

def calculate_button():
    user_input = float(entry.get())
    calc_answer = round(user_input * 1.60934, 3)
    answer_label.config(text=calc_answer)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=250, pady=150)

answer_label = Label(text=0, font=("Arial", 20))
answer_label.grid(row=1, column=1)

equal_to_label = Label(text="is equal to", font=("Arial", 20))
equal_to_label.grid(row=1, column=0)

km_label = Label(text="Km",font=("Arial", 20))
km_label.grid(row=1, column=2)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=2)


button = Button(text="Calculate", command=calculate_button, font=("Arial", 20), width=10)
button.grid(row=2, column=1)

entry = Entry(width=15)
entry.grid(row=0, column=1)





window.mainloop()
