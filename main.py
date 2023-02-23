# Welcome to the banker roulette 
import random

names_string = input("Add the names joining the payment roulette (separete with ',') \n")

names = names_string.split(", ")
total_names = len(names)

random_number = random.randint(0, total_names -1)

print(f"The choosed's name is : \n {names[random_number]}")