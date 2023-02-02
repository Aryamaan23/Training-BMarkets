"""
from flaskorm import Pet,db
#Create table
db.create_all()
sid=Pet('Siberian Cat','Dolly','Kapil',5)
hm=Pet('Himalayan','Molly','Rahul',3)
rs=Pet('Russian','Jelly','Rohan',4)
db.session.add_all([sid,hm,rs])
db.session.commit()
print(sid)
print(sid.pet_id)
print(hm)
print(hm.pet_id)
print(rs)
print(rs.pet_id)
"""

from flaskorm import db,Pet,Toy,Owner

db.create_all()
dog1 = Pet('Jimmy')
dog2 = Pet('Leo')

db.session.add_all([dog1,dog2])
db.session.commit()
print(Pet.query.all())
print(dog1.id,dog1.name)

owner1 = Owner('Kapil',dog1.id)

toy1 =  Toy("chew Toy", dog1.id)
toy2 =  Toy('Ball', dog1.id)

db.session.add_all([owner1,toy1,toy2])
db.session.commit()
dog1.represent_toys()