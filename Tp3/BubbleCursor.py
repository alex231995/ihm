import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BubbleCursor:
	
	defaultCol = Qt.yellow
	
	def __init__(self,listTargets):
		self.x = 0
		self.y = 0
		self.size = 0
		self.cercleCenterX = 0
		self.cercleCenterY = 0
		self.cercleX = 0
		self.cercleY = 0
		self.cercleSize = 0
		self.listTarget = listTargets
		self.closest = None
		self.selected = None
	
	def paint(self, QPainter):
		QPainter.setBrush(self.defaultCol)
		pen = QPen()
		
		bbox = QRect(QPoint(self.cercleCenterX-((self.cercleSize*3)/2), self.cercleCenterY-((self.cercleSize*3)/2)), QSize(self.cercleSize, self.cercleSize)*3)
		pen.setWidth(0)
		pen.setBrush(QColor(0, 0, 0))
		qPainter.setPen(pen)
		qPainter.setBrush(QColor("#e6005c"))
		qPainter.drawEllipse(bbox)
		bbox = QLine(self.x, self.y, self.cercleCenterX, self.cercleCenterY)
		pen.setWidth(2)
		pen.setBrush(QColor("#669999"))
		qPainter.setPen(pen)
		qPainter.drawLine(bbox)
		
	
	
