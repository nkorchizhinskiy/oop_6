import sys
from tkinter import Spinbox
from PyQt5.QtWidgets import QDialog, \
                            QVBoxLayout, \
                            QPushButton, \
                            QSpinBox, \
                            QHBoxLayout, \
                            QWidget                    
from PyQt5.QtGui import QPainter, \
                        QBrush, \
                        QColor
from PyQt5.QtCore import QPointF



class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        
        self.resize(700, 800)
        self.setWindowTitle('Лабораторная номер 6')

        #// Create Widgets
        self.spinbox = QSpinBox(self)
        self.spinbox.setPrefix('Скорость: ')
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(100)
        self.spinbox.move(50, 50)

        self.button_1 = QPushButton('Начать', self)
        self.button_2 = QPushButton('Выход', self)
        
        self.board = Board(self.spinbox.value())

        #// SIGNALS
        self.button_1.clicked.connect(lambda: self.board.start_game(True))
        self.spinbox.valueChanged.connect(lambda: self.board.change_speed(
                                                  self.spinbox.value()))
        self.button_2.clicked.connect(lambda: sys.exit())

        #// Create Layout --->
        #// Horizontal layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.button_1)
        buttons_layout.addWidget(self.button_2)
        
        #// Vertical Layout
        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.board)
        layout.addLayout(buttons_layout)        
        self.setLayout(layout)
       

class Board(QDialog):
    
    def __init__(self, spinbox):
        super().__init__()
        self.spinbox = spinbox

        #// Start ball's position
        self.x = 150
        self.y = -1

        self.setStyleSheet('background-color: #CCF')
        self.flag_x = 1
        self.flag_y = 1
        self.is_game_run = False
    
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.draw_rect()
        self.painter.end()

    def draw_rect(self):
        #// Set brush to fill ellipse
        brush = QBrush(QColor(255, 0, 0))
        self.painter.setBrush(brush)
        self.painter.drawEllipse((QPointF(self.x, self.y)), 40, 40)

        #// Change x Axis. Set Flag to change.
        if self.x <= 40:
            self.flag_x = 1
        elif self.x >= self.width()-40:
            self.flag_x = -1
        #// Change x's value
        if self.flag_x == 1:
            self.x += self.spinbox/100
        else:
            self.x -= self.spinbox/100
        
        #// Change y Axis. Set Flag to change.
        if self.y <= 40:
            self.flag_y = 1
        elif self.y >= self.height()-40:
            self.flag_y = -1
        #// Change y's value
        if self.flag_y == 1:
            self.y += self.spinbox/100
        else:
            self.y -= self.spinbox/100
        
        #// Check button clicked    
        if self.is_game_run:
            self.update()

    def change_speed(self, value):
        """Change speed of ellipse in conformity with spinbox value"""
        self.spinbox = value

    def start_game(self, start_flag):
        """Set True value, which help to start ball's moving"""
        if start_flag:
            self.is_game_run = True
            self.update()
        