{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

usernames = ['derek', 'daniel', 'roger', 'kobe', 'michael', 'admin']

for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a user report?")
	else:
		print("Hello " + username.title() + ", thank you for logging in again.")

