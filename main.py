number = int(input("Введите число: "))
print("Четные числа", number)
for i in range(number + 1):
  if i % 2 == 0:
    print(i)






x = int(input("Введи значение x:"))  
i = 1
res = 1
while i <= x:
    res *= i
    i += 1
print(res)
