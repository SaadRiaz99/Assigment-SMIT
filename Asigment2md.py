para = "My Name is Saad Bin Riaz"

split_res = para.split(" ")
print(split_res)

join_res = "-".join(split_res)
print(join_res)

replace_res = para.replace("Saad", "Umar")
print(replace_res)

find_res = para.find("Bin")
print(find_res)

count_res = para.count("a")
print(count_res)

# Q6

name = "Saad"
age = 19
language = "Python"

print("My Name is %s and I am %d years old" % (name, age))
print("I use %s and my Name is %s" % (language, name))

print("My Name is {} and I love {}".format(name, language))
print("I love {1} and my Name is {0}".format(name, language))

print(f"My Name is {name}, I am {age} years old, and I use {language}")
# Q7
a = "Saad"
b = "Saad"
print(a == b)

c = "Saad"
d = "Saad"
print(c == d)

print("Apple" < "Banana")

print("a" > "A")

print(c.lower() == d.lower())

# Q8


multi = "*"
print(multi * 10)


name = "Saad"
print(name * 3)


print(name * 0)


print("-" * 30)
print("WELCOME TO PYTHON")
print("-" * 30)


print("#" * 5)
print("#" * 5)
print("#" * 5)


for i in range(1, 6):
    print("*" * i)
