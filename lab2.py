# ---------------->how to print string
text="i am Anwar";
print(text);

# ----------->>
def add(x, y):
    return x + y

# Call the function and print the result
result = add(2, 3)
print(result)

# ------------------>>>> how to check types of variables in python --------------->>>
x=5
y=6.7
print(type(x))
print(type(y))
z=True
print(type(z))

# ------------>>>>while loops to iterate over array --------->>>>>>
# while loop 
arr=["A","B","C"]
i=0
while(i<3):
    i=i+1
    print("hello here")

# ------->>>for in loop , iterating over an array --------->>>>>
arr2=["Anwar","subhan"]
for i in arr2:
    print(i)

# ------------------->> iteration over tuple ---------------->>>
tupple=("Anwar","subhan", "Mr ghulam mustafa")
for i in tupple:
    print(i)

# ------------------->> iteration over string ---------------->>>
strng="Anwar"
for i in strng:
    print(i)

# ---->>>>> iterating by index of sequences ------------>>
arr3=["Anwar","subhan","soban"]
for i in range(len(arr3)):
    print(arr3[i])

# ------------------->> continue , break >> ---------------->>>
for letter in "geekforgeeks":
    if letter == "e":
        continue
    print("current letter : ", letter)

# program that takes age and validate if you are above 18
age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible")
else:  
    print("you are not eligible")
