# 使用ORM-sqlalchemy实现
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import numpy as np

import mysql.connector

Base = declarative_base()


class User2(Base):
    __tablename__ = "user2"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship("Book")

    # 定义输出字符串格式
    def __str__(self):
        return 'user2: id = %s,name = %s' % (self.id, self.name)

    __repr__ = __str__


class Book(Base):
    __tablename__ = "book"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 外键
    user_id = Column(String(20), ForeignKey("user2.id"))

    # 定义输出字符串格式
    def __str__(self):
        return 'book: id = %s,name = %s,user_id = %s' % (self.id, self.name, self.user_id)

    __repr__ = __str__


def get_DBSession():
    engine = create_engine('mysql+mysqlconnector://root:2014112217@localhost:3306/test_python')
    DBSession = sessionmaker(bind=engine)
    return DBSession


def destory_tables(conn):
    cursor = conn.cursor()
    cursor.execute("drop table if exists book  ")
    cursor.execute("drop table if exists user2  ")
    conn.commit()
    cursor.close()


def get_database_conn():
    return mysql.connector.connect(user="root", password="2014112217", database="test_python")


def create_user2_table(conn):
    cursor = conn.cursor()
    cursor.execute("create table if not exists  user2(id varchar(20) primary key ,name varchar(20))")
    conn.commit()
    cursor.close()
    # cursor = conn.cursor()
    # insert_data_user2(cursor)
    # cursor.close()


def query_user2(cursor):
    cursor.execute("select * from user")
    print(cursor.fetchall())


def insert_data_user2(cursor):
    line = "insert into user2 values (%,%)"
    for count in range(1, 5):
        cursor.execute(line, (count, "xue" + str(count)))


def add_user(session):
    for count in range(1, 5):
        new_user = User2(id=str(count), name="student" + str(count))
        session.add(new_user)
    session.commit()
    session.close()


def create_book_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        "create table if not exists book(id varchar(20) primary key,name varchar(20),user_id varchar(20), foreign key (user_id) references user2(id))")
    conn.commit()
    cursor.close()


def add_book(session):
    for count in range(1, 10):
        new_book = Book(id=str(count), name="book" + str(count), user_id=str(int(np.random.uniform(1, 5))))
        session.add(new_book)
    session.commit()
    session.close()


if __name__ == "__main__":
    conn = get_database_conn()
    # destory_tables(conn)
    # create_user2_table(conn)
    # create_book_table(conn)

    DBSession = get_DBSession()
    session = DBSession()
    # add_user(session)
    # add_book(session)
    # book_1 = session.query(Book).filter(Book.id == "1").one()
    # session.delete(book_1)
    # session.commit()
    book_2 = session.query(Book).filter(Book.id == "2").one()
    book_2.name = "世界地图"
    session.commit()

    print("所有记录：")
    print(session.query(User2).all())
    print(session.query(Book).all())
    print("user_id == 2 的所有书：")
    print(session.query(Book).filter(Book.user_id == "2").all())
    session.close()
    conn.close()
