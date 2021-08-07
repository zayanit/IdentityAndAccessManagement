import hashlib 

with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')

hashed_bad_passwords = {}

for bad_password in nist_bad:
    hashed_password = hashlib.md5(bad_password.encode()).hexdigest()
    hashed_bad_passwords[hashed_password] = bad_password


# Imagine this information was stolen or leaked
leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    }, 
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    }, 
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    }, 
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}

# Use the Rainbow table to determine the plain text password
for user in leaked_users_table.keys():
    try:
        print(user + ":\t" + hashed_bad_passwords[leaked_users_table[user]['md5']])
    except KeyError:
        print(user + ":\t" + '******* hash not found in rainbow table')