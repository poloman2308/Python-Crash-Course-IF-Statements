{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

available_toppings = ['mushrooms', 'olives', 'green pepers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'extra cheese', 'onions']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nYour pizza will be ready in 30 minutes.")

