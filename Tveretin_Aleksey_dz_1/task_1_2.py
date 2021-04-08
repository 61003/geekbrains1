def find_magic_sum(cubes):
    sum_of_div7 = 0
    for cube in cubes:
        remain = cube
        sum_of_digits = 0
        for digits in range(len(str(cube)), 0, -1):
            digit_degree = 10 ** (digits - 1)
            digit = remain // digit_degree
            remain -= digit_degree * digit
            sum_of_digits += digit
        if sum_of_digits % 7 == 0:
            sum_of_div7 += sum_of_digits
    return sum_of_div7


cubes = []
for number in range(1, 1000, 2):
    cubes.append(number ** 3)
sum = find_magic_sum(cubes)
print('Сумма всех чисел по задаче "a"= {}'.format(sum))

cubes_plus_17 = []
for cube in cubes:
    cubes_plus_17.append(cube + 17)
sum = find_magic_sum(cubes_plus_17)
print('Сумма всех чисел по задаче "b"= {}'.format(sum))

for cube_index in range(len(cubes)):
    cubes[cube_index] += 17

sum = find_magic_sum(cubes)
print('Сумма всех чисел по задаче "c"= {}'.format(sum))
