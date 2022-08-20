command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Caris alredy started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car is alredy stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else: print("sorry, I don't understand that!")
