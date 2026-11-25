
from sqlalchemy.sql import and_,or_
from db_init import engine,person

# 提取查询
# with engine.connect() as conn:
#     query = person.select()
#     result_set = conn.execute(query)


    #方法1:for循环
    # for row in result_set:
    #     print(row[0])
    #     print(row.name)

    #方法2:fetchall()
    # result = result_set.fetchall()
    # print(result)

    #方法3:fetchone()
    # result = result_set.fetchone()
    # print(result)

#条件查询
with engine.connect() as conn:
    # query = person.select().where(person.c.birthday > '2004.01.01')

    #复杂条件查询
    query = person.select().where(
        #要么是Jay，要么是2003年1月1日之前出生的，且id小于4
        or_(
            person.c.name == 'Jay',
            and_(
                person.c.birthday > '2003.01.01',
                person.c.id < 4
            )
        )
    )



    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)


