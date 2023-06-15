# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 10
print(num)
while count > 0:
    targ = int(input(f"угадай число, осталось {count} попыток: "))
    count -= 1

    if targ == num:
        print("ты угадал")
        break

    print("меньше" if targ > num else "больше")

