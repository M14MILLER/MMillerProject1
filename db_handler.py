import sqlite3
from typing import Tuple, Dict, List



def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def make_tables(cursor: sqlite3.Cursor, jobs_datashape: Dict):
    cursor.execute('''CREATE TABLE IF NOT EXISTS coll_data(
    school_id INTEGER PRIMARY KEY,
    school_name TEXT NOT NULL,
    student_size INTEGER,
    school_state TEXT,
    three_year_earnings_over_poverty INT,
    loan_repayment INT);''')
    columns = create_columns(jobs_datashape)
    create_statement = f"""CREATE TABLE IF NOT EXISTS job_info {columns}"""
    cursor.execute(create_statement)


def create_columns(jobs_datashape: Dict)-> str:
    column_list = ""
    for key in jobs_datashape:
        column_list = f"{column_list}, {key} {get_sql_type(jobs_datashape[key])}"
    final_column_statement = f"(id INTEGER PRIMARY KEY {column_list} );"
    return final_column_statement


def get_sql_type(sample_val)->str:
    if type(sample_val) == str:
        return "TEXT"
    elif type(sample_val) == int:
        return "INTEGER"
    elif type(sample_val) == float:
        return "FLOAT"
    else:
        return "TEXT" # for a default I'll go with text for now


def save_data(all_data, cursor):
    for coll_data in all_data:
        cursor.execute("""
        INSERT INTO university_data(school_id, school_name, student_size, university_state, three_year_earnings_over_poverty,
         loan_repayment)
         VALUES (?,?,?,?,?,?);
        """, (coll_data['id'], coll_data['school.name'], coll_data['2018.student.size'],
              coll_data['school.state'], coll_data['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line'],
              coll_data['2016.repayment.3_yr_repayment.overall']))


def save_excel_data(excel_data, cursor):
    first_item = excel_data[0]
    question_marks = ', '.join('?'*len(first_item)) # new to python? put one question mark for every data item
    column_names = ', '.join(list(first_item))
    insert_statement = f"INSERT INTO job_info ({column_names}) VALUES ({question_marks});"
    for record in excel_data:
        fill_in_blanks = tuple(record.values())
        cursor.execute(insert_statement, fill_in_blanks)