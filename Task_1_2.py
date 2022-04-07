"""1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
операции!
2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список."""

# 1 вычислим сумму

list_cub = [x**3 for x in range(1000) if x % 2 != 0]
print('Список кубов нечетных чисел {}'.format(list_cub));

my_num_sum = 0
my_num_sum_list = []

for i in range(len(list_cub)):
    my_str = str(list_cub[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    for i in range(len(my_list)):
        my_num_sum = my_num_sum + my_list[i]
    if my_num_sum % 7 == 0:
        print('Сумма чисел, делящихся на 7: ', my_num_sum)
        my_num_sum_list.append(my_num_sum)
print('Список чисел, делящихся на 7:', my_num_sum_list)

# 2 Добавим 17

cubes = [(x**3)+17 for x in range(1000) if x % 2 == 0]
print('Список кубов нечетных чисел {}'.format(cubes));
my_num_sum = 0
my_num_sum_list_even = []

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    for i in range(len(my_list)):
        my_num_sum = my_num_sum + my_list[i]

    if my_num_sum % 7 == 0:
        print('Сумма чисел, делящихся на 7: ', my_num_sum)
        my_num_sum_list_even.append(my_num_sum)
print('Список чисел, делящихся на 7: ', my_num_sum_list_even)
