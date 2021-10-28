import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*

result = 0
btn_text = 0

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Тест на профориентацию')
        self.setGeometry(500, 200, 500, 500)
        self.first_window()

    def first_window(self):

        global btn_text
        btn_text = 1
        self.my_text = QLineEdit(self)
        self.my_text.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text.move(100, 100)
        self.my_text.setFixedWidth(301)

        self.my_text1 = QtWidgets.QLineEdit(self)
        self.my_text1.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text1.move(100, 120)
        self.my_text1.setFixedWidth(301)

        self.my_text2 = QtWidgets.QLineEdit(self)
        self.my_text2.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text2.move(100, 140)
        self.my_text2.setFixedWidth(301)

        self.my_text3 = QtWidgets.QLineEdit(self)
        self.my_text3.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text3.move(100, 160)
        self.my_text3.setFixedWidth(301)

        self.my_text4 = QtWidgets.QLineEdit(self)
        self.my_text4.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text4.move(100, 180)
        self.my_text4.setFixedWidth(301)

        self.my_text5 = QtWidgets.QLineEdit(self)
        self.my_text5.setText('Это базовая надписьmnnnnnnnблаблаблаблабалблаблаблаблабла')
        self.my_text5.move(100, 200)
        self.my_text5.setFixedWidth(301)

        self.btn = QPushButton('Далее', self)
        self.btn.setToolTip('Для перехода к началу теста нажмите <b>"Далее"</b>')
        self.btn.resize(100, 50)
        self.btn.move(370, 420)
        self.btn.clicked.connect(self.my_text.clear)
        self.btn.clicked.connect(self.my_text1.clear)
        self.btn.clicked.connect(self.my_text2.clear)
        self.btn.clicked.connect(self.my_text3.clear)
        self.btn.clicked.connect(self.my_text4.clear)
        self.btn.clicked.connect(self.my_text5.clear)

        self.btn.setStyleSheet("QPushButton { background-color: rgb(36, 255, 215) }")
        self.btn.clicked.connect(self.vopros_1)

    def vopros_1(self):

        self.radiobutton_1_1 = QRadioButton('В прошлое')
        self.radiobutton_2_1 = QRadioButton('В будущее')
        self.radiobutton_3_1 = QRadioButton('Я бы продал эту возможность')
        self.radiobutton_4_1 = QRadioButton('В новые места, а не во времени')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('1. Ecли бы у вас был доступ к машине времени, вы бы предпочли отправиться:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_2)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_2(self):
        self.radiobutton_1_1 = QRadioButton('Предоставить доступ к вашим соцсетям второму лицу')
        self.radiobutton_2_1 = QRadioButton('Ездить в отпуск в одно и то же место')
        self.radiobutton_3_1 = QRadioButton('Позволить кому-то подберать вам одежду в течении месяца')
        self.radiobutton_4_1 = QRadioButton('Раздражающий коллега будет назначен вашим боссом')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('2. Какая идея кажется вам наихудшей?:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_3())

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_3(self):
        self.radiobutton_1_1 = QRadioButton('Решаете техническую проблему')
        self.radiobutton_2_1 = QRadioButton('Решаете проблему друга')
        self.radiobutton_3_1 = QRadioButton('Выступаете на сцене')
        self.radiobutton_4_1 = QRadioButton('Что-то создаете')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('3. Вы чувствуете себя счастливее всего, когда:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_4)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_4(self):
        self.radiobutton_1_1 = QRadioButton('Посмотрю что можно приготовить')
        self.radiobutton_2_1 = QRadioButton('Срочно за уборку!')
        self.radiobutton_3_1 = QRadioButton('Выберу правильную музыку')
        self.radiobutton_4_1 = QRadioButton('Гости? Я так не думаю')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('4. Ваши друзья будут у вас серез 30 минут. Ваши действия:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_5)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_5(self):
        self.radiobutton_1_1 = QRadioButton('Машинки с резиновыми бамперами')
        self.radiobutton_2_1 = QRadioButton('Американские горки')
        self.radiobutton_3_1 = QRadioButton('Карусели')
        self.radiobutton_4_1 = QRadioButton('Я бы поменял свой приз на материалы для творчества')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('5. Вы только что выиграли неограниченный доступ на ваш любимый атракцион '
                                    'в парке развлечений. Что же это будет?:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_6)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_6(self):
        self.radiobutton_1_1 = QRadioButton('Тренажерный зал')
        self.radiobutton_2_1 = QRadioButton('Никаких тренировок!')
        self.radiobutton_3_1 = QRadioButton('Йога - это жизнь')
        self.radiobutton_4_1 = QRadioButton('Я бегаю')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('6. Ваша идеальная тренировка:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_7)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_7(self):
        self.radiobutton_1_1 = QRadioButton('У меня нет на это времени!')
        self.radiobutton_2_1 = QRadioButton('Не более 1 часа')
        self.radiobutton_3_1 = QRadioButton('Около 3 часов')
        self.radiobutton_4_1 = QRadioButton('24/7')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('7. Сколько времени вы ежедневно проводите в социальных сетях:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_8)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_8(self):
        self.radiobutton_1_1 = QRadioButton('Я много пишу о себе')
        self.radiobutton_2_1 = QRadioButton('В основном я просто прокручиваю ленту')
        self.radiobutton_3_1 = QRadioButton('Я выкладываю мемы и новости')
        self.radiobutton_4_1 = QRadioButton('Ничем таким я не занимаюсь')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('8. Что из этого больше всего похоже на ваше поведение в социальных сетях:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_9)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_9(self):
        self.radiobutton_1_1 = QRadioButton('Лес. Нетронутая природа')
        self.radiobutton_2_1 = QRadioButton('Трасса с большим колличеством машин')
        self.radiobutton_3_1 = QRadioButton('Оживленная улица')
        self.radiobutton_4_1 = QRadioButton('Поле в грозу')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('9. Выберите образ, который больше всего вам подходит:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_10)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_10(self):
        self.radiobutton_1_1 = QRadioButton('Зеленые')
        self.radiobutton_2_1 = QRadioButton('Серые')
        self.radiobutton_3_1 = QRadioButton('Разноцветные')
        self.radiobutton_4_1 = QRadioButton('Голубые')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('10. Вы решили перекрасить стены в своей комнате. Теперь они будут:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_11)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_11(self):
        self.radiobutton_1_1 = QRadioButton('Абстрактный и простой рисунок')
        self.radiobutton_2_1 = QRadioButton('Любимая цитата')
        self.radiobutton_3_1 = QRadioButton('Фотоколлаж')
        self.radiobutton_4_1 = QRadioButton('Что-то связанное с работой')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('11. Пора что-нибудь сделать с этой пустой и голой стеной. Вы предпочитаете:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_12)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_12(self):
        self.radiobutton_1_1 = QRadioButton('Дизайнерская одежда')
        self.radiobutton_2_1 = QRadioButton('Вечеринка!')
        self.radiobutton_3_1 = QRadioButton('Частный самолет')
        self.radiobutton_4_1 = QRadioButton('Инвестиции')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('12. На работе вам только что выдали неожиданный бонус. Как вы его потратите:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_13)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_13(self):
        self.radiobutton_1_1 = QRadioButton('Собственный большой кабинет или мастерская')
        self.radiobutton_2_1 = QRadioButton('Зона отдыха')
        self.radiobutton_3_1 = QRadioButton('Офисный кубик')
        self.radiobutton_4_1 = QRadioButton('Любимая кофейня')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('13. Опишите ваше идеальное рабочее помещение:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_14)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_14(self):
        self.radiobutton_1_1 = QRadioButton('Злодей мирового класса')
        self.radiobutton_2_1 = QRadioButton('Неизвестный герой')
        self.radiobutton_3_1 = QRadioButton('Самый счастливый, но бедный')
        self.radiobutton_4_1 = QRadioButton('Богатый, но всегда одинокий')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('14. Кем из них вы предпочли бы быть:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.vopros_15)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def vopros_15(self):
        self.radiobutton_1_1 = QRadioButton('Брауни')
        self.radiobutton_2_1 = QRadioButton('Пломбир')
        self.radiobutton_3_1 = QRadioButton('Салат')
        self.radiobutton_4_1 = QRadioButton('Фруктовый торт')

        self.qestion_text_1 = QtWidgets.QLabel(self)
        self.qestion_text_1.setText('15. Ваш идеальный десерт:')
        self.qestion_text_1.move(10, 10)
        self.qestion_text_1.setFixedWidth(480)
        self.qestion_text_1.show()

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.radiobutton_1_1)
        self.button_group_1.addButton(self.radiobutton_2_1)
        self.button_group_1.addButton(self.radiobutton_3_1)
        self.button_group_1.addButton(self.radiobutton_4_1)

        self.button_group_1.buttonClicked.connect(self.radio_button_clicked_1)

        self.btn_1 = QPushButton('Далее', self)
        self.btn_1.setToolTip('Для перехода к следующему вопросу нажмите <b>"Далее"</b>')
        self.btn_1.resize(100, 50)
        self.btn_1.move(350, 400)
        self.btn_1.clicked.connect(self.last_w)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.radiobutton_1_1)
        layout_1.addWidget(self.radiobutton_2_1)
        layout_1.addWidget(self.radiobutton_3_1)
        layout_1.addWidget(self.radiobutton_4_1)
        layout_1.addWidget(self.btn_1)
        self.setLayout(layout_1)

    def last_w(self):
        pass

    def radio_button_clicked_1(self, button):
        print(button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())

