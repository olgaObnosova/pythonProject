import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel



class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        self.setGeometry(500, 200, 500, 500)
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()
        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("вопрос блаблаблаа")
        self.label.move(80, 30)



class Window2(QWidget):

    def __init__(self):
        super(Window2, self).__init__()
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()
        self.setWindowTitle('Тест на профориентацию')
        self.setGeometry(500, 200, 500, 500)
        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("Второй вопрос блаблабла")
        self.label.move(80, 30)

class Window3(QWidget):

    def __init__(self):
        super(Window3, self).__init__()
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()
        self.setWindowTitle('вопрос №3')
        self.setGeometry(500, 200, 500, 500)
        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("третий вопрос блаблабла")
        self.label.move(80, 30)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.button.clicked.connect(self.show_window_2)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.button.clicked.connect(self.show_window_3)
        self.w2.button.clicked.connect(self.w2.close)
        self.w2.show()
    def show_window_3(self):
        self.w3 = Window3()
        #self.w1.button.clicked.connect(self.show_window_3)
        #self.w1.button.clicked.connect(self.w2.close)
        self.w3.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    #w.show()
    w.show_window_1()
    sys.exit(app.exec_())
