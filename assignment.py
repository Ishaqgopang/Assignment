num_list: list =[]
user_name: str = input("What is your name :")
for x in range(1,4):
    num: int = int(input(f"Write your {x} favorite number :"))
    num_list.append(num)
print(f"\nHello, {user_name} let,s explore your favorite number :")
for item in num_list:
    if item % 2 == 0:
        print (f"{item} is even number")
    else:
        print (f"{num} is idd number")
for item in num_list:
    print (f"The number {item} and it,s square :({item} , {item ** 2})")
sum_of_num : int = sum(num_list)
print(sum_of_num)
print(f" Amazing! the sum of your favorite number is {sum_of_num}")
is_prinme = True
if sum_of_num <= 1:
    is_prinme = False
for x in range (2, sum_of_num):
    if sum_of_num  % x == 0:
        is_prinme = False
if is_prinme:
    print(f"wow! the number {sum_of_num} is a prime number!")
else:
    print(f" Great job! the number {sum_of_num} is not a prime number.")