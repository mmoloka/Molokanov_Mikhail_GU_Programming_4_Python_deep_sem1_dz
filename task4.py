''' Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
    from random import randint
    num = randint(LOWER_LIMIT, UPPER_LIMIT) '''

from random import randint
num = randint(0, 1000)
start = 0
end = 1000
tries = 1
guess = (end - start) // 2

if guess == num:
    print('Попадание с первой попытки! Загадано число 500.')
else:
    while guess != num:
        if num > guess:
            print(f'Попытка: {tries}, число: {guess}, результат: больше.')
            start = guess
            guess += (end - start) // 2
        else:
            print(f'Попытка: {tries}, число: {guess}, результат: меньше.')
            end = guess
            guess -= (end - start) // 2
        tries += 1
    print(f'Попытка: {tries}, число: {guess}, Загадано число {num}.')        
