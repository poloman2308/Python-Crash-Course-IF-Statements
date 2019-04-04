{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

requested_toppings = ['pepperoni', 'canadian bacon']

print("What kind of toppings would you like on your pizza?")

if 'pepperoni' in requested_toppings:
	print("- " + "Adding pepperoni")
if 'mushrooms' in requested_toppings:
	print("- " + "Adding mushrooms")
if 'canadian bacon' in requested_toppings:
	print("- " + "Adding canadian bacon")

print("\nYour pizza will be ready in 20 minutes.")

