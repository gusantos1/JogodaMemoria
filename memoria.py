import sys
from random import sample
from JogodaMemoria.memoriagui import *
from PyQt5.QtWidgets import QMainWindow,QApplication
class Main(QMainWindow,Ui_MainWindow):
    # globais
    elementos_matriz = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    matriz = []
    jogadas = termina = c = 0
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.mascara1 = None
        self.mascara2 = None
        self.foi_clicado = None
        self.foi_sorteado = None
        self.forma_matriz()
        # Cliques
        self.btn0x0.clicked.connect(self.input_btn0x0)
        self.btn0x1.clicked.connect(self.input_btn0x1)
        self.btn0x2.clicked.connect(self.input_btn0x2)
        self.btn0x3.clicked.connect(self.input_btn0x3)
        self.btn1x0.clicked.connect(self.input_btn1x0)
        self.btn1x1.clicked.connect(self.input_btn1x1)
        self.btn1x2.clicked.connect(self.input_btn1x2)
        self.btn1x3.clicked.connect(self.input_btn1x3)
        self.btn2x0.clicked.connect(self.input_btn2x0)
        self.btn2x1.clicked.connect(self.input_btn2x1)
        self.btn2x2.clicked.connect(self.input_btn2x2)
        self.btn2x3.clicked.connect(self.input_btn2x3)
        self.btn3x0.clicked.connect(self.input_btn3x0)
        self.btn3x1.clicked.connect(self.input_btn3x1)
        self.btn3x2.clicked.connect(self.input_btn3x2)
        self.btn3x3.clicked.connect(self.input_btn3x3)
    def forma_matriz(self):
        """Função que estrutura a matriz 4x4 cobrindo-a com '*' e
        acrescenta False referente ao par ainda não encontrado.
        Estrutura: [valor_sample,'*',False]. Sem parâmetros de entrada."""
        lista_temp = []
        for linha in range(0, 4):
            for coluna in range(1, 5):
                elemento_sorteado = sample(self.elementos_matriz, 1)[0]
                lista_temp.append(elemento_sorteado)
                self.elementos_matriz.remove(elemento_sorteado)
                lista_temp.append('*')
                lista_temp.append(False) # Se o par já foi sorteado
                lista_temp.append(False) # Se já foi clicado
                if coluna % 4 == 0:
                    self.matriz.append(lista_temp)
                    lista_temp = []
            print(self.matriz)
    #Butões
    def setter_btn(self,x,y):
        self.foi_clicado = self.matriz[x][y * 4 + 3]
        self.foi_sorteado = self.matriz[x][y * 4 + 2]
        if self.foi_sorteado is False and self.foi_clicado is False:
            self.matriz[x][y * 4 + 1] = str(self.matriz[x][y * 4]) #asterisco recebendo o valor
            self.matriz[x][y * 4 + 3] = True
            print(self.matriz)
            if self.c == 0:
                self.x1 = x
                self.y1 = y
            else:
                self.x2 = x
                self.y2 = y
                self.c = 0
                return self.verifica(self.x1, self.y1, self.x2, self.y2)
            self.c += 1
    def add_icon(self, x, y):
        """Função que adiciona o ícone no botão conforme o valor referente na matriz."""
        if self.matriz[x][y*4] == 1:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g1.png"))')
        elif self.matriz[x][y*4] == 2:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g2.png"))')
        elif self.matriz[x][y*4] == 3:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g3.png"))')
        elif self.matriz[x][y*4] == 4:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g4.png"))')
        elif self.matriz[x][y*4] == 5:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g5.png"))')
        elif self.matriz[x][y*4] == 6:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g6.png"))')
        elif self.matriz[x][y*4] == 7:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g7.png"))')
        else:
            eval(f'self.btn{x}x{y}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/g8.png"))')
        return eval(f'self.btn{x}x{y}.setIconSize(QtCore.QSize(140,210))')
    def input_btn0x0(self):
        x, y = 0, 0
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn0x1(self):
        x, y = 0, 1
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn0x2(self):
        x, y = 0, 2
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn0x3(self):
        x, y = 0, 3
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn1x0(self):
        x, y = 1, 0
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn1x1(self):
        x, y = 1, 1
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn1x2(self):
        x, y = 1, 2
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn1x3(self):
        x, y = 1, 3
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn2x0(self):
        x, y = 2, 0
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn2x1(self):
        x, y = 2, 1
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn2x2(self):
        x, y = 2, 2
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn2x3(self):
        x, y = 2, 3
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn3x0(self):
        x, y = 3, 0
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn3x1(self):
        x, y = 3, 1
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn3x2(self):
        x, y = 3, 2
        self.add_icon(x, y)
        return self.setter_btn(x, y)
    def input_btn3x3(self):
        x, y = 3, 3
        self.add_icon(x, y)
        return self.setter_btn(x, y)

    #Verificação dos Pares
    def verifica(self,x1,y1,x2,y2):
        self.jogadas += 1
        if self.matriz[x1][y1 * 4] != self.matriz[x2][y2 * 4]:
            #Retornar asterisco se o par for diferente.
            self.matriz[x1][y1 * 4 + 1] = '*'
            self.matriz[x2][y2 * 4 + 1] = '*'
            #Retornar foi_clicado como False.
            self.matriz[x2][y2 * 4 + 3] = False
            self.matriz[x1][y1 * 4 + 3] = False
            self.ln_resultado.setText('\t\t\tVocê errou... tente de novo.')
            #Retorna asterisco se não formar par.
            eval(f'self.btn{x1}x{y1}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/ast.png"))')
            eval(f'self.btn{x2}x{y2}.setIcon(QtGui.QIcon("../../../../Área de Trabalho/ast.png"))')
        else:
            self.termina += 1
            self.ln_resultado.setText('\t\t\tParabéns você acertou !')
            #Retornar foi_sorteado como True
            self.matriz[x1][y1 * 4 + 2] = True
            self.matriz[x2][y2 * 4 + 2] = True
            if self.termina == 8:
                self.ln_resultado.setText(f'\t\tParabéns! Você descobriu todas as casas com {self.jogadas} jogadas')
        print(f'Jogadas: {self.jogadas}, termina: {self.termina}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela = Main()
    tela.show()
    sys.exit(app.exec_())
