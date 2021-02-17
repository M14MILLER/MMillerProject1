import requests
import secrets
import json
import sqlite3
from typing import Tuple
#import random


def get_data():
    all_data = []
    for page in range(162):
        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?"
                                f"school.degrees_awarded.predominant=2,3&fields=school.name,school.city,"
                                f"2018.student.size,2017.student.size,"
                                f"2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,"
                                f"2016.repayment.3_yr_repayment.overall&api_key={secrets.api_key}&page={page}")
        if response.status_code != 200:
            print("error getting data")

        page_of_data = response.json()
        page_of_school_data = page_of_data['results']
        all_data.extend(page_of_school_data)
    return all_data

def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
        cursor = db_connection.cursor()#get ready to read/write data
        return db_connection, cursor

def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()

def setup_db(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS college_data(school.name TEXT NOT NULL,
    school.city TEXT NOT NULL, 
    The2018.student.size INTEGER DEFAULT 0,
    The2017.student.size INTEGER DEFAULT 0,
    The2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line REAL DEFAULT 0,
    The2016.repayment.3_yr_repayment.overall REAL DEFAULT 0,
    );''')

def add_college(cursor: sqlite3.Cursor, name, city, T2018size, T2017size, T2017earn, T2016repay):
    cursor.execute(f'''INSERT INTO COLLEGES (The2018_student_size, The2017_student_size, The2017_earn, The2016_repay)
    VALUES({name}, {city}, {T2018size}, {T2017size}, {T2017earn}, {T2016repay}''')

def main():
    conn, cursor = open_db("college_db.sqlite")
    setup_db(cursor)
    college_data = get_data()
    with open('school_data.txt', 'w') as outfile:
        json.dump(college_data, outfile)
    print(college_data)
    close_db(conn)



if __name__ == '__main__':
    main()
