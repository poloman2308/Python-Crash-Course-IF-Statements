{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

#alien_color = 'green'
#alien_color = 'red'
alien_color = 'yellow'

if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 points!")

