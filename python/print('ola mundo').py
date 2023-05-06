list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 - num2) #diferença
print(num1 | num2) #uniom
print(num1 ^ num2) #tira os valores iguais
print(num1 & num2) #ADD
