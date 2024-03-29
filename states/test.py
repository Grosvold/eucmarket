from aiogram.dispatcher.filters.state import StatesGroup, State


# Создаем группу состояний Test - для тестирования.
# Если у вас другой смысл состояний - называйте соответственно, не надо тупо копировать Test
class AdvertQA(StatesGroup):
    # Создаем состояние в этой группе. Называйте каждое состояние соответственно его назначению.
    # В данном случае Q1 - question 1, то есть первый вопрос. У вас это может быть по-другому
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
