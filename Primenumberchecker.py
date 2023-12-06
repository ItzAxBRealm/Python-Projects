def prime_checker(number):
    prime_num = True
    for i in range(2, number - 1):
        if number % i == 0:
            prime_num = False
    if prime_num == True:
        print(str(number) + " is a prime number.")
    else:
        print(str(number) + " is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)