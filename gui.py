import threading
import pygame

from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit, QTableWidget, QTableWidgetItem

#Définir les couleurs

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#créé class Gui

class Gui(threading.Thread,QMainWindow):



    def __init__(self,x = 20,y = 40): #init taille da la grill
        threading.Thread.__init__(self)
        self.width = 20
        self.height = 20
        self.margin = 5
        self.grid = []
        self.x = x
        self.y = y

        for row in range(self.x):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.y):
                self.grid[row].append(0)  # Append a cell


    def updateCell(self, x, y, valeur):

        self.grid[x][y] = valeur

    def run(self):
        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [self.x*(self.width+self.margin)+self.margin, self.height*(self.y+self.margin)+self.margin,]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Jeu de la vie TORRES PREVOST")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        def __init__(self):
                super().__init__()
                self.initUI()

        def initUI(self):

                menubar = self.menuBar()
                fichierMenu = menubar.addMenu("Fichier")


                recAct = QAction("Enregistrer", self)
                recAct.triggered.connect(self.rec)
                recAct.setShortcut('ctrl+S')
                recAct.setStatusTip('Enregistrer un fichier')

                fichierMenu.addAction(recAct)


                self.setMinimumSize(1280, 720)

                self.setWindowTitle('RAVI 2')

                self.myWidget = MyTableWidget(self)

                self.setCentralWidget(self.myWidget)

                self.show()


        def rec(self):
                print("rec")

        class MyTableWidget(QWidget):

            def __init__(self, parent):
                super(QWidget, self).__init__(parent)
                self.layout = QVBoxLayout(self)

                # Initialize tab screen
                self.tabs = QTabWidget()
                self.tab1 = QWidget()
                self.tab2 = QWidget()

                # Add tabs
                self.tabs.addTab(self.tab1, "Onglet 1")

                self.tab1.layout = QVBoxLayout(self)
                openButton = QPushButton("Nom ?")
                openButton.clicked.connect(self.openClick)

                self.tab1.layout.addWidget(openButton)
                self.tab1.setLayout(self.tab1.layout)
                self.tab1.setStyleSheet("background-image: url(./banniere_23.jpg); background-attachment: fixed;")



                saveButton = QPushButton("Sauvegarde")
                saveButton.clicked.connect(self.saveClick)
                self.tab2.layout.addWidget(saveButton)

                self.tab2.setLayout(self.tab2.layout)

                # Add tabs to widget
                self.layout.addWidget(self.tabs)
                self.setLayout(self.layout)

            # Dictionnaire
            def saveClick(self):
                print("save")

                # save Tableau Onglet 2
                import json
                with open("data.json", "w") as info_personnelle:
                    json.dump(dictionnaire, info_personnelle)


        # -------- Main Program Loop -----------

        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # Set the screen background
            screen.fill(BLACK)
            # Draw the grid

            for row in range(self.x):
                for column in range(self.y):
                    color = WHITE
                    if self.grid[row][column] == 1:
                        color = BLACK
                    if self.grid[row][column] == 2:
                        color = RED
                    if self.grid[row][column] == 3:
                        color = GREEN
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()
