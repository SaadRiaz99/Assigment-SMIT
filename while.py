while True:
    battery = int(input("Enter initial battery level (1-100): "))
    if 1 <= battery <= 100:
        print(f"Battery level set to {battery}%\n")
        break
    else:
        print("Invalid input! Enter a number between 1 and 100.")

target_Charged = 90

while True:
    charged_per_circle = int(input("Enter charge per cycle (1-100): "))
    if 1 <= charged_per_circle <= 100:
        print(f"Valid charge per cycle: {charged_per_circle}%\n")
        break
    else:
        print("Invalid number! Try again.")

print("Charging System Started\n")

while battery < target_Charged:
    print(f"Battery Level: {battery}%")
    battery += charged_per_circle
    if battery >= 100:
        battery = 100
        print(f"Battery fully charged at 100%")
        break

print(f"\nCharging Stopped at {battery}%")

if battery >= target_Charged and battery < 100:
    print("Exit Reason: Target charge level reached.")
elif battery >= 100:
    print("Exit Reason: Safety condition triggered (battery full).")
else:
    print("Exit Reason: Unknown condition.")