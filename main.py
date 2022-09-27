class Training:
    """ Общий класс для тренировок."""
    LEN_STEP = 0.65  # расстояние за один шаг.
    M_IN_KM = 1000   # количество метров в 1 километре.

    def __init__(self, action: int, duration: float, weight: float):
        self.action = action        # колличество действий
        self.duration = duration    # длительность тренировки
        self.weight = weight        # вес спортсмена

    def get_distance(self):
        # преодоленная_дистанция_за_тренировку в км
        return self.action * Training.LEN_STEP / Training.M_IN_KM

    def get_mean_speed(self):
        #  значение средней скорости движения во время тренировки
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        # возвращает количество килокалорий, израсходованных за время тренировки
        # логика подсчета калорий для каждого вида тренировки своя
        pass


class Running(Training):
    """ Класс тренировок по бегу."""
    def __init__(self, action: int, duration: float, weight: float):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(action, duration, weight)

    # переопределяем родительский метод get_spent_calories()
    def get_spent_calories(self):
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        m_in_h = 60
        return (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2) * self.weight * (self.duration * m_in_h)


class SportsWalking(Training):
    """ Класс тренировок по ходьбе."""
    def __init__(self, action: int, duration: float, weight: float, height: float):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(action, duration, weight)
        # принимаем дополнительный параметр
        self.height = height

    # переопределяем родительский метод get_spent_calories()
    def get_spent_calories(self):
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        m_in_h = 60
        return ((coeff_calorie_1 * self.weight +
                (self.get_mean_speed() ** 2 // self.height) * coeff_calorie_2 * self.weight) *
                (self.duration * m_in_h))


class Swimming(Training):
    """ Класс тренировок по плаванью."""
    LEN_STEP = 1.38  # расстояние за один гребок.

    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: int):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(action, duration, weight)
        # принимаем дополнительные параметры
        self.length_pool = length_pool
        self.count_pool = count_pool

    # переопределяем родительский метод get_mean_speed()
    def get_mean_speed(self):
        return self.length_pool * self.count_pool / Training.M_IN_KM / self.duration

    # переопределяем родительский метод get_spent_calories()
    def get_spent_calories(self):
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


class InfoMassage:
    """ Класс для создания объектов сообщений."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def show_training_info(self):
        """ Метод который возвращает объект класса сообщения."""
        info = InfoMassage(self)
        return info

    def get_message(self):
        """ Метод который возвращает строку сообщения."""
        return (f"Тип тренировки: {self.training_type}; "
                f"Длительность: {self.duration} ч.; "
                f"Дистанция: {round(self.distance,3)} км; "
                f"Ср. скорость: {round(self.speed, 3)} км/ч; "
                f"Потрачено ккал: {round(self.calories, 3)}.")


def read_package(workout_type, data):
    """ Функция чтения принятых пакетов."""
    training_dict = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking
                     }
    return training_dict[workout_type](data)


def main(training: Training):
    pass

    """ Функция main() должна принимать на вход экземпляр класса Training.
        При выполнении функции main()для этого экземпляра должен быть вызван метод show_training_info();
        результатом выполнения метода должен быть объект класса InfoMessage, его нужно сохранить в переменную info.
        Для объекта InfoMessage, сохранённого в переменной info, должен быть вызван метод, который вернет строку
        сообщения с данными о тренировке; эту строку нужно передать в функцию print().
    """


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),  # количество гребков, время в часах, вес пользователя, длина бассейна,
                                        # сколько раз пользователь переплыл бассейн.
        ('RUN', [15000, 1, 75]),        # количество шагов, время в часах, вес пользователя.
        ('WLK', [9000, 1, 75, 180]),    # количество шагов, время в часах, вес пользователя, рост пользователя.
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
