import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
        print("Window")

        def __init__(self):
                super(MainWindow,self).__init__()
                self.resize(400,400)

                bar = self.menuBar()

                fileMenu = bar.addMenu("Fichier")

                OpenAct = QAction(QIcon("open.png"),"Open...",fileMenu)
                OpenAct.setShortcut("Ctrl+O")
                OpenAct.setStatusTip(self.tr("Open"))
                fileMenu.addAction(OpenAct)
                OpenAct.triggered.connect(self.openFile)

                SaveAct = QAction(QIcon("save.png"),"Save...",fileMenu)
                SaveAct.setShortcut("Ctrl+S")
                SaveAct.setStatusTip(self.tr("Save"))

                fileMenu.addAction(SaveAct)
                SaveAct.triggered.connect(self.saveFile)

                QuitAct = QAction(QIcon("quit.png"),"Quit...",fileMenu)
                QuitAct.setShortcut("Ctrl+X")
                QuitAct.setStatusTip(self.tr("Quit"))

                fileMenu.addAction(QuitAct)
                QuitAct.triggered.connect(self.quit)

                fileToolBar = QToolBar("Open")
                fileToolBar.addAction(OpenAct)
                self.addToolBar(fileToolBar)

                fileToolBar = QToolBar("Save")
                fileToolBar.addAction(SaveAct)
                self.addToolBar(fileToolBar)

                fileToolBar = QToolBar("Quit")
                fileToolBar.addAction(QuitAct)
                self.addToolBar(fileToolBar)

                self.textEdit = QTextEdit(self)
                self.setCentralWidget(self.textEdit)

                super(MainWindow,self).statusBar()

        def openFile(self):
                fileName = QFileDialog.getOpenFileName(self,"Open file","...")
                print(filename+"_____________")
                file = QFile(filename)
                if file.open(QFile.ReadOnly | QFile.Text):
                        stream = QTExtStream(file)
                        self.textEdit.setPlainText(stream.readAll())

        def saveFile(self):
                fileName = QFileDialog.getSaveFilename(self,"Save file",".../untitled")
                file = QFile(fileName)
                if file.open(QFile.WtriteOnly):
                        file.write(self.textEdit.toPlainText())
                print(filename)

        def closeEvent(self,event):
                quest = QMessageBox.question(self,"Quit","Voulez-vous vraiment quitter cette fenêtre ?","Non","Oui")
                if quest == 1:
                        self.close()
                else:
                        event.ignore()

        def quit(self):
                quest = QMessageBox.question(self,"Quit","Voulez-vous vraiment quitter cette fenêtre ?","Non","Oui")
                if quest == 1:
                        self.close()
                

        
                

def main(args):
	print(args)
	app = QApplication(args)
	w = MainWindow()
	w.resize(400,200)
	w.show()
	app.exec_()

	

                
        

if __name__ == "__main__":
        print("execution du programme")
        main(sys.argv)
        
