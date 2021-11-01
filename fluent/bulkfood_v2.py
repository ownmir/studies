"""
стр. 634 Магазин, продающий натуральные продукты по весу.
Заказ состоит из последовательности строк. Строка представлена классом LineItem
Теперь нельзя задать отрицательный вес: raisins = LineItem('Golden raisins', -20, 6.95)  Traceback ... ValueError: value must be > 0
"""
class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # Здесь уже используется метод установки свойства, который гарантирует, что не может быть создан экземпляр с отрицательным значением weight. При этом не меняется интерфейс класса (какБ например в Java - get_weight, set_weight)
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price
    
    @property  # Этим декоратором обозначается метод чтения свойства
    def weight(self):  # Имена всех методов, реализующих свойство, совпадают с именем открытого атрибута: weight
        return self.__weight  # Фактическое значение хранится в закрытом атрибуте __weight
    
    @weight.setter  # У декорированного метода чтения свойства имеется атрибут .setter, который является также и декоратором; тем самым методы чтения и установки связываются между собой.
    def weight(self, value):
        if value > 0:
            self.__weight = value  # присваиваем
        else:
            raise ValueError('value must be > 0')  # возбуждаем исключение


raisins = LineItem('Golden raisins', -20, 6.95)
