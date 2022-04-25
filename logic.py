from PyQt5.QtWidgets import QDialog, \
                            QVBoxLayout, \
                            QPushButton, \
                            QSpinBox, \
                            QHBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib




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
        self.button_1.clicked.connect(self.draw)
        
        self.figure = plt.figure(facecolor='#CCCCCC')
        self.canvas = FigureCanvas(self.figure)

        #// Create Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.button_1)
        buttons_layout.addWidget(self.button_2)
        
        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.canvas)
        layout.addLayout(buttons_layout)        
        
        self.setLayout(layout)
        self.canvas.draw()
    
    def draw(self):
        plt.gcf().clear()
        circle1 = matplotlib.patches.Circle((0, 0), radius=0.1, fill=True)
        S
        self.cavnas.draw()
        