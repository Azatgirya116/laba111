import doctest

class KettlebellPhysics:
    def __init__(self, kettlebell_weight:float, kettlebell_density:float ):
        """
        Создание и подготовка к работе объекта "Физические свойства гири"
        :param kettlebell_weight: Масса гири
        :param kettlebell_density: Плотность гири

        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0) # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_weight, (int, float)):
            raise TypeError("Масса гири должена быть типа int или float")
        if kettlebell_weight < 0:
            raise ValueError("Масса гири должна быть положительным числом больше нуля")
        self.kettlebell_weight = kettlebell_weight
        if not isinstance(kettlebell_density, (int, float)):
            raise TypeError("Плотность гири должна быть int или float ")
        if kettlebell_density < 0:
            raise ValueError("Плотность гири должна быть положительным числом больше нуля")
        self.kettlebell_density = kettlebell_density

    def ability_lift_kettlebell(self) -> bool:
        """
        Функция которая определяет может ли человек поднять гирю
        :return: Может или не может
        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0)
        >>> kettlebell.ability_lift_kettlebell()
        """

    def ability_break_kettlebell (self,kettlebell_force: int) -> bool:
        """
        Функция которая определяет можно ли сломать гирю
        :param kettlebell_force: Сила удара по гире, Н
        :return: Сломается или нет

        Примеры:
        >>> kettlebell = KettlebellPhysics(10.0, 10.0)
        >>> kettlebell.ability_break_kettlebell(99)
        """
        if not isinstance(kettlebell_force , (int, float)):
            raise TypeError("Сила удара должна быть типа int или float")
        if kettlebell_force < 0:
            raise ValueError("Сила удара должна быть положительным числом")
class KettlebellAppearance:
    def __init__(self, kettlebell_colour: str, kettlebell_shape: str):
        """
        Создание и подготовка к работе объекта "Внешний вид гири"
        :param kettlebell_colour: Цвет гири
        :param kettlebell_shape: Форма гири

        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленая', 'круглая')  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_colour, str):
            raise TypeError("Цвет гири должен быть типа str")
        self.kettlebell_colour = kettlebell_colour
        if not isinstance(kettlebell_shape, str):
            raise TypeError("Форма гири должна быть типа str")
    def beauty_kettlebell (self) -> bool:
        """
        Функция которая определяет входит ли эта гиря в список красивых гирь
        :return: Красивая гиря или нет

        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленая', 'круглая')
        >>> kettlebell.beauty_kettlebell()
        """

    def rolling_kettlebell(self) -> float:
        """
        Функция которая считает вероятность того, что гиря указанной формы покатится
        :return: Вероятность качения
        Примеры:
        >>> kettlebell = KettlebellAppearance('зеленая', 'круглая')
        >>> kettlebell.rolling_kettlebell()
        """

class KettlebellСollection:
    def __init__(self, kettlebell_number:int, kettlebell_price:float ):
        """
        Создание и подготовка к работе объекта "Коллекция гирь"
        :param kettlebell_number: Колличество гирь в коллекции
        :param kettlebell_price: Стоимость всех гирь
         Примеры:

        >>> kettlebell = KettlebellСollection(999, 189000)  # инициализация экземпляра класса
        """
        if not isinstance(kettlebell_number, int):
            raise TypeError("Число гирь в коллекции должно быть типа int")
        if kettlebell_number < 0:
            raise ValueError("Число гирь в коллекции должно быть положительным числом")
        self.kettlebell_number = kettlebell_number
        if not isinstance(kettlebell_price, (int, float)):
            raise TypeError("Цена гирь в коллекции должна быть типа int или float")
        if kettlebell_price < 0:
            raise ValueError("Цена гирь в коллекции должна быть положительным числом")
        self.kettlebell_price = kettlebell_price
    def single_kettlebell (self) -> float:
        """
        Функция которая определяет цену одной гири
        :return: Цена одной гири

        Примеры:
        >>> kettlebell  = KettlebellСollection(999, 189000)
        >>> kettlebell.single_kettlebell()
        """
        ...
    def comparison_collections (self,largest_collection:int ) -> bool:
        """
         Функция которая определяет больше ли моя коллекция гирь самой большой коллекции гирь
         :param largest_collection: Наибольшая известная коллекция гирь, число гирь
         :return: Да или нет
        Примеры:
        >>> kettlebell = KettlebellСollection(999, 189000)
        >>> kettlebell.comparison_collections(10)
        """
        if not isinstance(largest_collection, int):
            raise TypeError("Число гирь наибольшей коллекции должно быть типа int")
        if largest_collection < 0:
            raise ValueError("Число гирь наибольшей коллекции должено быть положительным числом")

if __name__ == "__main__":
    doctest.testmod()
