import wikipedia
from colorama import init, Fore, Back
init()



search = input(Fore.RED + "wiki: ")
result = Fore.BLUE + wikipedia.summary(search)

print('\n')
print(f"Result for: {search}")
print(result)