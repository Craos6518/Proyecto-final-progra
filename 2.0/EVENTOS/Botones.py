import sys
from UI.CALCULADORA_ui import *
class MiFormulario(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
        self.ui.BOTON0.clicked.connect(self.Obtener)
        self.ui.BOTON1.clicked.connect(self.Obtener1)
        self.ui.BOTON2.clicked.connect(self.Obtener2)
        self.ui.BOTON3.clicked.connect(self.Obtener3)
        self.ui.BOTON4.clicked.connect(self.Obtener4)
        self.ui.BOTON5.clicked.connect(self.Obtener5)
        self.ui.BOTON6.clicked.connect(self.Obtener6)
        self.ui.BOTON7.clicked.connect(self.Obtener7)
        self.ui.BOTON8.clicked.connect(self.Obtener8)
        self.ui.BOTON9.clicked.connect(self.Obtener9)
        self.ui.MENOS.clicked.connect(self.Obtener10)
        self.ui.MAS.clicked.connect(self.Obtener11)
        self.ui.POR.clicked.connect(self.Obtener12)
        self.ui.DIVIDIDO.clicked.connect(self.Obtener13)
        self.ui.PORCENTAJE.clicked.connect(self.Obtener14)
        self.ui.IGUAL.clicked.connect(self.Obtener15)
        self.ui.PARENTECIS_1.clicked.connect(self.Obtener16)
        self.ui.PARENTECIS_2.clicked.connect(self.Obtener17)
        self.ui.PUNTO.clicked.connect(self.Obtener18)
        self.ui.BOTON_AC.clicked.connect(self.Obtener19)

    def Obtener(self):
        Entrada = self.ui.Valor.text()
        Entrada += "0"
        self.ui.Valor.setText(Entrada)

    def Obtener1(self):
        Entrada = self.ui.Valor.text()
        Entrada += "1"
        self.ui.Valor.setText(Entrada)

    def Obtener2(self):
        Entrada = self.ui.Valor.text()
        Entrada += "2"
        self.ui.Valor.setText(Entrada)

    def Obtener3(self):
        Entrada = self.ui.Valor.text()
        Entrada += "3"
        self.ui.Valor.setText(Entrada)

    def Obtener4(self):
        Entrada = self.ui.Valor.text()
        Entrada += "4"
        self.ui.Valor.setText(Entrada)

    def Obtener5(self):
        Entrada = self.ui.Valor.text()
        Entrada += "5"
        self.ui.Valor.setText(Entrada)

    def Obtener6(self):
        Entrada = self.ui.Valor.text()
        Entrada += "6"
        self.ui.Valor.setText(Entrada)

    def Obtener7(self):
        Entrada = self.ui.Valor.text()
        Entrada += "7"
        self.ui.Valor.setText(Entrada)

    def Obtener8(self):
        Entrada = self.ui.Valor.text()
        Entrada += "8"
        self.ui.Valor.setText(Entrada)

    def Obtener9(self):
        Entrada = self.ui.Valor.text()
        Entrada += "9"
        self.ui.Valor.setText(Entrada)

    def Obtener10(self):
        Entrada = self.ui.Valor.text()
        Entrada += "-"
        self.ui.Valor.setText(Entrada)

    def Obtener11(self):
        Entrada = self.ui.Valor.text()
        Entrada += "+"
        self.ui.Valor.setText(Entrada)

    def Obtener12(self):
        Entrada = self.ui.Valor.text()
        Entrada += "*"
        self.ui.Valor.setText(Entrada)

    def Obtener13(self):
        Entrada = self.ui.Valor.text()
        Entrada += "/"
        self.ui.Valor.setText(Entrada)

    def Obtener14(self):
        Entrada = self.ui.Valor.text()
        try:
            self.an = (Entrada +"/100")
            self.ui.Valor.setText(self.an)
        except:
            self.ui.Valor.setText("")

    def Obtener15(self):
        Entrada = self.ui.Valor.text()
        try:
            ans = eval(Entrada)
            self.ui.Valor.setText(str(ans))
        except:
            self.ui.Valor.setText("ERROR")

    def Obtener16(self):
        Entrada = self.ui.Valor.text()
        Entrada += "("
        self.ui.Valor.setText(Entrada)
    
    def Obtener17(self):
        Entrada = self.ui.Valor.text()
        Entrada += ")"
        self.ui.Valor.setText(Entrada)

    def Obtener18(self):
        Entrada = self.ui.Valor.text()
        Entrada += "."
        self.ui.Valor.setText(Entrada)

    def Obtener19(self):
        Entrada = self.ui.Valor.text()
        self.ui.Valor.setText(Entrada[:len(Entrada)-1])

'''if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mi_app = MiFormulario()
    Mi_app.show()
    sys.exit(app.exec_())'''