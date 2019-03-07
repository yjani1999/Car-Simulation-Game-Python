print("***** The Car simulation game ***** ")
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
            print("Car Started ready to go!!")
    elif command == "stop":
            print("Car Stopped.")
    elif command == "help":
            print(""" Start - to start the car
 Stop - to stop the car
 Quit - to exit""")
    elif command == "quit":
            break
    else:
            print("Sorry I don't understand that")
print("***** Developed by Yash Jani ***** ")