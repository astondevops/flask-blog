from models import User, db

user = User.create("charlie@gmail.com", password="secret", name="Charlie")

#print(user.password_hash)
#db.session.add(user)
#db.session.commit()
print(User.authenticate("charlie@gmail.com", "secret"))
print(User.authenticate("charlie@gmail.com", "test"))

