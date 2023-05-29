from pyfiglet import figlet_format

print(figlet_format("* * *"))

number = 5

for num in range(1, number + 1):
    shape = num * "*"
    print(Fore.RED , shape ,Fore.RESET) 