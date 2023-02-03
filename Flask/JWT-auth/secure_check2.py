from umodel import User_db
#users=[User(1,'Kapil','pass'),User(2,'Abhay','pass')]
#username_table={u.username : u for u in users}
#print(username_table)
#userid_table={u.id : u for u in users}
#print(userid_table)

def authenticate(username,password):
    user=User_db.query.filter_by(username=username).first()
    print(user)
    if user and password==user.password:
        return user

def identity(payload):
    user_id=payload['identity']
    return User_db.query.filter_by(id=user_id).first().id


authenticate('Kapil','pass')