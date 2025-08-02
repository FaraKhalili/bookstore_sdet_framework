from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float

    def get_info(self):
        return f"{self.title} by {self.author} costs ${self.price}"

    def discount_price(self, percentage):
        return round(self.price * (1 - percentage), 2)
