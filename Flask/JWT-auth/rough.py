from umodel import User_db

print(User_db.query.filter_by(username="Aryamaan1").first().username)