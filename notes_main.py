#начни тут создавать приложение с умными заметками

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QListWidget, QInputDialog

app = QApplication([])
main_win = QWidget()

main_win.resize(700, 700)
main_win.setWindowTitle('Умные Заметки')

main_layout = QHBoxLayout()
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()

text_edit = QTextEdit()
qline_edit = QLineEdit()
qline_widget = QListWidget()
qline_widget2 = QListWidget()

text1 = QLabel('Список Заметок')
text2 = QLabel('Список Тегов')

button1 = QPushButton('Создать Заметку')
button2 = QPushButton('Удалить Заметку')
button3 = QPushButton('Сохранить Заметку')
button4 = QPushButton('Добавить к Заметке')
button5 = QPushButton('Открепить от Заметки')
button6 = QPushButton('Искать Заметки по тегу')


import json

notes = {'Добро Пожаловать!': { 'текст': 'Это лучшее приложение для заметок!', 'теги': ['инструкция']}}

with open('notes.json', 'w') as file:
    json.dump(notes, file)

qline_widget.addItems(notes)

def show_note():
    key = qline_widget.selectedItems()[0].text()
    text_edit.setText(notes[key]['текст'])
    qline_widget2.clear()
    qline_widget2.addItems(notes[key]['теги'])

def add_note():
    note_name, result = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки:')

    if result and note_name != '':
        notes[note_name] = {'текст': '', 'теги': ['']}
        qline_widget.addItem(note_name)

def del_note():
    if qline_widget.selectedItems():
        key = qline_widget.selectedItems()[0].text()
        del notes[key]
        qline_widget.clear()
        qline_widget2.clear()
        text_edit.clear()
        qline_widget.addItems(notes)
        with open ('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys = True)

def save_note():
    if qline_widget.selectedItems():
        key = qline_widget.selectedItems()[0].text()
        notes[key]['текст'] = text_edit.toPlainText()
        with open ('notes.json', 'w') as file:
            json.dump(note_name, notes, file)

def add_tag():
    if qline_widget.selectedItems():
        key = qline_widget.selectedItems()[0].text()
        tag = qline_edit.text()
        notes[key]['теги'].append(tag)
        qline_widget2.addItem(tag)
        with open ('notes.json', 'w') as file:
            json.dump(notes, file)

def del_tag():
    if qline_widget.selectedItems():
        key = qline_widget.selectedItems()[0].text()
        tag = qline_widget2.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        qline_widget2.clear()
        qline_widget2.addItems(notes[key]['теги'])

def search_tag():
    tag = qline_widget2.text()
    if button6.text() == 'Искать Заметки по тегу' and tag:
        qline_widget = qline_widget2.selectedItems()[0].text()
        for note in notes:
            if tag in notes[note]['теги']:
                qline_widget[note] = notes[note]
        button6.setText('Сбросить поиск')
        qline_widget.clear()
        qline_widget2.clear()
        qline_widget.addItems(notes_filtered)
    elif button6 == 'Сбросить поиск':
        qline_edit.clear()
        qline_widget.clear()
        qline_widget2.clear()
        qline_widget.addItems(notes)
        button6.setText('Искать Заметки по тегу')
    else:
        pass
################

button6.clicked.connect(search_tag)
button5.clicked.connect(del_tag)
button4.clicked.connect(add_tag)
button3.clicked.connect(save_note)
button2.clicked.connect(del_note)
button1.clicked.connect(add_note)
qline_widget.itemClicked.connect(show_note)


main_layout.addLayout(layout1)
main_layout.addLayout(layout2)


layout1.addWidget(text_edit)
layout2.addWidget(text1)
layout2.addWidget(qline_widget)
layout2.addWidget(button1)
layout2.addWidget(button2)
layout2.addWidget(button3)
layout2.addWidget(text2)
layout2.addWidget(qline_widget2)
layout2.addWidget(qline_edit)
layout2.addWidget(button4)
layout2.addWidget(button5)
layout2.addWidget(button6)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()


