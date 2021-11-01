"""
стр. 633 Магазин, продающий натуральные продукты по весу.
Заказ состоит из последовательности строк. Строка представлена классом LineItem
Проблема в том, что можно задать отрицательный вес: raisins = LineItem('Golden raisins', -20, 6.95)  raisins.subtotal() = 139.0
"""
class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price
