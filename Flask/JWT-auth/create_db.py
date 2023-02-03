from umodel import User_db
from umodel import db



db.create_all()

user1 = User_db('Akshit','pass')
user2 = User_db('Aryamaan1', 'pssass')
#db.session.add_all([user1,user2])
db.session.add_all([user1,user2])
db.session.commit()
print(user1.username)
print(user2.username)

