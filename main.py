class Training:
    """ Общий класс для тренировок."""
    LEN_STEP = 0.65  # расстояние за один шаг.
    M_IN_KM = 1000

    def __init__(self, action: int, duration: int, weight: int):
        """
            Получение информации с датчиков:
            action - колличество действий;
            duration - длительность тренировки;
            weight - вес спортсмена.
        """
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self):
        pass

    def get_mean_speed(self):
        pass

    def get_spent_calories(self):
        pass


class Running(Training):
    """ Класс тренировок по бегу."""
    pass


class SportsWalking(Training):
    """ Класс тренировок по ходьбе."""
    pass


class Swimming(Training):
    """ Класс тренировок по плаванью"""
    pass


class InfoMassage:
    def __init__(self, training_type, duration, speed, calories):
        pass

    def show_training_info(self):
        pass

    def get_message(self):
        print(Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.)
