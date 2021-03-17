from app import db, User

def create_User(name, passw):
    u = User(name, passw)
    db.session.add(u)
    db.session.commit()
    print(f"Added {u}!")