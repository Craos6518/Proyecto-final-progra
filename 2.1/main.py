from PyQt5 import QtCore, QtGui, QtWidgets
from UI.COMPLEMENTOS.SIMPLE.Calculadora_Principal import MiFormulario
from UI.COMPLEMENTOS.RESISTENCIA.Resistencia_Principal import MiApp2
from UI.COMPLEMENTOS.INFO.Info import Ui_Form3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 81, 51))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 150, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton.clicked.connect(self.popWindow) #Añadir un evento de clic para el botón
        self.pushButton_2.clicked.connect(self.popWindow2) #Añadir un evento de clic para el botón
        self.pushButton_3.clicked.connect(self.popWindow3) #Añadir un evento de clic para el botón
        
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
        self.pushButton_2.setText(_translate("MainWindow", "RESISTENCIAS"))
        self.pushButton_3.setText(_translate("MainWindow", "INFO"))

    #Mostrar la función de la calculadora simple (consistente con el contenido en la función principal correspondiente generada automáticamente en UI_second.py)
    def popWindow(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = MiFormulario()
        self.ui2.__init__(self.form2)
        self.form2.show()
    #Mostrar la función de la GRAFICADORA (consistente con el contenido en la función principal correspondiente generada automáticamente en UI_second.py)
    def popWindow2(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = MiApp2()
        self.ui2.__init__(self.form2)
        self.form2.show()

    #Mostrar la función de la info (consistente con el contenido en la función principal correspondiente generada automáticamente en UI_second.py)
    def popWindow3(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = Ui_Form3()
        self.ui2.setupUi3(self.form2)
        self.form2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
#No se sigue con la idea de la calculadora didactica
#Se adopta la idea de un graficador