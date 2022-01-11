# Task 1
# вивести на екран усі можливі варіанти порівняння трьох змінних
x = '10'
y = '5'
z = '20'
x_1 = int(x)
y_1 = int(y)
z_1 = int(z)
print(x_1==y_1)
print(x_1!=y_1)
print(x_1==z_1)
print(x_1!=z_1)
print(y_1==z_1)
print(y_1!=z_1)
print(x_1<y_1)
print(x_1>y_1)
print(x_1>=y_1)
print(x_1<=y_1)
print(x_1<z_1)
print(x_1>z_1)
print(x_1>=z_1)
print(x_1<=z_1)
print(y_1>z_1)
print(y_1<z_1)
print(y_1>=z_1)
print(y_1<=z_1)
print(x_1 < y_1 <z_1)
print(y_1 <z_1 < x_1)
print(y_1 <x_1 < z_1)



# Task 2 
# Використовуючи методи str на прикладі даної стрічки вивести на екран:видалити усі пробіли зліва та справа,к-ть символів 'a',given_string у верхньому регістрі(усі букви заголовні/великі),given_string н нижньому регістрі,в given_string замінити 'super power' на 'tasty breakfast' і вивести усе на екран,перевірити чи складається given_string з букв,замінити усі пробіли на дефіс, а i на 1

given_string = '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
print(given_string.strip())
print(given_string.count('a'))
print(given_string.upper())
print(given_string.lower())
print(given_string.replace('super power','tasty breakfast'))
print(given_string.isalpha())
print(given_string.replace('','-'))
print(given_string.replace('i','1'))


# Task 3 
# Написати програму, яка питає ім'я користувача. 

xy =  input("Введіть своє ім'я: ")
x_1 = input(f"Привіт {xy}! Введіть своє призвіще: ")
x_2 = input(f"{xy} {x_1} , введіть своє ім'я по-батькові: ")
x_3 = input(f"{x_1} {xy} {x_2}, введіть свій рік народження: ")
print(f"ПІП: {x_1[0]}{xy[0]}{x_2[0]}\nПрізвище: {x_1}\nІм'я: {xy}\nПо-батькові: {x_2}\nДата народження: {x_3}")
