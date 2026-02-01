print("=========break Statement=====")
print("=========login =====")

passw  = "SIRTalalSMIT".lower()


print(f"Password is :{passw}")
print("Password is --------------")
for atempt in range(0 ,3):
    inp_user  = input(f"atempt: {atempt}--Enter Password:")

    if inp_user == passw.lower():
        print("Access Granted ")
        break
    else:
        print(f"Wrong Password {inp_user}")
else:
    print(f"{atempt} cross locked Your Atempt")
