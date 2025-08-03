from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float

    def get_info(self) -> str:
        return f"{self.title} by {self.author} costs ${self.price}"

    def discount_price(self, percentage) -> float:
        return round(self.price * (1 - percentage), 2)
