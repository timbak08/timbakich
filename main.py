from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.qp = QPainter()
        self.coords_ = [randint(0, 100), randint(0, 100)]
        self.pen = QPen()
        self.pen.setWidth(3)
        self.pen.setColor(QColor('yellow'))
        self.label = QLabel()
        self.label.resize(700, 300)
        canvas = QPixmap(900, 700)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def run(self):
        x, y = [randint(10, 500) for i in range(2)]
        R = randint(10, 500)
        painter = QPainter(self.label.pixmap())
        painter.setPen(self.pen)
        painter.drawEllipse(x, y, R, R)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

