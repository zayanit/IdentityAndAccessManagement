import hashlib 

with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')

hashed_bad_passwords = {}

for bad_password in nist_bad:
    hashed_password = hashlib.md5(bad_password.encode()).hexdigest()
    hashed_bad_passwords[hashed_password] = bad_password
