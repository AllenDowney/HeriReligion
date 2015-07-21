from __future__ import print_function, division

import savReaderWriter as s
import pandas as pd


def read_sav(filename, columns, nrows=1000):

    reader = s.SavReader(filename, rawMode=True)
    header = reader.getHeader(None)

    indices = [header.index(col) for col in columns]

    data = []
    for i, line in enumerate(reader):
        values = [line[index] for index in indices]
        data.append(values)
        if i == nrows-1:
            break

    df = pd.DataFrame(data=data, columns=columns)

    na = -1.7976931348623157e+308
    df.replace(na, np.nan, inplace=True)
    return df


def read_dem_sav():
    #store = pd.HDFStore('dem.h5')

    filename = '1 DEMOGRAPHICS.SAV'
    columns = ['YEAR', 'SUBJID', 'SEX', 'AGE1', 'AGE2', 'RRACE', 
                'RACEGROUP', 'INCOME', 'FATHEDUC', 'MOTHEDUC', 
                'FIRSTGEN', 'FRELIGIONA', 'MRELIGIONA', 'SRELIGIONA']
    dem = read_sav(filename, columns, nrows=10000000)
    #store['dem'] = dem
    #store.close()
    print(dem.tail())
    dem.to_pickle('dem.pkl')

def read_hs_sav():
    #store = pd.HDFStore('hs.h5')

    filename = '2 HIGH SCHOOL.SAV'
    columns = ['YEAR', 'SUBJID', 'HSGPA', 'SATV', 'SATM', 'SATW', 
               'ACTCOMP', 'ACT08', 'ACT09', 'ACT21', 'ACT25', 'ACT28', 
               'ACT29', 'ACT17_T', 'ACT21_T', 'ACT24_T']
    hs = read_sav(filename, columns, nrows=10000000)
    #store['hs'] = hs
    #print(store)    
    #store.close()
    print(hs.tail())
    hs.to_pickle('hs.pkl')


def main():
    read_dem_sav()
    read_hs_sav()


if __name__ == '__main__':
    main()

