class ShoppingCart:
    taxrate = 0.1

    def __init__(self):
        self.items = []

    @staticmethod
    def pricevalidation(price):
        return price > 0

    @staticmethod
    def discount(subtotal, code):
        if code == "2005":
            return subtotal - subtotal / 100 * 10
        return subtotal

    @staticmethod
    def tax(amount, taxrate):
        return amount * taxrate

    def additem(self, name, price, quantity):
        if not name or not self.pricevalidation(price) or quantity < 1:
            return False

        for item in self.items:
            if item["name"].lower() == name.lower():
                item["quantity"] += quantity
                return True

        self.items.append({"name": name, "price": price, "quantity": quantity})
        return True

    def get_subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def checkout(self, code=""):
        subtotal = self.get_subtotal()
        discounted = self.discount(subtotal, code)
        tax = self.tax(discounted, self.taxrate)
        return {
            "subtotal": subtotal,
            "discount": subtotal - discounted,
            "tax": tax,
            "total": discounted + tax,
        }





