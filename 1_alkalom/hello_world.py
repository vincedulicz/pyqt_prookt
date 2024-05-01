import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

# Főablak osztály létrehozása, QMainWindow-ból származik
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Főablak címének beállítása
        self.setWindowTitle("My First PyQt6 Application")

        # Címke létrehozása és beállítása a főablakhoz
        self.label = QLabel("Hello, PyQt6!", self)
        self.label.setGeometry(100, 50, 200, 50)  # x, y, width, height

        # Főablak méretének és elhelyezkedésének beállítása
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height

# Főprogram függvény
def main():
    # Alkalmazás létrehozása
    app = QApplication(sys.argv)
    # Főablak létrehozása és megjelenítése
    window = MyWindow()
    window.show()
    # Alkalmazás futtatása
    sys.exit(app.exec())

# Főprogram indítása, ha ez a fájl kerül közvetlenül futtatásra
if __name__ == "__main__":
    main()
