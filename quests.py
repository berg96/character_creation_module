# Импортируйте datetime.
import datetime as dt
# Импортируйте time.
import time


class Quest:

    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        # Допишите два свойства класса.
        self.start_time = None
        self.end_time = None

    # Напишите методы приема и сдачи квеста.
    def accept_quest(self):
        if self.end_time is None:
            self.start_time = dt.datetime.now()
            return f'Начало квеста "{self.name}" положено.'
        else:
            return 'С этим испытанием вы уже справились.'

    def pass_quest(self):
        if self.start_time is not None:
            self.end_time = dt.datetime.now()
            completion_time = self.end_time - self.start_time
            return (f'Квест "{self.name}" окончен. '
                    f'Время выполнения квеста: {completion_time}')
        else:
            return 'Нельзя завершить то, что не имеет начала!'

    def __str__(self):
        if self.start_time is not None:
            if self.end_time is not None:
                return (f'Цель квеста {self.name} - {self.goal}. '
                        'Квест завершён.')
            else:
                return (f'Цель квеста {self.name} - {self.goal}. '
                        'Квест выполняется.')
        else:
            return f'Цель квеста {self.name} - {self.goal}.'


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

print(new_quest)
