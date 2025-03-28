import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * (pow((1 + rate / 100), time)) - principal

    result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")

window = tk.Tk()
window.title("Interest Calculator")
window.geometry("400x300")

tk.Label(window, text="Principal Amount:").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

tk.Label(window, text="Rate of Interest (% per annum):").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

tk.Label(window, text="Time Period (years):").pack()
time_entry = tk.Entry(window)
time_entry.pack()

tk.Button(window, text="Calculate", command=calculate_interest).pack()

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

window.mainloop()
