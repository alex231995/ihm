from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from MainBubble import *

class BubbleWidget(QWidget):
	
	def __init__(self,):
		super().__init__()
		self.targets = []
		
		fic = open("src_tp_bubble.csv")
		for line in fic:
			x,y,size = line.split(",")
			self.targets.append(Target(int(x),int(y),int(size)))
		self.cursor = BubbleCursor(self.targets)
		
	def paintEvent(self, event):
		painter = QPainter(self)
		for target in self.targets:
			target.paint(painter)
		self.cursor.paint(painter)

