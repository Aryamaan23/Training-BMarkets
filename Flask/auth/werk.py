from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash("mypassword")
print(hashed_pass)
chk = check_password_hash(hashed_pass, "mypassword")
print(chk)