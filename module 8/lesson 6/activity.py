import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "FRIES MEAL": 2.0,
            "LUNCH MEAL": 2.0,
            "BURGER MEAL": 3.0,
            "CHEESE BURGER": 2.5,
            "PIZZA MEAL": 4.0,
            "DRINKS": 1.0
        }

        self.exchange_rate = 120.0  

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold"),
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price:.2f}):",
                font=("Arial", 12),
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = (price, quantity_entry)

        self.currency_var = tk.StringVar()
        ttk.Label(
            frame, 
            text="Currency:", 
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1, 
            column=0, 
            padx=10, 
            pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=["USD", "BDT"],
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1, 
            column=1, 
            padx=10, 
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace_add("write", self.update_menu_prices)

        # Place the order button right after the dropdown
        order_button = ttk.Button(
            frame, 
            text="Place Order", 
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2, 
            column=0, 
            columnspan=2, 
            pady=15
        )

    def update_menu_prices(self, *args):
        """Updates the menu labels based on the selected currency."""
        currency = self.currency_var.get()
        for item, price in self.menu_items.items():
            if currency == "BDT":
                converted_price = price * self.exchange_rate
                symbol = "TK"
            else:
                converted_price = price
                symbol = "$"
            
            self.menu_labels[item].config(text=f"{item} ({symbol}{converted_price:.2f}):")

    def place_order(self):
        """Calculates the total and displays an order summary receipt."""
        total_cost = 0.0
        receipt_items = []
        currency = self.currency_var.get()
        symbol = "TK" if currency == "BDT" else "$"

        for item, (price, entry) in self.menu_quantities.items():
            qty_str = entry.get().strip()
            if qty_str:  # Skip empty fields
                try:
                    qty = int(qty_str)
                    if qty < 0:
                        raise ValueError
                    if qty > 0:
                        item_price = price * self.exchange_rate if currency == "BDT" else price
                        item_total = item_price * qty
                        total_cost += item_total
                        receipt_items.append(f"{item} x{qty}: {symbol}{item_total:.2f}")
                except ValueError:
                    messagebox.showerror("Error", f"Please enter a valid positive integer for {item}.")
                    return

        if not receipt_items:
            messagebox.showinfo("Empty Order", "Please select at least one item to order.")
            return

        # Generate and show receipt
        receipt_text = "\n".join(receipt_items)
        receipt_text += f"\n\nTotal Bill: {symbol}{total_cost:.2f}"
        messagebox.showinfo("Order Receipt", receipt_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x450")
    app = RestaurantOrderManagement(root)
    root.mainloop()
