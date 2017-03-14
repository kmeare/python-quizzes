def secret_of_life():
    num = int(input())
    if num == 42:
        return
    print(num)
    secret_of_life()
secret_of_life()

# num = 0
# while num != 42:
#     num = int(input("enter a number: "))
#     print(num)