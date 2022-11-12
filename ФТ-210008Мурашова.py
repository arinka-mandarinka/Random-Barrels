import logging
import random
import os

logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
os.system('cls')

# Ввод числа пользователем.
while True:
    try:
        logging.info('Пользователь вводит количество бочонков')
        count = int(input('Введите количество бочонков: '))
        logging.info(f'Пользователь ввел: {count}')
    except:
        print('Неверно введенно число. Попробуйте ещё раз!')
        logging.error('Введенное значение пользователем было неверным', exc_info=True)
        continue

    if count < 1:
        print('Число должно быть больше 1. Попробуйте ещё раз!')
        logging.error('Введенное число было меньше 1')
        continue

    logging.info(f'Верно введенно число пользователем: {count}')
    break

# Заполнение списка и его перемешивание.
burrels = []
for i in range(1, count + 1):
    burrels.append(i)
random.shuffle(burrels)
logging.info(f'Получившийся перемешанный список боченков: {burrels}')

# Выкидываем каждый раз последнее число из списка.
print()
for i in range(len(burrels)):
    bur = burrels.pop()
    print(f'Случайно выпавший бочонок с номером: {bur}')
    logging.info(f'Выпавшее число пользователю: {bur}')
    input('Нажмите enter для следующего бочонка...')