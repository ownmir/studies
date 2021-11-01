"""
стр. 640 Магазин, продающий натуральные продукты по весу.
Заказ состоит из последовательности строк. Строка представлена классом LineItem
Теперь нельзя задать отрицательный вес: raisins = LineItem('Golden raisins', -20, 6.95)  Traceback ... ValueError: value must be > 0
Фабрика свойств.
"""
class LineItem:
    weight = quantity('weight')  # Используем фабрику для определения свойства weight в виде атрибута класса
    price = quantity('price')
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # Здесь своство уже работает, и поэтому попытка присвоить weight нулевое или отрицательное значение отвергается
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price  # Здесь свойства также работают: с их помощью производится доступ к значениям, хранящимся в экземпляре.
    
    
    def quantity(storage_name):  # Аргумент storage_name определяет, где хранятся данные свойства; в случае свойства weight данные будут хранится в атрибуте с именем "weight"
        
        def getter_quantity(instance):  # Называть первый аргумент метода getter_quantity именем self было бы не совсем правильно, так как это не тело класса; instance ссылается на экземпляр LineItem, в котором будет храниться атрибут.
            return instance.__dict__[storage_name]  # Метод getter_quantity ссылается на storage_name, поэтому будет сохранен в замыкании этой функции; значение берется непосредственно из instance.__dict__, стобы обойти свойство и избежать бесконечной рекурсии.
    
        def setter_quantity(instance, value):  # 1й аргумент также instance
            if value > 0:
                instance.__dict__[storage_name] = value  # присваиваем тоже в обход свойства
            else:
                raise ValueError('value must be > 0')  # возбуждаем исключение

        return property(getter_quantity, setter_quantity)  # конструируем и возвращаем объект свойства.
