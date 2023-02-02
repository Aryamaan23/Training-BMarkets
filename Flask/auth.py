from flask_bcrypt import Bcrypt
bcrypt = Bcrypt() #create a hash function to crypt the password
hashed_pass = bcrypt.generate_password_hash('mypassword')
print(hashed_pass)
check1 = bcrypt.check_password_hash(hashed_pass,"mypass")
print(check1)
check2 = bcrypt.check_password_hash(hashed_pass,"mypassword")
print(check2)