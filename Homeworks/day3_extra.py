#Day 3- Extra

login={"username":"Bugce", "password":"1234"}
username1 =input("Please enter your user name: ")

password1= input("Please enter your password: ")

if (username1 == login["username"] and password1 == login["password"]):
    print("You are now logged in! ")
elif (username1 == login["username"] and password1 != login["password"]):
    print("Invalid password")
elif (username1 != login["username"] and password1 == login["password"]):
    print("Invalid username")
else :
    print("Invalid password and username" )