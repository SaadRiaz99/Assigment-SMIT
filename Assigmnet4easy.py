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


