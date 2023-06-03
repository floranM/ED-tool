"""
main.py - fichier principal du programme

"""
import sys
import time

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QLabel, QWidget, QSystemTrayIcon, QMenu, QVBoxLayout
from PySide6.QtGui import QIcon, QAction, QFont, QGuiApplication, QPalette, QColor

def main():
    app = QApplication(sys.argv)
    
    # Create the icon
    icon = QIcon("assets/ico.png")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()
    action = QAction("A menu item")
    menu.addAction(action)

    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)
    
    window = MainWindow()
    window.setStyleSheet("""
                            windows {
                                background-color: "ivory";
                                color: "black";
                            }
                            QLabel {
                                color: "hotpink"
                            }
                            QPushButton {
                                font-size: 16px;
                                background-color: "darkgreen"
                            }
                            QLineEdit {
                                background-color: "white";
                                color: "black";
                            }
                        """)
    window.show()
    sys.exit(app.exec())

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def ChooseTheme(self, start=0):
        print("Appui sur le bouton")
        if start != 0:
            return 0
        elif start == 0:
            action = self.sender()
            print(action.data())
            
            if action.data() == 'light':
                print('light')
            elif action.data() == 'dark':
                print('dark')
            else:
                print('erreur lors de la selection du thème.')
        
        self.setStyleSheet("""
                            Windows {
                                background-color: "black";
                                color: "white";
                            }
                            QLabel {
                                color: "yellow"
                            }
                            QPushButton {
                                font-size: 24px;
                                background-color: "red"
                            }
                            QLineEdit {
                                background-color: "white";
                                color: "black";
                            }
                        """)
    
    def initUI(self):
        
        self.ChooseTheme(1)
        # définition des actions des menus/toolbar
        exitAct = QAction(QIcon('assets/ico.png'), '&Quitter', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Quitter l\'application')
        exitAct.triggered.connect(QApplication.instance().quit)
        
        lightThemeAct = QAction('&Light Theme', self)
        lightThemeAct.setData('light')
        lightThemeAct.triggered.connect(self.ChooseTheme)
        darkThemeAct = QAction('&Dark Theme', self)
        darkThemeAct.setData('dark')
        darkThemeAct.triggered.connect(self.ChooseTheme)

        self.statusBar()
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Fichier')
        themeMenu = menubar.addMenu('&Thèmes')
        fileMenu.addAction(exitAct)
        themeMenu.addAction(lightThemeAct)
        themeMenu.addAction(darkThemeAct)
    

        # Contenu de la fenetre
        CmdLabel = QLabel('Commandant')
        CmdLabel.setContentsMargins(5,0,10,0)
        CmdValueLabel = QLabel('Name of CMD')
        CmdValueLabel.setContentsMargins(10,0,10,0)
        ShipLabel = QLabel('Vaisseau')
        ShipLabel.setContentsMargins(5,0,10,0)
        ShipValueLabel = QLabel('Name of ship')
        ShipValueLabel.setContentsMargins(10,0,10,0)
        
        vLayout = QVBoxLayout()
        gridCMD = QGridLayout()
        
        gridCMD.addWidget(CmdLabel, 1, 0)
        gridCMD.addWidget(CmdValueLabel, 1, 1)
        gridCMD.addWidget(ShipLabel, 2, 0)
        gridCMD.addWidget(ShipValueLabel, 2, 1)
        gridCMD.setRowStretch(gridCMD.rowCount(), 1)
        gridCMD.setColumnStretch(gridCMD.columnCount(), 1)
        
        welcomeMessage = QLabel('Bienvenu Commandant')
        PoliceMessage = QFont('Times', 20)
        PoliceMessage.setBold(True)
        #PoliceMessage.setItalic(True)
        welcomeMessage.setFont(PoliceMessage)
    
        
        
        vLayout.addWidget(welcomeMessage)
        vLayout.addLayout(gridCMD)

        widget = QWidget()
        grid = vLayout
        widget.setLayout(grid)
        self.setCentralWidget(widget)
         
        # Mise en place de la fenetre.
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(int(screen.width()/4), int(screen.height()/4), int(screen.width()/2), int(screen.height()/2))
        self.setWindowTitle('ED-tool')
        self.setWindowIcon(QIcon('assets/ico.png'))
        #self.setWindowOpacity(0.9)
       
        self.setStyleSheet("background-color: rgba(255,100,100,255);")
       
        self.show()

if __name__ == "__main__":
    print("Hello, World!")
    main()