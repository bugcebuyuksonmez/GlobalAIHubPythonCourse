
#Day 3- User Login Application

username = "Bugce"
password ="1234"
username1 =input("Please enter your user name: ")
password1= input("Please enter your password: ")

if (username != username1 and password == password1):
    print("Invalid Username")
elif (username==username1 and password != password1):
    print("Invalid Password")
elif (username != username1 and password!= password1):
    print("Invalid Username and Password")
else:
    print("You are now logged in. ")