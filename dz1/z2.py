# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

a = 10
b = 10
c = 10

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    print('такого треугольника не существует')
elif a == b and a == c:
    print('треугольник равносторонний')
elif a == b or a == c or b == c:
    print('треугольник равнобедренный')
else:
    print('треугольник существует')