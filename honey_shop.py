import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

class OrderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Оформление заказа")

        self.name_edit = QLineEdit(self)
        self.surname_edit = QLineEdit(self)
        self.address_edit = QLineEdit(self)
        self.quantity_edit = QLineEdit(self)

        form_layout = QFormLayout()
        form_layout.addRow("Имя:", self.name_edit)
        form_layout.addRow("Фамилия:", self.surname_edit)
        form_layout.addRow("Место доставки:", self.address_edit)
        form_layout.addRow("Количество:", self.quantity_edit)

        self.accept_button = QPushButton("Оформить", self)
        self.cancel_button = QPushButton("Отмена", self)

        self.accept_button.clicked.connect(self.accept_order)
        self.cancel_button.clicked.connect(self.reject_order)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.accept_button)
        button_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def accept_order(self):
        name = self.name_edit.text()
        surname = self.surname_edit.text()
        address = self.address_edit.text()
        quantity = self.quantity_edit.text()

        # Генерация случайного номера заказа
        order_number = random.randint(1000000, 9999999)

        # Здесь можно добавить логику для обработки заказа, например, отправку данных на сервер
        # и дополнительные проверки ввода

        QMessageBox.information(self, "Спасибо за заказ", f"Ваш заказ оформлен. Номер заказа: {order_number}")
        self.accept()

    def reject_order(self):
        self.reject()

class HoneyStoreApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Магазин мёда')

        self.honey_image_label = QLabel(self)
        self.image_paths = ['image_1.png', 'image_2.png', 'image_3.png', 'image_4.png', 'image_5.png', 'image_6.png']
        self.current_image_index = 0
        self.image_labels = {
            'image_1.png': 'Акациевый мёд',
            'image_2.png': 'Гречишный мёд',
            'image_3.png': 'Вересковый мёд',
            'image_4.png': 'Лесной мёд',
            'image_5.png': 'Липовый мёд',
            'image_6.png': 'Малиновый мёд'
        }

        self.image_label = QLabel(self.image_labels[self.image_paths[self.current_image_index]], self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.prev_button = QPushButton('<<', self)
        self.order_button = QPushButton('Заказать мёд', self)
        self.next_button = QPushButton('>>', self)

        self.prev_button.clicked.connect(self.show_prev_image)
        self.next_button.clicked.connect(self.show_next_image)
        self.order_button.clicked.connect(self.show_order_dialog)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.order_button)
        button_layout.addWidget(self.next_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.honey_image_label, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        layout.addLayout(button_layout)

        description_layout = QVBoxLayout()

        self.description_label = QLabel(self)
        description_layout.addWidget(self.description_label, alignment=Qt.AlignCenter)

        layout.addLayout(description_layout)
        layout.setAlignment(Qt.AlignCenter)

        self.update_image()

    def update_image(self):
        pixmap = QPixmap(self.image_paths[self.current_image_index])
        pixmap = pixmap.scaledToWidth(500)
        self.honey_image_label.setPixmap(pixmap)

        self.image_label.setText(self.image_labels[self.image_paths[self.current_image_index]])

        self.prev_button.setEnabled(self.current_image_index > 0)
        self.next_button.setEnabled(self.current_image_index < len(self.image_paths) - 1)

        self.update_description()

    def update_description(self):
        current_honey = self.image_labels[self.image_paths[self.current_image_index]]
        if current_honey == 'Акациевый мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.8 г\n"\
                            "жиры - 0 г\n"\
                            "углеводы - 74.8 г\n"\
                            "калорийность - 308 ккал/100 г\n"\
                            "банка - 100г"
        elif current_honey == 'Гречишный мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.5 г\n"\
                            "жиры - 0 г\n"\
                            "углеводы - 76.8 г\n"\
                            "калорийность - 309 ккал/100 г\n"\
                            "банка - 100г"
        elif current_honey == 'Вересковый мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.5 г\n"\
                            "жиры - 0 г\n"\
                            "углеводы - 78 г\n"\
                            "калорийность - 314 ккал\n"\
                            "банка - 100г"
        elif current_honey == 'Лесной мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.35 г\n"\
                            "жиры - 0.1 г\n"\
                            "углеводы - 81.38 г\n"\
                            "калорийность - 311.67 ккал/100 г\n"\
                            "банка - 100г"
        elif current_honey == 'Липовый мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.69 г\n"\
                            "жиры - 0.01 г\n"\
                            "углеводы - 78.44 г\n"\
                            "калорийность - 312.61 ккал/100 г\n"\
                            "банка - 100г"
        elif current_honey == 'Малиновый мёд':
            description =   "Пищевая и энергетическая ценность:\n"\
                            "белки - 0.84 г\n"\
                            "жиры - 0 г\n"\
                            "углеводы - 98.5 г\n"\
                            "калорийность - 394 ккал/100 г\n"\
                            "банка - 100г"

        self.description_label.setText(description)

    def show_prev_image(self):
        self.current_image_index = max(0, self.current_image_index - 1)
        self.update_image()

    def show_next_image(self):
        self.current_image_index = min(len(self.image_paths) - 1, self.current_image_index + 1)
        self.update_image()

    def show_order_dialog(self):
        order_dialog = OrderDialog(self)
        order_dialog.exec_()

    def place_order(self):
        print('Заказ мёда размещен!')


window = HoneyStoreApp()
window.showMaximized()
sys.exit(app.exec_())