from sqlalchemy1 import ma_co_phieus
for i in db.ma_co_phieus.query.all():
    print(i.name)
    print(i.code)