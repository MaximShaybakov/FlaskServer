from sqlalchemy import Column, String, Integer, DateTime, Text, \
    create_engine, func
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


DSN = 'postgresql://app:1234@127.0.0.1:5431/netology'

engine = create_engine(DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    creation_time = Column(DateTime, server_default=func.now())
    password = Column(String(100), nullable=False)
    email = Column(String(30), nullable=True)
    advertisements = relationship('Ads', back_populates="owner")

    def __repr__(self):
        return f'User "{self.name}"'


class Ads(Base):

    __tablename__ = 'advertisements'

    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates="advertisements")

    def __repr__(self):
        return f'Ads "{self.title[:20]}"'
