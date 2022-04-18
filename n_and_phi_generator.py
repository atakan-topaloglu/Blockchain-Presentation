from prime_check import is_prime

# Calculates the product of two primes and their totient
# Performs a validity check on primes using is_prime function.


def calculate_n_and_phi():

    first_prime = int(input('First prime number: '))
    
    isprime1 = is_prime(first_prime)
    while first_prime < 2 or not isprime1:
        first_prime = int(input('Invalid prime, enter again: '))
        isprime1 = is_prime(first_prime)

    second_prime = int(input('Second prime number: '))
 
    isprime2 = is_prime(second_prime)
    while second_prime < 2 or not isprime2:
        second_prime = int(input('Invalid prime, enter again: '))
        isprime2 = is_prime(second_prime)

    n = first_prime * second_prime
    phi = (first_prime-1) * (second_prime-1)
    return n, phi


# n1, phi1 = calculate_n_and_phi()
# print(n1, phi1)
