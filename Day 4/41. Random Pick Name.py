import random

name_list = input("Give names separated by a coma ")

names = name_list.split(", ")

print(names[random.randint(0, len(names) - 1)])