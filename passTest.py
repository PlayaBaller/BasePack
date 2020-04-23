attempts_left = 3

while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter password "
                     "(you have {} attempts left): ".format(attempts_left + 1))
    if password == "hustla777":
        print("Access granted")
        break
else:
    print("Wrong password")


