import secrets, string

otp= f"{secrets.randbelow(1000000):06d}" # pad with leading zeros
print(f"Secure OTP: {otp}")

# 12-character session token
allowed_chars= string.ascii_letters + string.digits
token= ''.join(secrets.choice(allowed_chars) for _ in range(12))
print(f"Session Token: {token}")

# 8-bit random integer
rand_int= secrets.randbits(8)
print(f"8-bit integer: {rand_int}")
print(f"Binary representation: {bin(rand_int)}")

# Why not random.randint() for OTP/token?
# random is pseudo-random and predictable if someone knows the seed.
# secrets is designed for cryptography — unpredictable and secure.
# In login systems, predictability = vulnerability, so secrets is the right choice.