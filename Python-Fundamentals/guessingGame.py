import random
randomNumber = random.randint(1, 100)
userNo = int(input("Geuss the number between 1-100: "))

cnt = 0
while userNo != randomNumber:
    if userNo < randomNumber:
        print("Guess higher number")
    else:
        print("Guess lower number")
    cnt += 1
    userNo = int(input("Enter again: "))

print(f"Congratulations!, you guessed the number in {cnt} attempts")