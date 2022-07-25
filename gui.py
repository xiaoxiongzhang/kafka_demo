import datetime
import os.path
import sys
import time
import traceback
from dataclasses import dataclass

from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QLineEdit

from main import KafkaHandler
from tools_ui import Ui_MainWindow


@dataclass
class InputData:
    bootstrap_servers: str
    topic: str
    output: str


def echo_log(content: str):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
    return f"[{time_str}]  {content}"


class MainWindow(QMainWindow, Ui_MainWindow):
    echo_signal = pyqtSignal(str)
    operation_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self._echo = lambda s: self.plainTextEdit.appendPlainText(echo_log(s))
        self.echo_signal.connect(self._echo)
        self.operation_signal.connect(self.operation_status)

        self.start.clicked.connect(self.handle)
        self.output_toolButton.clicked.connect(self.explorer)

    def load_data(self):
        bootstrap_servers = self.bootstrap_serverslineEdit.text()
        topic = self.topic_lineEdit_2.text()
        output = self.output_lineEdit_3.text()
        input_data = InputData(
            bootstrap_servers=bootstrap_servers,
            topic=topic,
            output=output
        )
        return input_data

    def handle(self):
        self._echo("开始下载Kafka数据...")
        self.operation_status(False)
        self.dump_t = DumpThread(self)
        self.dump_t.start()

    def explorer(self):
        path = QFileDialog.getExistingDirectory(self, "选择文件下载路径", "./")
        self.output_lineEdit_3.setText(path)

    def operation_status(self, a0):
        self.start.setEnabled(a0)
        self.bootstrap_serverslineEdit.setEnabled(a0)
        self.topic_lineEdit_2.setEnabled(a0)
        self.output_lineEdit_3.setEnabled(a0)
        self.output_toolButton.setEnabled(a0)


class DumpThread(QThread):
    def __init__(self, window: MainWindow):
        super(DumpThread, self).__init__()
        self.w = window

    def run(self):
        try:
            data = self.w.load_data()
            file_name = f"{data.topic}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
            file_path = data.output + "/" + file_name
            kafka_handler = KafkaHandler(bootstrap_servers=data.bootstrap_servers)
            kafka_handler.dumps(file_path, data.topic)
        except:
            self.w.echo_signal.emit(traceback.format_exc())
        else:
            self.w.echo_signal.emit(f"Kafka数据下载完成，下载文件见：【{file_path}】")
        finally:
            self.w.operation_signal.emit(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_w = MainWindow()

    main_w.show()
    sys.exit(app.exec_())
