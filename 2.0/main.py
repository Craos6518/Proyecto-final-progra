from PyQt5 import QtCore, QtGui, QtWidgets
from Botones import MiFormulario

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 81, 51))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.popWindow) #Añadir un evento de clic para el botón
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MENU"))
        self.pushButton.setText(_translate("MainWindow", "CALCULADORA SIMPLE"))
        
    #Mostrar la función de la segunda ventana (consistente con el contenido en la función principal correspondiente generada automáticamente en UI_second.py)
    def popWindow(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = MiFormulario()
        self.ui2.__init__(self.form2)
        self.form2.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

