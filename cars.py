{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

		