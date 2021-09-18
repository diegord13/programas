# name = "ada lovelace"
# print(name.title())

# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print(full_name)
# print("Hello, " + full_name.title() + "!")
# message = "Hello, " + full_name.title() + "!"
# print(message)

# print('Para agregar un espacio tab ¨\t¨')
# print('Para agregar un nuevo espacio hacia abajo \n')


# mammals = ['a','b','c']
# for i in range(len(mammals)):
#     print(i,':',mammals[i])

# a = [1,2,3,4]
# b = ['a','b','c','d']
# z = zip(a,b)

# for pair in zip(a,b):
#     print(pair)

# a,b =zip(*z)
# print(a,b)


# #2.4.2
# p = [4,5,0,2]
# dPdx = []
# for i, c in enumerate(p[1:]):
#     dPdx.append((i+1)*c)
# print(dPdx)

#2,4,3
# list1 = [87,75,75,50,32,32]
# list2 = []
# contador = 0
# for i in range(len(list1[:])):
#     contador  += 1
#     if list1[i] != list1[i -1]:
#         #contador += 1
#         list2.append((contador))
#     else:
#         list2.append((contador - 1))
# print(list1)
# print(list2)

#2.4.4
#pi = sqrt(12)*(1 - 1/3*3 + 1/5*3**2 + 1/7*3**3 ...)

# import math
# pi = 0
# for k in range(50):
#     pi += pow(-3, -k) / (2*k+1)

# pi *= math.sqrt(12)
# print('pi = ', pi)
# #pi = 3.1415926535714034
# print('error = ', abs(pi - math.pi))
# error = 1.8389734179891093e-11
        
# encontrar la matriz p donde el valor p[i] = al valor de la multiplicacion de los valores de a a excepcion
#de a[i]
a = [3,6,7]
p = []
for i in range(len(a)):
    b=1
    for j in range(len(a)):
        b *= a[j]
    p.append(b)
    p[i] = p[i] // a[i]
print(p)




