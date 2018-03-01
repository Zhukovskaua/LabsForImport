print("Ноль в качестве знака операции завершит работу программы")
print("В операции Not будет обрабатываться переменная x")
while True:
	s = input("Выберите операцию (xor,or,and,not): ")
	if s == '0': break
	if s in ('xor','or','and','not'):
		x = int(input("x="))
		y = int(input("y="))
		if s == 'xor':
			print("%.2f" % (x&y))
		elif s == 'or':
			print("%.2f" % (x|y))
		elif s == 'and':
			print("%.2f" % (x^y))
		elif s == 'not':
			if x != 0:
				print("%.2f" % (~x))
			else:
				print("Деление на ноль!")
	else:
		print("Неверный знак операции!")