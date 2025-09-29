# # task1.1
# a, b = map(int, input().split())
# def task1(a,b):
#     if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
#         return a + b
# print(task1(a, b))

# # task1.2
# def task2(a,b):
#     if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
#         return a + b**2
# print(task2(a, b))

# # task1.3
# f = open('task3').readline()
# def task3(f):
#     a, b = map(int, f.split())
#     if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
#         return a + b
# print(task3(f))

# # task1.4
# f = open('task3').readline()
# def task3(f):
#     a, b = map(int, f.split())
#     if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
#         return a + b**2
# print(task3(f))

# # task 2
# def calc_fib(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
# with open('input.txt', 'r') as file_in:
#     # 8. Чтение всего содержимого файла, удаление лишних пробелов и преобразование в число
#     n = int(file_in.read().strip())
# res = calc_fib(n)
#
# with open('output.txt', 'w') as file_out:
#     file_out.write(str(res))
#
# # task 3
# def fib_last_num(n):
#     if n <= 1:
#         return n
#
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, (a + b) % 10  # сохраняем только последнюю цифру
#     return b
#
# with open('input.txt', 'r') as file_in:
#     n = int(file_in.read().strip())
#
# res = fib_last_num(n)
#
# with open('output.txt', 'w') as file_out:
#     file_out.write(str(res))
