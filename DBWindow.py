from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox
from typing import List, Dict


class DataWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.list_control = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("API Data GUI")
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400,350)
        self.setGeometry(300,100, 400, 500)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(300, 400)
        api_db_demo_button = QPushButton("Push me for Data Visual", self)
        api_db_demo_button.move(100, 400)
        api_db_demo_button.clicked.connect(self.do_something_to_test)
        self.show()

    def put_data_in_list(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['state_name']}\t\t{item['occ_title']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    def do_something_to_test(self):
        message_box = QMessageBox(self)
        message_box.setText("You just pushed the button - imagine database work here")
        message_box.setWindowTitle("API Data")
        message_box.show()