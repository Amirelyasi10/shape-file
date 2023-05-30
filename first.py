print("#-------------- By Amir -----------#")

from colorama import Fore

print(Fore.RED, "Shape", Fore.RESET)

number = 5

for num in range(1, number + 1):
    shape = num * "*"
    print(shape) 
    
for num in range(number, 0, -1):
    shape = num * "*"
    print(shape) 
