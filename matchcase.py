print("=== lets Enjoy ===")
print("Available commands: greet, calculate, joke, info, exit")


while True:
    comm = input("Enter Your Command According to Your Mood :").lower()

    match comm:
        case "greet":
            name = str(input("Enter Your name:"))
            print(f"Sallam {name} have A good Day ")
        case "calculate":
            try:
                expr = input("Enter a math expression (Example: (2 + 3 * 4)): ")
                result = eval(expr)
                rint(f"The result is: {result}")
            except Exception as e:
                print("Invalid expression. Please try again.")
        case "joke":
            print(""" Bari behn padha rahi thi aur bhai bilkul nahi samajh raha tha.
                     Behn boli: Agar 2 + 2 karoge, kitna hoga?
                    Bhai bola: 5!
                    Behn phir example diya: “Theek hai, maan lo tumhare paas 2 roti hain, aur tumne ek kha li, to piche kitna bacha?”
                    Bhai bola: “Salan!”
                    Phir behn gusse me: "Ab bas, samajh gaya!" aur bhai ko maar diya""")  
        case "info":
            print("This is a smart command router. You can try these commands:")
            print("---->: greet: Get a personalized greeting")
            print("---->: calculate: Evaluate a math expression")
            print("---->: joke: Hear a joke")
            print("---->: info: Show this menu")
            print("---->: exit: Quit the program")

        case "exit":
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid command! Please type one of: greet, calculate, joke, info, exit")      


