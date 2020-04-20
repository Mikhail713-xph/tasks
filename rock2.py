# go
import random
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

rock = 1
pepaper = 2
scissors = 3
pointl = 0
pointw = 0
i = 0
print(Fore.BLACK)
print(Back.CYAN)
print('Здраствуйте, это игра: Камень - Ножницы -Бумага ')

a = int(input('Введите колличество раундов:  '))


while i in range(a):
	nomber = int(input('Сделайте выбор: \n Камень под номером 1, Бумага - 2, Ножницы - 3 :  '))
	warrior = random.randint(1,3)
	if nomber == 1:

		if warrior == 1:
			print('У вас Ничья! Противник выбрал: Камень')
		elif warrior == 2:
			print("Вы проиграли:( Противник выбрал: Бумагу")
			pointl = pointl + 1
		else:
			print('Вы Выйграли! Противник выбрал: Ножницы')
			pointw = pointw + 1

	elif nomber == 2:

		if warrior == 2:
			print('У вас Ничья! Противник выбрал: Бумагу')
		elif warrior == 3:
			print("Вы проиграли:( Противник выбрал: Ножницы")
			pointl = pointl + 1
		else:
			print('Вы Выйграли! Противник выбрал: Камень')
			pointw = pointw + 1

	elif nomber == 3:

		if warrior == 3:
			print('У вас Ничья! Противник выбрал: Ножницы')
		elif warrior == 1:
			print("Вы проиграли:( Противник выбрал: Камень")
			pointl = pointl + 1
		else:
			print('Вы Выйграли! Противник выбрал: Бумагу')
			pointw = pointw + 1

	else:
		print('Что - то пошло не так.. Помните, колличество раундов должно быть больше 1,\n а выбрать можно только: Камень, Бумагу или Ножницы. 1,2,3')
	i += 1
	print('Колиичество выйграных матчей: ',pointw,'  Колиичество проигранных матчей: ',pointl)