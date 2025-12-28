import tkinter as tk
from tkinter import ttk, messagebox



class RestaurantOrderManagement:

    def __init__(self, root):
        self.root = root  
        self.root.title(
            "Restaurant Management App")
       
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  

      
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 

   

ttk.Label(Frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

self.menu_labels = {}  
self.menu_quantities = {}  




self.currency_var = tk.StringVar()
ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(
    row=len(self.menu_items) + 1, column=0, padx=10, pady=5
)


currency_dropdown = ttk.Combobox(
    frame,
    textvariable=self.currency_var,
    state="readonly",
    width=18,
    values=("USD", "INR")
)
currency_dropdown.grid(row=len(self.menu_items) + 1, column=1, padx=10, pady=5)
currency_dropdown.current(0)  # Set default currency

self.currency_var.trace('w', self.update_menu_prices)


order_button = ttk.Button(Frame, text="Place Order", command=self.place_order)
order_button.grid(row=len(self.menu_items) + 2, columnspan=3, padx=10, pady=10)


def update_menu_prices(self, *args):
    currency = self.currency_var.get()
    symbol = "₹" if currency == "INR" else "$"
rate = self.exchange_rate if currency == "INR" else 1

for item, entry in self.menu_quantities.items():
    quantity = entry.get()
    if quantity.isdigit():
        quantity = int(quantity)
        price = self.menu_items[item] * rate
        cost = quantity * price
        total_cost += cost

        if quantity > 0:
            order_summary += (f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n")
            if total_cost > 0: 
                order_summary += f"\nTotal Cost: {symbol}{total_cost}"
    messagebox.showinfo("Order Placed", order_summary)  # Show order summary in a message box
else:
    # Show error if no items are ordered
    messagebox.showerror("Error", "Please order at least one item.")

