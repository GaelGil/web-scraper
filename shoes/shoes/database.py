# import sqlite3

# conn = sqlite3.connect('myshoes.db')
# curr = conn.cursor()

# # curr.execute("""create table shoes_table (
# #                 name text,
# #                 price text
# #                 )""")

# curr.execute("insert into shoes_table values ('oneshoe', 'oneprice')")

# curr.execute(SELECT SUBSTR(s,1,instr(cmd,' ')-1) FROM log2conn.commit())
# conn.close()

# from sqlalchemy import create_engine
# from sqlalchemy import String, Column, Inetger
# from sqlalchemy.exet.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///test_db.db')
# session = sessionmaker(bind=engine)()

# Base = declarative_base()

# class ShoesPipeline(object, Base):
#     __tablename__ = "Sneakers"
#     shoe_name = Column(Sring, primary_key=True)
#     shoe_price = Column(Inetger)

#     def __init__(self, shoe_name, shoe_price):
#         self.shoe_name = shoe_name
#         self.shoe_price = shoe_price
#     def add_to_db(self):
#         session.add(object)
#         session.commit()

#     def store_db(self, item):
#         self.curr.execute("""insert into shoes_table values (?, ?)""",(
#             item['shoe'][0],
#             item['price'][0]
#         ))
#         self.conn.commit()