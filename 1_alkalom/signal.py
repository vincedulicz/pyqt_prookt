import sys

# PySide6 csomagból importáljuk az alkalmazás és az UI elemek osztályait
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import random

# Főablak osztály létrehozása, QWidget-ből származik
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Főablak beállításai: cím és méret
        self.setWindowTitle("UI tutiorál color 2") # a főablak címe
        self.setGeometry(400, 400, 600, 800) # főablak mérete + helye

        # Vízszintes elrendezés létrehozása
        vbox = QVBoxLayout()

        # Gomb létrehozása és hozzáadása a főablakhoz
        btn = QPushButton('Change text')
        self.label = QLabel("Hello")
        vbox.addWidget(btn)
        vbox.addWidget(self.label)

        # Gombhoz eseménykezelő csatolása (a feliratváltás funkció)
        btn.clicked.connect(self.change_text)

        # Elrendezés beállítása a főablakra
        self.setLayout(vbox)

    # Feliratváltó függvény definiálása
    def change_text(self):
        # Színválaszték definiálása
        color = {1: "purple", 2: "green", 3: "red"}

        # Felirat módosítása véletlenszerű szöveggel és színnel
        self.label.setText(f"I changed this: {random.randint(10, 100)}")
        self.label.setStyleSheet(f"color: {color[random.randint(1, 3)]}") # CSS stílus beállítása a szöveg színének módosításához


if __name__ == '__main__':
    # Alkalmazás indítása
    app = QApplication([])
    # Főablak létrehozása és megjelenítése
    window = MainWindow()
    window.show()
    # Alkalmazás főciklusának elindítása
    app.exec()