from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FeiraLivre(Base):
    __tablename__ = 'FEIRA_LIVRE'

    id = Column('ID', Integer, primary_key=True)
    longitude = Column('LONGITUDE', Integer, nullable=False)
    latitude = Column('LATITUDE', Integer, nullable=False)
    setcens = Column('SETCENS', Integer, nullable=False)
    areap = Column('AREAP', Integer, nullable=False)
    codDist = Column('CODDIST', Integer, nullable=False)
    distrito = Column('DISTRITO', String(50), nullable=False)
    codSubPref = Column('CODSUBPREF', Integer, nullable=False)
    subPrefe = Column('SUBPREFE', String(50), nullable=False)
    regiao5 = Column('REGIAO5', String(10), nullable=False)
    regiao8 = Column('REGIAO8', String(10), nullable=False)
    nomeFeira = Column('NOME_FEIRA', String(50), nullable=False)
    registro = Column('REGISTRO', String(6), nullable=False)
    logradouro = Column('LOGRADOURO', String(255), nullable=False)
    numero = Column('NUMERO', String(50), nullable=True)
    bairro = Column('BAIRRO', String(50), nullable=False)
    referencia = Column('REFERENCIA', String(255), nullable=True)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)