# truth table
print("===========Truth Table============")
print("Type True or False \n")
a = input("Enter True or False : ").strip().lower() == "true"
b = input("Enter True or False : ").strip().lower() == "true"
c = input("Enter True or False : ").strip().lower() == "true"

print("========INPUT CONDITIONS========")
print("A -->", a)
print("B -->", b)
print("C -->", c)

print("=== BASIC LOGIC RESULTS ===")
print("A AND B =", a and b)
print("A OR B =", a or b)
print("NOT A =", not a)

print("B AND C =", b and c)
print("B OR C =", b or c)
print("NOT C =", not c)


print("==== COMPLEX COMBINATIONS =====")
print("A AND B AND C =", a and b and c)
print("A OR B OR C =", a or b or c)
print("(A AND B) OR C =", (a and b) or c)
print("A AND (B OR C) =", a and (b or c))
print("NOT (A AND B) =", not (a and b))
print("NOT (A OR C) =", not (a or c))


# Q2

print("Grade System")

A_PLUS = 85
A = 70
B = 60
C = 50
D = 40



def grade(per):
    if per >= A_PLUS:
        return  "A_PLUS"
    elif  per >= A:
        return "A"     
    elif  per >= B:
        return "B"     
    elif  per >= C:
        return "C"     
    elif  per >= D:
        return "D"     
    else:
        return "Fail"    
per  = float(input("Enter The Percent :"))
Grade = grade(per)        
print("Grade" , Grade )