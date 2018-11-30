import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit


def r(fl):
    if fl % 1 == 0:
        return int(fl)
    return fl


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.makeUI()

    def makeUI(self):
        self.setGeometry(0, 0, 420, 390)
        self.setWindowTitle(
            "Миникалькулятор")

        self.btn = QPushButton('Рассчитать', self)
        self.btn.resize(200, 100)
        self.btn.move(110, 20)
        self.btn.clicked.connect(self.calcul)

        self.inputA = QLineEdit(self)
        self.inputA.resize(200, 100)
        self.inputA.move(7, 130)

        self.inputB = QLineEdit(self)
        self.inputB.resize(200, 100)
        self.inputB.move(214, 130)

        self.sum = QLCDNumber(self)
        self.sum.resize(92, 100)
        self.sum.move(20, 240)

        self.dif = QLCDNumber(self)
        self.dif.resize(92, 100)
        self.dif.move(116, 240)

        self.mul = QLCDNumber(self)
        self.mul.resize(92, 100)
        self.mul.move(212, 240)

        self.div = QLCDNumber(self)
        self.div.resize(92, 100)
        self.div.move(308, 240)

        self.message = QLabel(self)
        self.message.setText("")
        self.message.resize(300, 30)
        self.message.move(100, 360)

    def calcul(self):
        self.a = float(self.inputA.text())
        self.b = float(self.inputB.text())
        if self.a == 0 or self.b == 0:
            self.message.setText("Ошибка: Деление на ноль")
        else:
            self.message.setText("")
            self.sum.display(r(self.a + self.b))
            self.dif.display(r(self.a - self.b))
            self.mul.display(r(self.a * self.b))
            self.div.display(r(self.a / self.b))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = MiniCalculator()
    calc.show()
    sys.exit(app.exec())