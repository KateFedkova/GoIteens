exersice = """#########
#     #
#     #
#     #
#########

#     #
#     #
#########
#     #
#     #"""
print(exersice)



song = """We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine
Yellow submarine, yellow submarine

We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine
Yellow submarine, yellow submarine"""
print(song)

song_1 = '\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\n\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\nWe all live in a yellow submarine\nYellow submarine, yellow submarine'
print(song_1)

print('Федькова\tКатерина')


start_string = "abcdefghijklmn"
print(len(start_string))
print(start_string[0:4])
print(start_string[9:14])
print(start_string[5:9])
print(start_string[:: 2])
x = 3
y = 9
print(f' Сума {x}+{y}= {x+y}')
print(f' Віднімання {x}-{y}= {x-y}')
print(f' Множення {x}*{y}= {x*y}')
print(f' Ділення {x}/{y}= {x/y}')
print(f' Степінь {x}**{y}= {x**y}')
print(f' Цілочисельне {x}//{y}= {x//y}')
print(f' Оcтача {x}%{y}= {x%y}')


string = "abcdef"
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)

message = "Test program"
# check if the message ends with program
print(message.endswith('program'))