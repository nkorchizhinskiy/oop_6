from tkinter import Spinbox
from PyQt5.QtWidgets import QDialog, \
                            QVBoxLayout, \
                            QPushButton, \
                            QSpinBox, \
                            QHBoxLayout, \
                            QWidget                    
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF
from matplotlib.pyplot import draw



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.resize(700, 800)
        self.setWindowTitle('Лабораторная номер 6')

        #// Create Widgets
        self.spinbox = QSpinBox(self)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(100)
        self.spinbox.move(50, 50)
        self.spinbox.setPrefix('Скорость: ')

        self.button_1 = QPushButton('Начать', self)
        self.button_2 = QPushButton('Выход', self)
        
        self.board = Board(self.spinbox.value())

        #// SIGNALS
        # self.button_1.clicked.connect(self.board.draw_rect)
        self.spinbox.valueChanged.connect(lambda: self.board.change_speed(
            self.spinbox.value()))

        #// Create Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.button_1)
        buttons_layout.addWidget(self.button_2)
        
        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.board)
        layout.addLayout(buttons_layout)        
        self.setLayout(layout)
       

class Board(QDialog):
    
    def __init__(self, spinbox):
        super().__init__()
        self.setStyleSheet('background-color: #90EE90')
        self.x = 150
        self.flag = 1
        self.spinbox = spinbox
    
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.draw_rect()
        self.painter.end()

    def draw_rect(self):
        self.painter.drawEllipse((QPointF(self.x, self.height()//2)), 40, 40)
        if self.x <= 40:
            self.flag = 1
        elif self.x >= self.width()-40:
            self.flag = -1
        
        if self.flag == 1:
            self.x += self.spinbox/100
        else:
            self.x -= self.spinbox/100
        self.update()

    def change_speed(self, value):
        self.spinbox = value
