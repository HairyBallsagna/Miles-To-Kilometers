from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{round(km, 2)}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=20)

miles_input = Entry(width=9)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=5)

is_equal_label = Label(text="TO KILOMETERS:")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=5)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(padx=10, pady=5)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=10, pady=5)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10)



window.mainloop()