from sqlalchemy1 import db
a = db.session.query(ma_co_phieus)
for i in a.query.all():
    print(i.name)
    print(i.code)