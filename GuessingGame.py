# Tumi Bopape 
# Guessing Game
# 07/03/2026



import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random




class MyWidget(QWidget):
    def __init__(self,parent =None):      # Mywidget constructor method 
        QWidget.__init__(self,parent)
        self.setGeometry(250,250,600,300)
        self.setWindowTitle('Guessing Game')
        
        # Creating all labels in the game 
        GUESSES=QLabel('Guesses: ')
        GUESSES.setFont(QFont('Arial',20,10))
        self.guess1= QLabel('Guess 1:')
        self.guess2= QLabel('Guess 2:')
        self.guess3= QLabel('Guess 3:')
        
        self.userguess1 = QLabel('') # Empty label as placeholder for user input
        self.userguess2 = QLabel('')
        self.userguess3 = QLabel('')
        
        self.feedback1 =QLabel('')
        self.feedback2 =QLabel('')
        self.feedback3 =QLabel('')
        
        
        
        INTERFACE=QLabel('Interface: ')
        INTERFACE.setFont(QFont('Arial',20,10))
        self.picture=QLabel('Picture ')
        self.colour =QLabel('Colour ')
        
        #Creating all buttons in the game 
        self.guess  =QPushButton('Guess')
        self.change =QPushButton('Change')
        self.close_btn  =QPushButton('Close')
        self.NewGame=QPushButton('New Game')
        
        #Creating all dropdown lists in the game
        self.picCombo= QComboBox()
        self.picCombo.addItem('Mickey')
        self.picCombo.addItem('Pluto')
        
        self.colourCombo =QComboBox()
        self.colourCombo.addItem('Red')
        self.colourCombo.addItem('Blue')
        
        #Line Edit 
        self.user = QLineEdit()
    
        
        # Using a grid layout to create the firsst panel for the guesses section 
        grid = QGridLayout()
        
        grid.addWidget(self.guess1, 0,0)
        grid.addWidget(self.userguess1,0,1)
        grid.addWidget(self.feedback1,0,2)
        
        grid.addWidget(self.guess2, 1, 0)
        grid.addWidget(self.userguess2, 1,1)
        grid.addWidget(self.feedback2, 1,2)
        
        grid.addWidget(self.guess3, 2,0)
        grid.addWidget(self.userguess3,2,1)
        grid.addWidget(self.feedback3,2, 2)
        
        grid.addWidget(self.user, 3, 1)
        grid.addWidget(self.guess, 3, 2)
        
        grid_widget = QWidget()
        grid_widget.setLayout(grid)
        
        
        # Using a grid layout to create the firsst panel for the interface section 
        grid1 =QGridLayout()
        grid1.addWidget(self.picture, 0,0)
        grid1.addWidget(self.colour, 1,0)
        grid1.addWidget(self.close_btn, 2,0) 
        grid1.addWidget(self.picCombo, 0,1)
        grid1.addWidget(self.colourCombo, 1,1)
        grid1.addWidget(self.NewGame , 2,1)         
        grid1.addWidget(self.change, 1,2)
        grid_widget1 = QWidget()
        grid_widget1.setLayout(grid1)
        
        #Including the photo 
        pixmap = QPixmap('pluto.gif')
        self.pic_label =QLabel()
        self.pic_label.setPixmap(pixmap)
        
        
        #Combining the guesses and interface panels using vbox 
        
        vbox =QVBoxLayout()
        vbox.addWidget(GUESSES)
        vbox.addWidget(grid_widget)
        vbox.addWidget(INTERFACE)
        vbox.addWidget(grid_widget1)
        vbox_widget = QWidget()
        vbox_widget.setLayout(vbox)
        
        # nested panel layout combining the main game layout and the picture using hbox  
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.pic_label)
        hbox.addWidget(vbox_widget)
        self.setLayout(hbox)
        self.setPalette(QPalette(QColor('blue')))        
        self.setAutoFillBackground(True)
        
        self.counter = 0 # Keeps track of guess events to allow each guess to be allocated correctly 
        self.special_num= random.randint(1,10) # Creates a global initial random number 
        # Event Handling : Signals 
        
        self.guess.clicked.connect(self.guess_clicked)
        self.close_btn.clicked.connect(self.close_clicked)
        self.NewGame.clicked.connect(self.NewGame_clicked)
        self.change.clicked.connect(self.change_clicked)
        
    
        # Event Handling : Callables 
        
    def guess_clicked(self):
        
        self.counter +=1 # increments the counter to allow each guess to be distinguishable 
        if self.counter ==1:
            text = self.user.text()
            num= eval(text)
            self.userguess1.setText(text)
            
            if num == self.special_num:
                self.feedback1.setText('Correct')
            elif num< self.special_num:
                self.feedback1.setText('Too Small')
            else:
                self.feedback1.setText('Too big') 
                
        elif self.counter ==2:
            text = self.user.text()
            num= eval(text)
            self.userguess2.setText(text)
            
            if num == self.special_num:
                self.feedback2.setText('Correct')
            elif num< self.special_num:
                self.feedback2.setText('Too Small')
            else:
                self.feedback2.setText('Too big') 
                
        elif self.counter==3:
            text = self.user.text()
            num= eval(text)
            self.userguess3.setText(text)
            
            
            if num == self.special_num:
                self.feedback3.setText('Correct')
            elif num< self.special_num:
                self.feedback3.setText('Too Small')
            else:
                self.feedback3.setText('Too big') 
        
            
    def close_clicked(self):
        self.close()
            
    def change_clicked(self):
        usecolour = self.colourCombo.currentText()
        usepicture = self.picCombo.currentText()
        
        #Colour 
        if usecolour == 'Red':
            self.setPalette(QPalette(QColor('red')))        
            self.setAutoFillBackground(True)            
        else:
            self.setPalette(QPalette(QColor('blue')))        
            self.setAutoFillBackground(True)
        #Picture 
        if usepicture =='Mickey':
            pixmap = QPixmap('mickey.gif')
            self.pic_label.setPixmap(pixmap)
                        
            
        else:
            pixmap = QPixmap('pluto.gif')
            self.pic_label.setPixmap(pixmap)
                        
    
    def NewGame_clicked(self):
        self.special_num= random.randint(1,10) # Setting a new guess number 
        
        self.userguess1.setText('')
        self.userguess2.setText('')
        self.userguess3.setText('')
        
        self.feedback1.setText('') 
        self.feedback2.setText('') 
        self.feedback3.setText('') 
        
        self.counter =0 
            
        
def main():
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
        
main()
        
        
    

