print("=== Let's Check Your Health Status ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
health = input("Are you healthy? (yes or no): ").lower()
membership = input("Do you have a health membership? (yes or no): ").lower()
print("\nCheck Health Status")
runing = int(input("How many kilometers can you run without stopping: "))
pushups = int(input("How many push-ups can you do in a row: "))


if runing >= 1 and pushups >= 10:
    healthy = "yes"
    print("You are healthy based on your activity level.")
else:
    healthy = "no"
    print("Your activity level suggests you may have some health restrictions.")
print("Check Age Elgibilty")    
if age >= 18 and membership == "yes" and health == "no":
    print("Congratulations, you meet the age eligibility requirements.")

    height = int(input("Enter your height in cm: "))
    if height >= 150:
        print("Your height meets the requirement.")

        vip_member = input("Do you have a VIP pass? (yes or no): ").lower()
        if vip_member == "yes":
            print("VIP access granted. You can enjoy all rides.")
        else:
            print("Standard access granted. You can enjoy regular rides.")
    else:
        print("Height requirement not met. Only limited access is allowed.")

else:
    print(f"Sorry {name}, you are not eligible for entry.")
    if age < 18:
        print("Reason: You must be at least 18 years old.")
    elif membership != "yes":
        print("Reason: A health membership is required.")
    elif health == "yes":
        print("Reason: Your health condition does not allow participation.")

    else:
        print("Invalid Entry")