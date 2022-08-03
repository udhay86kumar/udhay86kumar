def prime_serius(number):
    for iter in range(2,number):
        if is_prime(iter)== True:
            print(iter,end=" ")
        else:
            pass
number=int(input("Enter the input range: "))
is_prime=lambda numer: all(numer%i != 0 for i in range(2,int(number**.5)+1))
prime_serius(number)
