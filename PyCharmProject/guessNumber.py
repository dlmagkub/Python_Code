import random
num = random.randint(1, 10)
num_1 = int(input("guess number"))
if num_1 == num:
    print("right! congratulation!")
elif num_1 > num:
    print("the answer is smaller")
else:
    print("the answer is bigger")
num_1 = int(input("try again(2/3)"))      # second chance
if num_1 == num:
    print("right! congratulation!")
elif num_1 > num:
    print("the answer is smaller")
else:
    print("the answer is bigger")
num_1 = int(input("try again(3/3)"))      # third chance
if num_1 == num:
    print("right! congratulation!")
elif num_1 > num:
    print("the answer is smaller")
else:
    print("the answer is bigger")
num_1 = int(input("try again(4/3)"))      # final chance
if num_1 == num:
    print("right! congratulation!")
else:
    print("game over,the answer is :", num)
