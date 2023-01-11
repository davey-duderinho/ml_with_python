"""Udacity OOP"""


class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
print(f"The price of the shirt is ${shirt_one.price}")
shirt_one.change_price(10)
print(f"The changed price of the shirt is ${shirt_one.price}")

print(f"The discounted price of the shirt is ${shirt_one.discount(0.12)}")

shirt_two = Shirt('orange', 'L', 'short_sleeve', 10)
total = shirt_one.price + shirt_two.price
total_discount = shirt_one.discount(0.14) + shirt_two.discount(0.06)
print(f'Total discount price of both shirts is {total_discount}')
