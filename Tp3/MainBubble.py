import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from BubbleWidget import *
from BubbleCursor import *


class Target:
	
    defaultCol = Qt.blue
    highlightCol = Qt.green
    toSelectCol = Qt.red

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self, qPainter):
        if(self.toSelect):
            qPainter.setBrush(self.toSelectCol)

        elif(self.highlighted):
            qPainter.setBrush(self.highlightCol)

        else:
            qPainter.setBrush(self.defaultCol)
        
        bbox = QRect(QPoint(self.x, self.y), QSize(self.size, self.size))
        qPainter.drawEllipse(bbox)
	
def main(args) :
	app = QApplication(args)
	win = QMainWindow()
	bw = BubbleWidget()
	win.setCentralWidget(bw)
	win.resize(1024,800)
	win.show()
	app.exec()


if __name__ == "__main__":
	main(sys.argv)

