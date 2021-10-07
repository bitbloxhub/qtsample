import sys
import requests
from PySide6 import QtCore, QtWidgets
from __feature__ import snake_case  # noqa: F401
from __feature__ import true_property  # noqa: F401


class HTTPGet(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.url = QtWidgets.QLineEdit()
        self.url.placeholder_text = "URL here"

        self.get_button = QtWidgets.QPushButton("Get the page!!!")
        self.get_button.clicked.connect(self.get)

        self.content = QtWidgets.QTextEdit()
        self.content.placeholder_text = "Content here"

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.add_widget(self.url)
        self.layout.add_widget(self.get_button)
        self.layout.add_widget(self.content)

    @QtCore.Slot()
    def get(self):
        self.content.plain_text = requests.get(self.url.text).text


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = HTTPGet()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
