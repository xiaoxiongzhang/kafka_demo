import sys
from dataclasses import dataclass, field

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QInputDialog, QLineEdit

from tools_ui import Ui_MainWindow


@dataclass
class InputData:
    bootstrap_servers: str
    topic: str
    output: str


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.start.clicked.connect(self.handle)
        self.output_toolButton.clicked.connect(self.explorer)

    def load_data(self):
        ...

    def handle(self):
        ...

    def explorer(self):
        ...

    def operation_status(self, a0):
        self.start.setEnabled(a0)
        self.bootstrap_serverslineEdit.setEnabled(a0)
        self.topic_lineEdit_2.setEnabled(a0)
        self.output_lineEdit_3.setEnabled(a0)
        self.output_toolButton.setEnabled(a0)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_w = MainWindow()

    main_w.show()
    sys.exit(app.exec_())
