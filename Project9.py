age=int(input("Enter your age: "))
if age<=20 and age>=10:
    print("You are eligable")
else:
    age2=int(input("Enter again we might have mistaken you: "))

    if age<=20 and age>=10:
        print("You are eligable")
    else:
        print("Your not eligable")