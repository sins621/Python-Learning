import tkinter as tk


def miles_to_km():
    miles = float(en_miles.get())
    kilos = round(miles * 1.60934, 2)
    lb_kilo_value.config(text=f"{kilos}")


window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

en_miles = tk.Entry(width=30)
en_miles.grid(column=1, row=0)

lb_miles = tk.Label(text="Miles")
lb_miles.grid(column=2, row=0)

lb_equal_to = tk.Label(text="is equal to")
lb_equal_to.grid(column=0, row=1)

lb_kilo_value = tk.Label(text="0")
lb_kilo_value.grid(column=1, row=1)

lb_kilo = tk.Label(text="Km")
lb_kilo.grid(column=2, row=1)

bt_calculate = tk.Button(text="Calculate", command=miles_to_km)
bt_calculate.grid(column=1, row=2)


window.mainloop()
