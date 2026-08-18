str = input("Enter a sentence: ")
l1 = list(str.split(" "))
print(l1)

for i in l1:
    print(i.capitalize(), end=" ")