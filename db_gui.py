import openpyxl
import PySide6.QtWidgets
import sys
import DBWindow
import numbers
from typing import List, Dict


def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = DBWindow.api_dbDemoWindow(data)
    sys.exit(qt_app.exec_())


def get_test_data() -> List[Dict]:
    workbook_file = openpyxl.load_workbook("state_M2019_dl.xlsx")
    worksheet = workbook_file.active
    final_data_list = []
    for current_row in worksheet.rows:
        state_cell = current_row[0]
        state_name = state_cell.value
        hourly_mean = current_row[16].value
        if not isinstance(hourly_mean, numbers.Number):
            continue
        record = {"state_name": state_name, "hourly_mean": hourly_mean}
        final_data_list.append(record)
    return final_data_list


def get_key(value:dict):
    return value["hourly_mean"]


def main():
    test_data = get_test_data()
    test_data.sort(key=get_key)
    display_data(test_data)


if __name__ == '__main__':
    main()