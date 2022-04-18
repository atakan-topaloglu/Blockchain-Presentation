# Generates private keys using e, n, and phi

def generate_private_key(e, n, phi):
    priv_key = pow(e, -1, phi)
    return priv_key, n

# print(generate_private_key(5,323,288))
