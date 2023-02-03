from user import User
users=[User(1,'Kapil','pass'),User(2,'Abhay','pass')]
username_table={u.username : u for u in users}
print(username_table)
userid_table={u.id : u for u in users}
print(userid_table)

def authenticate(username,password):
    user=username_table.get(username,None)
    print(user)
    if user and password==user.password:
        return user

def identity(payload):
    user_id=payload['identity']
    print(user_id)
    return userid_table.get(user_id,None)


authenticate('Kapil','pass')
