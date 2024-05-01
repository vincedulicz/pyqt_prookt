import sys

# PySide6 csomagból importáljuk az alkalmazás, a widgetek és a címkék osztályait
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap, QMovie
from PySide6.QtCore import QSize

# Főablak osztály létrehozása, QWidget-ből származik
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Főablak beállításai: cím, méret és ikon
        self.setWindowTitle('UI tutorial')
        self.setGeometry(450, 250, 800, 600)
        self.setWindowIcon(QIcon(r"Q:\#work\#prookt\240430_1_alkalom\pictures\derp.jpg"))

        # Címke létrehozása és beállítása
        label = QLabel('Ez egy label', self)
        label.setGeometry(100, 100, 100, 100)  # elhelyezkedés és méret beállítása
        label.setStyleSheet("border: 4px solid black")  # CSS stílus beállítása a keret megjelenítéséhez

        # Második címke létrehozása és beállítása képpel
        label2 = QLabel(self)
        image = QPixmap(r"Q:\#work\#prookt\240430_1_alkalom\pictures\derp.jpg")  # kép betöltése
        label2.setPixmap(image)
        label2.setGeometry(200, 200, 200, 200)  # elhelyezkedés és méret beállítása

        # Harmadik címke létrehozása és beállítása animációval
        label3 = QLabel(self)
        gif = QMovie(r"Q:\#work\#prookt\240430_1_alkalom\pictures\5612.gif")  # GIF betöltése
        label3.setGeometry(450, 450, 400, 400)  # elhelyezkedés és méret beállítása
        gif.setSpeed(100)  # animáció sebességének beállítása
        label3.setMovie(gif)  # címkehez tartozó animáció beállítása
        gif.start()  # animáció indítása

if __name__ == '__main__':
    # Alkalmazás indítása
    app = QApplication([])
    # Főablak létrehozása és megjelenítése
    window = MainWindow()
    window.show()
    # Alkalmazás főciklusának elindítása
    app.exec()