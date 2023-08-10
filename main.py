from PyQt5.QtWidgets import *
import random


app = QApplication([])

window = QWidget()
window.resize(500, 500)

firstText = QLabel("Тицни, щоби дізнатися переможця!")
twoText = QLabel("Переможець")
knopkf = QPushButton("Визначити переможця")


line = QVBoxLayout()
line.addWidget(firstText)


line.addWidget(twoText)
line.addWidget(knopkf)

window.setLayout(line)

def winner():
    a = str(random.randint(0, 100))
    twoText.setText(a)


knopkf.clicked.connect(winner)

window.show()

app.exec()

коментар для завдання 
