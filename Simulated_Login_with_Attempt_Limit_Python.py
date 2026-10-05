username = "Admin"
password = "1234"
temp = 1
login = False

while temp <= 3 and not login :
	username_ = input("Please enter the username : ")
	password_ = input("Please enter the password : ")

	if username_ == username and password_ == password :
		print("Login successful.")
		login = True
	else :
		print(f"Login failed. Attempts left : {3-temp}")
		temp += 1

if not login :
	print("Too many failed attempts. Account locked.")