import sys

# PySide6 csomagból importáljuk az alkalmazás, a widgetek és a címkék osztályait, valamint a kép- és animációkezelő osztályokat
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap, QMovie

# Főablak osztály létrehozása, QWidget-ből származik
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Főablak beállításai: cím, méret és ikon
        self.setWindowTitle('UI tutorriál')
        self.setGeometry(400, 20, 800, 600)
        self.setWindowIcon(QIcon(r"Q:\#work\#prookt\240430_1_alkalom\pictures\derp.jpg"))

        # Egy szöveges címke létrehozása és beállítása
        label = QLabel("ez itt egy label", self)
        label.setGeometry(100, 120, 100, 120)  # elhelyezkedés és méret beállítása
        label.setStyleSheet("border: 4px solid black")  # CSS stílus beállítása a keret megjelenítéséhez

        # Egy címke létrehozása és beállítása képpel
        label_picture = QLabel(self)
        image = QPixmap(r"Q:\#work\#prookt\240430_1_alkalom\pictures\derp.jpg")  # kép betöltése
        label_picture.setPixmap(image)
        label_picture.setGeometry(200, 200, 200, 200)  # elhelyezkedés és méret beállítása

        # Egy címke létrehozása és beállítása animációval
        label_gif = QLabel(self)
        gif = QMovie(r"Q:\#work\#prookt\240430_1_alkalom\pictures\5612.gif")  # GIF betöltése
        label_gif.setGeometry(200, 200, 200, 200)  # elhelyezkedés és méret beállítása
        gif.setSpeed(100)  # animáció sebességének beállítása
        label_gif.setMovie(gif)  # címkehez tartozó animáció beállítása
        gif.start()  # animáció indítása


if __name__=='__main__':
    # Alkalmazás indítása
    app = QApplication([])
    # Főablak létrehozása és megjelenítése
    window = MainWindow()
    window.show()
    # Alkalmazás főciklusának elindítása
    app.exec()