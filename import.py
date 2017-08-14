import logging.config
import csv
from models import FeiraLivre
from db import session

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

with open('DEINFO_AB_FEIRASLIVRES_2014.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rowFind = feira = session.query(FeiraLivre).filter(FeiraLivre.id == row['ID']).first()

        if rowFind is not None:
            log.info('%s already imported ' % (row['ID']))
        else:
            if not row['NUMERO'] or row['NUMERO'] == 'S/N':
                row['NUMERO'] = None;

            if not row['REFERENCIA'] or row['REFERENCIA'] == '':
                row['REFERENCIA'] = None;

            feira = FeiraLivre(
                id=row['ID'],
                longitude=row['LONG'],
                latitude=row['LAT'],
                setcens=row['SETCENS'],
                areap=row['AREAP'],
                codDist=row['CODDIST'],
                distrito=row['DISTRITO'],
                codSubPref=row['CODSUBPREF'],
                subPrefe=row['SUBPREFE'],
                regiao5=row['REGIAO5'],
                regiao8=row['REGIAO8'],
                nomeFeira=row['NOME_FEIRA'],
                registro=row['REGISTRO'],
                logradouro=row['LOGRADOURO'],
                numero=row['NUMERO'],
                bairro=row['BAIRRO'],
                referencia=row['REFERENCIA'])

            session.add(feira)
            session.commit()

            log.info('%s imported ' % (row['ID']))