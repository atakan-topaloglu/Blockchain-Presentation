# Following functions are used to determine if a number is prime or
# If two numbers are relatively prime


def is_prime(number):
    prime = True
    for i in range(2, number//2+1):
        if number % i == 0:
            prime = False
    return prime


def is_relatively_prime(first, second):
    rel_prime = True
    min_x = min(first, second)
    for i in range(2, min_x + 1):
        if first % i == 0 and second % i == 0:
            rel_prime = False
    return rel_prime 

# y1 = is_prime(5)
# print(y1) 

# r1 = is_relatively_prime(1501, 1513) 
# print(r1)
