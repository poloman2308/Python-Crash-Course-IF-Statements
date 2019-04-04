{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

#age = 3
#age = 8
#age = 15

#if age < 4:
#	print("Admission is free!")
#elif age < 12:
#	print("Admission cost is $5.")
#else:
#	print("Admission cost is $10.")

# Setting price inside if-elif-else statement
age = 8

if age < 4:
	price = 0
elif age < 10:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")

