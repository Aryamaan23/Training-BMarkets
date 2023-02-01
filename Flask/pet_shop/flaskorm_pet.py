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