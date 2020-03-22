from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from random import randint
import clickhouse_driver

from MainWindow import Grafic

import time
import clickhouse_driver

from MainWindow import Ui_MainWindow

client = clickhouse_driver.Client("127.0.0.1")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.old = 0

        self.Graf = Grafic(self, int(self.lineEdit_1.text()), int(self.lineEdit_2.text()), v = self.old)
        self.Graf.move(235, 10)

        # Setup numbers.
        for n in range(0, 8):
            getattr(self, 'pushButton_%s' % n).pressed.connect(lambda v=n: self.DrowGraf(v))

        self.lineEdit_1.returnPressed.connect(lambda v=self.old: self.DrowGraf(v))
        self.lineEdit_2.returnPressed.connect(lambda v=self.old: self.DrowGraf(v))

        self.show()
        #self.Update()

    def DrowGraf(self, v):
        startInterval = int(self.lineEdit_1.text())
        endInterval = int(self.lineEdit_2.text())
        self.old = v
        if(startInterval < endInterval):
            self.Graf.drow(startInterval, endInterval, v)





if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Web")

    window = MainWindow()
    app.exec_()