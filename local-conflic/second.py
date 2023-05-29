from colorama import Fore

number = 5
start = 1

for num in range(number, start -1, -1):
    shape = num * "*"
    print(Fore.RED, shape, Fore.RESET)