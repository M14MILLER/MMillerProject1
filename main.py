import api_data
import db_handler
import excelwork


def main():
    api_data = []
    excel_data = excelwork.get_excel_jobs_info('state_M2019_dl.xlsx')
    conn, cursor = db_handler.open_db("college_db.sqlite")
    db_handler.make_tables(cursor, excel_data[0])
    db_handler.save_data(api_data, cursor)
    db_handler.save_excel_data(excel_data, cursor)
    db_handler.close_db(conn)


if __name__ == '__main__':
    main()
