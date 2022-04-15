from prime_check import is_relatively_prime

# Generates a public key with inputs as n and phi
# Uses the is_relatively_prime function from part a to check if randomly chosen
# integer e is relatively prime with phi


def generate_public_key(n, phi):
    public_keys = 0, 0
    for i in range(2, phi):
        if is_relatively_prime(i, phi):
            e = i
            public_keys = e, n
            break
    return public_keys
