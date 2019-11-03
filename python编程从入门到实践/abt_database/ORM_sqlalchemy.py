# ORM（Object-Relational Mapping）框架；在Python中，最有名的ORM框架是SQLAlchemy

from sqlalchemy import Column, String, create_engine, ForeignKey, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User类
class User(Base):
    # 表的名字
    __tablename__ = "user"
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    #email = Column(String(40), unique=True)
    #score = Column(Integer())


# create_engine初始化数据库连接: '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:2014112217@localhost:3306/test_python')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()  # DBSession对象可视为当前数据库连接。
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库:
session.commit()
session.close()

session = DBSession()
# 有了ORM，查询出来的可以不再是tuple，而是User对象
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == "5").one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
session.close()

'''
#删除用户
u=session.query(User).filter(User.id=='2').one()
session.delete(u)
session.commit()
#修改数据：获取一条数据对象，修改属性并提交即可
user=session.query(User).filter(User.id=='2').one()
user.score=99
session.commit()
'''


# 使用ORM实现 一对多以及多对多关系
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# 例如，如果一个User2拥有多个Book，就可以定义一对多关系如下：
class User2(Base):
    __tablename__ = "user2"

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = "Book"

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey("user2.id"))
