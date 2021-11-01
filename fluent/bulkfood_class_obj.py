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


class Class:  # Определяем  Class с двумя атрибутами класса: атрибут-данные data  и свойством prop
    """
    стр. 637 Атрибут экземпляра маскирует атрибут-данные класса. Атрибут экземпляра не!! маскирует свойство класса
    """
    data = 'атрибут-данные класса'
    
    @property
    def prop(self):
        return 'значение свойства'

obj = Class()
print(vars(obj))  # vars возвращает атрибут __dict__ объекта obj; как видим атрибутов экземпляра в нем нет.
# {}
print(obj.data)  # Чтение из obj.data возвращает значение Class.data
# атрибут-данные класса
obj.data = "атрибут экземпляра, например, 'bar'"  # Запись в obj.data создает атрибут экземпляра
print(vars(obj))  # Снова инспектируем экземпляр, чтобы узнать, какие у него атрибуты
# {'data': "атрибут экземпляра, например, 'bar'"}
print(obj.data)  # Теперь, читая obj.data, мы получаем значение атрибута экземпляра. Чтение экземпляра obj маскирует атрибут класса data
# атрибут экземпляра, например, 'bar'
print(Class.data)  # Атрибут Class.data не изменился
# атрибут-данные класса

# ! Стр 638! попробуем теперь переопределить атрибут prop экземпляра obj

# ! Атрибут экземпляра НЕ!!(NO!!) маскирует свойство класса
print(Class.prop)  # Чтение prop непосредственно из Class возвращает сам объект свойства, при этом его метод чтения не выполняется.
# <property object at 0x0329E3F0>
print(obj.prop)  # Чтение obj.prop приводит к выполнению метода чтения.
# значение свойства
# obj.prop = 'foo'  # Попытка установить атрибут экземпляра prop завершается ошибкой.
# Traceback ...
# ...
# AttributeError: can't set attribute
obj.__dict__['prop'] = 'foo'  # Запись 'prop' напрямую в __dict__ работает.
print(vars(obj))  # 
# {'data': "атрибут экземпляра, например, 'bar'", 'prop': 'foo'}  # Как видим, теперь у obj есть два атрибута экземпляра: data и prop
print('obj.prop -', obj.prop)  # Однако при чтении obj.prop по-прежнему выполняется метод чтения свойства. Свойства НЕ маскируются атрибутом экземпляра.
# obj.prop значение свойства
Class.prop = 'baz'  # В случае перезаписывания Class.prop объект свойства уничтожается.
print('obj.prop -', obj.prop)  # Теперь чтение obj.prop возвращает атрибут экземпляра. Class.prop больше не является свойством, поэтому и не переопределяет obj.prop
# obj.prop - foo
print('obj.data -', obj.data)  # obj.data возвращает атрибут экземпляра data
# obj.data - атрибут экземпляра, например, 'bar'
print('Class.data -', Class.data)  # Class.data возвращает атрибут класса data
# стр 639 Class.data - атрибут-данные класса
Class.data = property(lambda self: 'the "data" prop value')  # Перезаписываем Class.data полным свойством.
print('obj.data -', obj.data)  # Теперь Class.data маскирует obj.data
# obj.data - the "data" prop value
del Class.data  # Удаляем свойство
print('obj.data -', obj.data)  # Теперь obj.data снова возвращает атрибут экземпляра data
# obj.data - атрибут экземпляра, например, 'bar'

"""
При вычислении выражения вида obj.attr поиск начинается не с obj, а с obj.__class__.


"""
