from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
  
  
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
  
# Adding an icon
icon = QIcon("icon.png")
  
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

def openBrowser():
    import threading, webbrowser
    url = "http://127.0.0.1:5000/home"
    #webbrowser.open_new_tab(url)
    threading.Timer(1.25, lambda: webbrowser.open_new_tab(url)).start()

# Creating the options
menu = QMenu()
openAction = QAction("Open")
openAction.triggered.connect(openBrowser)
menu.addAction(openAction)
  
# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)
  
app.exec_()