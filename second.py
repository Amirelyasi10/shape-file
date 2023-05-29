from pyfiglet import figlet_format

print(figlet_format("* * *"))

number = 5
start = 1

for num in range(number, start -1, -1):
    print(num * "*")