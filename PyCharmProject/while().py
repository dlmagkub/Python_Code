# import random
# num = random.randint(1, 10)
num = 6
num_1 = int(input("guess number"))
i = 1
while i < 3:
    if num_1 == num:
        print("right! congratulation!")
    elif num_1 > num:
        print("the answer is smaller")
    else:
        print("the answer is bigger")
    num_1 = int(input("try again (%d/3)  " % i))
    i += 1
if num_1 == num:
    print("right! congratulation!")
print("the answer is %d" % num)
