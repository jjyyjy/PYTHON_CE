a = int(input("정수를 입력하세요! : "))

for i in range(1, a+1):
    for j in range(i):
        print("*", end="")
    print()