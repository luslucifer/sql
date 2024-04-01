from models.extracting_data import FilterInfo
from models.unziping_info import UnzipingInfo
import sqlite3
import requests
from multiprocessing import Pool

url = 'http://dl.opensubtitles.org/en/download/sub/'

dict_keys = ('IMDBLink', 'IMDBScore', 'SubtitleLink', 'SubtitleDownload', 'SubtitleFilename', 'SubtitleDownloads', 'SubtitleLanguage', 'SubtitleFormat', 'SubtitleTotal', 'SubtitleUploaded', 'SubtitleNFOCreated', 'SubtitleReleaseName', 'SubtitleFPS', 'CDFilename', 'CDSize', 'CDMD5')

class Main:
    def insert_data_to_database(self, data_list):
        conn = sqlite3.connect('lucifer.sqlite3')
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SubtitleData (
                IMDBLink TEXT,
                IMDBScore REAL,
                SubtitleLink TEXT,
                SubtitleDownload TEXT,
                SubtitleFilename TEXT,
                SubtitleDownloads INTEGER,
                SubtitleLanguage TEXT,
                SubtitleFormat TEXT,
                SubtitleTotal INTEGER,
                SubtitleUploaded TEXT,
                SubtitleNFOCreated TEXT,
                SubtitleReleaseName TEXT,
                SubtitleFPS REAL,
                CDFilename TEXT,
                CDSize INTEGER,
                CDMD5 TEXT,
                IMDB_ID TEXT,
                OP_id TEXT
            )
        ''')

        # Insert data into the table
        cursor.executemany('''
            INSERT INTO SubtitleData (
                IMDBLink,
                IMDBScore,
                SubtitleLink,
                SubtitleDownload,
                SubtitleFilename,
                SubtitleDownloads,
                SubtitleLanguage,
                SubtitleFormat,
                SubtitleTotal,
                SubtitleUploaded,
                SubtitleNFOCreated,
                SubtitleReleaseName,
                SubtitleFPS,
                CDFilename,
                CDSize,
                CDMD5,
                IMDB_ID,
                OP_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data_list)

        conn.commit()
        conn.close()


    def making_dict(self, id:str) -> dict:
        try :
            res:bytes = requests.get(url+id).content
            f = FilterInfo()
            u = UnzipingInfo()
            unziped:str = u.unziping(res)
            extracted = f.main_extracting_data(unziped)
            try :
                splited = extracted['IMDBLink'].split('/')
                extracted['IMDB_ID'] = splited[len(splited)-2]
                extracted['OP_id'] = id
            except Exception as err : 
                print( f' err in scraping id: {id} :{err}')

            return(tuple(extracted.values()))
        except Exception as err : 
            print('err in making list dict :{err}')


    def main (self, id, l=None):  # Pass l as an argument
        try:
              # Initialize l if not provided
            values = self.making_dict(id=id)
            return(values)
        except Exception as err: 
            print(f'err was in main id:{id} and err is err:{err}')

if __name__ == '__main__':
    m = Main()
    l = []
    with open('ids.txt','r') as file:
        ids_arr = file.read().splitlines()
    
    
    try :
        with Pool(20) as p :
            l = p.map(m.main,ids_arr)  # Pass l to the main method
    except Exception as err : 
        print(f'err in pool : {err}')
    
    
    m.insert_data_to_database(l)
