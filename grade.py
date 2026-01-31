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