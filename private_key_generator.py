# Generates private keys using e, n, and phi

# def generate_private_key(e, n, phi):
#     priv_keys = 0, 0
#     for m in range(n):
#         d = (1 + m * phi)/e
#         if d % 1 == 0:  # cheks if d is an integer
#             priv_keys = (int(d), n)
#             break
#     return priv_keys

def generate_private_key(e, n, phi):
    priv_key_1 = pow(e, -1, phi)
    return priv_key_1, n


# Add Euclidian Algorithm to make it more efficient

# print(generate_private_key(5,323,288))
