import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:root@localhost/testdb',echo=True)

meta_data = sqlalchemy.MetaData()
person = sqlalchemy.Table(
    'person',meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(128),unique=True,nullable=False),
    sqlalchemy.Column('birthday', sqlalchemy.Date,nullable=False),
)

meta_data.create_all(engine)

#增加一个记录
# person_insert =  person.insert()
# print(person_insert)
# insert_qs = person_insert.values(name = '乔松',birthday = '2008.01.01')
#
# with engine.connect() as  conn:
#     result = conn.execute(insert_qs)
#     print(result.inserted_primary_key)
#     conn.commit()

#插入多条记录
person_insert = person.insert()
with engine.connect() as  conn:
    conn.execute(person_insert,[
                     {"name":"Jay","birthday":"2003.1.1"},
    {"name": "Jam", "birthday": "2003.1.11"},
    {"name": "Jim", "birthday": "2003.10.1"}

    ])
    conn.commit()
