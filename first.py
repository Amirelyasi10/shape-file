from colorama import Fore

number = 5

for num in range(1, number + 1):
    shape = num * "*"
    print(Fore.RED , shape ,Fore.RESET) 