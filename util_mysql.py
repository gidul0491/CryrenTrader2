from sqlalchemy import create_engine, Column, Integer, String, Numeric, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, insert
from sqlalchemy.ext.declarative import declarative_base
import json
with open("config.json","r") as conf:
    c = json.load(conf)["mySql"]

# SQLAlchemy 엔진 생성
url = f"mysql+pymysql://{c['user']}:{c['passwd']}@{c['host']}:{c['port']}/{c['db']}?charset=utf8mb4"
engine = create_engine(url, 
                       echo=True,pool_size=5, max_overflow=5) 

# 테이블이 객체를 생성할 때 사용
meta = MetaData() 
meta.bind = engine

# SQLAlchemy 세션 생성
Session = sessionmaker(autocommit=False,  autoflush=False, bind=engine)

# 세션 연결 함수
def openSession():
    return Session()

# 세션 연결 종료 함수
def closeSession(session):
    session.close()

# 테이블 객체 생성
cs = Table("candlestick",meta, autoload_with=engine)

# 기본 선언
Base = declarative_base()

# a fucntion to insert caldleStick
def insCS(session, symb, ticS, t, openP, closeP, highP, lowP, volumeC, volumeM, mpVolumeC, mpVolumeM):
  try:
    stmt = insert(cs).values(
        symbol = symb,
        ticSec = ticS,
        time = t,
        openPrice = openP,
        closePrice = closeP,
        highPrice = highP,
        lowPrice = lowP,
        volumeCoin = volumeC,
        volumeMoney = volumeM,
        mpVolumeCoin = mpVolumeC,
        mpVolumeMoney = mpVolumeM
    )
    session.execute(stmt)
    session.commit()
  except Exception as e:
    print(e)
