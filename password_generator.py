import bcrypt

salt = bcrypt.gensalt()

password_hash = bcrypt.hashpw(''.encode(), salt)
password_hash = str(password_hash)[2:-1]
print(password_hash)
