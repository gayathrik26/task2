class Invoice:
    def __init__(self, invoice_number, date, customer_name, items):
        self.invoice_number = invoice_number
        self.date = date
        self.customer_name = customer_name
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def calculate_gst(self):
        gst_rate = 0.18  # 18% GST
        return self.calculate_total() * gst_rate

    def generate_invoice(self):
        invoice_text = f"Invoice Number: {self.invoice_number}\n"
        invoice_text += f"Date: {self.date}\n"
        invoice_text += f"Customer Name: {self.customer_name}\n\n"
        invoice_text += "Items:\n"
        for item in self.items:
            invoice_text += f"{item['description']} - {item['quantity']} x ₹{item['price']:.2f} = ₹{item['quantity'] * item['price']:.2f}\n"
        invoice_text += "\n"
        total_amount = self.calculate_total()
        gst_amount = self.calculate_gst()
        invoice_text += f"Subtotal: ₹{total_amount:.2f}\n"
        invoice_text += f"GST (18%): ₹{gst_amount:.2f}\n"
        invoice_text += f"Total Amount: ₹{total_amount + gst_amount:.2f}\n"
        return invoice_text

def get_item_details():
    items = []
    while True:
        description = input("Enter item description: ")
        quantity = int(input("Enter item quantity: "))
        price = float(input("Enter item price (₹): "))
        items.append({'description': description, 'quantity': quantity, 'price': price})
        
        more_items = input("Add more items? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break
    return items

def main():
    invoice_number = input("Enter invoice number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    customer_name = input("Enter customer name: ")
    
    items = get_item_details()
    
    invoice = Invoice(invoice_number, date, customer_name, items)
    print("\nGenerated Invoice:")
    print(invoice.generate_invoice())

if __name__ == "__main__":
    main()
