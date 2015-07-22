from __future__ import print_function, division

import savReaderWriter as s
import pandas as pd
import numpy as np

NROWS = 0

def read_sav(filename, columns, nrows=0):

    reader = s.SavReader(filename, rawMode=True)
    header = reader.getHeader(None)

    indices = [header.index(col) for col in columns]

    data = []
    for i, line in enumerate(reader):
        if line[0] < 1996.0:
            continue

        values = [line[index] for index in indices]
        data.append(values)
        if i == nrows-1:
            break

    df = pd.DataFrame(data=data, columns=columns)

    na = -1.7976931348623157e+308
    df.replace(na, np.nan, inplace=True)
    df.index = df.SUBJID
    return df


def read_dem_sav():
    #store = pd.HDFStore('dem.h5')

    filename = '1 DEMOGRAPHICS.SAV'
    columns = ['YEAR', 'SUBJID', 'SEX', 'AGE1', 'AGE2', 'RRACE', 
                'RACEGROUP', 'INCOME', 'FATHEDUC', 'MOTHEDUC', 
                'FIRSTGEN', 'FRELIGIONA', 'MRELIGIONA', 'SRELIGIONA']
    dem = read_sav(filename, columns, nrows=NROWS)
    #store['dem'] = dem
    #store.close()
    print(dem.tail())
    dem.to_pickle('dem.pkl')


def read_hs_sav():
    #store = pd.HDFStore('hs.h5')

    filename = '2 HIGH SCHOOL.SAV'
    columns = ['YEAR', 'SUBJID', 'HSGPA', 'SATV', 'SATM', 'SATW', 
               'ACTCOMP']

    for i in range(1, 34):
        if i in [7, 13, 16, 22]:
            continue
        columns.append('ACT%.2d' % i)

    columns.extend(['ACT17_T', 'ACT21_T', 'ACT23_T', 'ACT24_T', 'ACT26_T'])

    hs = read_sav(filename, columns, nrows=NROWS)
    #store['hs'] = hs
    #print(store)    
    #store.close()
    print(hs.tail())
    hs.to_pickle('hs.pkl')


def main():
    #read_dem_sav()
    read_hs_sav()


if __name__ == '__main__':
    main()

