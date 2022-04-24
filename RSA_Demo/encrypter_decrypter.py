# Modular exponentiation will be the basis of the encryption method
# Uses an iterative approach to calculate the output
# This function is then implemented in encryption and decryption functions
# respectively.
# Encryption and decryption functions will use the private and public keys
# generated earlier.

def exponent_calc(base, power, mod):
    output = 1
    for i in range(1, power+1):
        output = (output * base) % mod
    return output


def encrypt(x, e, n):
    y = exponent_calc(x, e, n)
    return y


def decrypt(y, d, n):
    x = exponent_calc(y, d, n)
    return x

# x1 = encrypt(4560, 7, 10403)
# print(x1)
#
# y1 = decrypt(200, 8743, 10403)
# print(y1)
#