import io
import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QDialog, QMainWindow, QFileDialog,
                             QTableWidgetItem, QLabel)

import utils
import ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.main_page)
        uic.loadUi(f, self)

        loginWindow().exec()
        if utils.user == -1:
            sys.exit()
        self.user_tickets_update()

        self.btn_update.clicked.connect(self.user_tickets_update)
        self.btn_add.clicked.connect(self.goto_create)
        self.user_table.itemSelectionChanged.connect(self.goto_edit_ticket)


        if not utils.is_user_admin():
            self.tabWidget.setTabEnabled(1, 0)
        else:
            self.categories_update()
            self.admin_tickets_update()
            self.btn_categories.clicked.connect(self.goto_categories)
            self.btn_admins.clicked.connect(self.goto_admins)
            self.cb_sorting.currentIndexChanged.connect(self.admin_tickets_update)
            self.checkBox_waiting.checkStateChanged.connect(self.admin_tickets_update)
            self.checkBox_reviewed.checkStateChanged.connect(self.admin_tickets_update)
            self.checkBox_closed.checkStateChanged.connect(self.admin_tickets_update)
            self.cb_cat_sorting.currentIndexChanged.connect(self.admin_tickets_update)
            self.btn_admin_update.clicked.connect(self.admin_tickets_update)
            self.admin_table.itemSelectionChanged.connect(self.goto_edit_ticket)

    def keyPressEvent(self, event):
        if event.Key() == Qt.Key.Key_R:
            if utils.is_user_admin():
                self.admin_tickets_update()
            self.user_tickets_update()

    def goto_edit_ticket(self):
        sender = self.sender()
        is_admin = (sender == sender.parent().parent().parent().parent().parent().admin_table)
        if is_admin:
            item = self.admin_table.selectedIndexes()
            if item:
                ticket_id = int(self.admin_table.verticalHeaderItem(item[0].row()).text())
        else:
            item = self.user_table.selectedIndexes()
            if item:
                ticket_id = int(self.user_table.verticalHeaderItem(item[0].row()).text())
        if item:
            ticket = utils.get_ticket(ticket_id)
            editTicketWindow(*ticket, admin=is_admin).exec()

    def user_tickets_update(self):
        tickets = utils.user_tickets()
        self.user_table.setColumnCount(4)
        self.user_table.setRowCount(len(tickets))
        self.user_table.setHorizontalHeaderLabels(['заголовок', 'категория',
                                                   'статус', 'изображение'])
        self.user_table.setVerticalHeaderLabels([ticket[0] for ticket in tickets])
        for i in range(len(tickets)):
            self.user_table.setItem(i, 0, QTableWidgetItem(tickets[i][1]))
            self.user_table.setItem(i, 1, QTableWidgetItem(tickets[i][2]))
            self.user_table.setItem(i, 2, QTableWidgetItem(tickets[i][3]))
            img_label = QLabel(self)
            img_label.setScaledContents(True)
            pixmap = QPixmap(tickets[i][4])
            img_label.setPixmap(pixmap)
            self.user_table.setCellWidget(i, 3, img_label)

    def admin_tickets_update(self):
        tickets = self.sorting(utils.all_tickets())
        self.admin_table.setColumnCount(5)
        self.admin_table.setRowCount(len(tickets))
        self.admin_table.setHorizontalHeaderLabels(['заголовок', 'категория', 'статус',
                                                    'пользователь', 'изображение'])
        self.admin_table.setVerticalHeaderLabels([ticket[0] for ticket in tickets])
        for i in range(len(tickets)):
            self.admin_table.setItem(i, 0, QTableWidgetItem(tickets[i][1]))
            self.admin_table.setItem(i, 1, QTableWidgetItem(tickets[i][2]))
            self.admin_table.setItem(i, 2, QTableWidgetItem(tickets[i][3]))
            self.admin_table.setItem(i, 3, QTableWidgetItem(tickets[i][4]))
            img_label = QLabel(self)
            img_label.setScaledContents(True)
            pixmap = QPixmap(tickets[i][5])
            img_label.setPixmap(pixmap)
            self.admin_table.setCellWidget(i, 4, img_label)

    def sorting(self, tickets):
        if self.cb_sorting.currentIndex() == 1:
            tickets.reverse()
        allowed_statuses = ['в обработке', 'рассмотрено', 'закрыто']
        if any([self.checkBox_waiting.isChecked(), self.checkBox_reviewed.isChecked(),
                self.checkBox_closed.isChecked()]):
            allowed_statuses = []
            if self.checkBox_waiting.isChecked():
                allowed_statuses.append('в обработке')
            if self.checkBox_reviewed.isChecked():
                allowed_statuses.append('рассмотрено')
            if self.checkBox_closed.isChecked():
                allowed_statuses.append('закрыто')
        sorted_tickets = []
        sort_by_cat = False
        if self.cb_cat_sorting.currentText() != 'все категории':
            sort_by_cat = True
        for ticket in tickets:
            if ticket[3] in allowed_statuses:
                if sort_by_cat:
                    if ticket[2] == self.cb_cat_sorting.currentText():
                        sorted_tickets.append(ticket)
                else:
                    sorted_tickets.append(ticket)
        return sorted_tickets

    def categories_update(self):
        categories = utils.get_categories()
        self.cb_cat_sorting.addItems(['все категории'] + categories)

    def goto_create(self):
        createPage().exec()

    def goto_categories(self):
        catPage().exec()

    def goto_admins(self):
        adminsPage().exec()


class loginWindow(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.login)
        uic.loadUi(f, self)

        self.btn_login.clicked.connect(self.login)
        self.btn_reg.clicked.connect(self.reg)

    def login(self):
        result = utils.login(self.username.text(), self.pas.text())
        if result == 0:
            self.close()
        elif result == 1:
            self.label_status.setText('неверный пароль')
        else:
            self.label_status.setText('неверный логин')

    def reg(self):
        if self.reg_pas.text() == self.reg_pas_confirm.text():
            result = utils.register(self.reg_username.text(), self.reg_pas.text())
            if result == 0:
                self.close()
            else:
                self.label_reg_status.setText('пользователь уже существует')
        else:
            self.label_reg_status.setText('пароли не совпадают')


class editTicketWindow(QDialog):
    def __init__(self, ticket_id, heading, description, category,
                 status, user, image, date, answer, admin=False):
        super().__init__()
        f = io.StringIO(ui.ticket_edit)
        uic.loadUi(f, self)

        self.is_admin = admin
        self.ticket_id = ticket_id
        self.status = status
        self.ans = answer
        self.admin = admin
        self.timedelta = utils.get_timedelta(date)
        print(123)

        self.heading.setReadOnly(True)
        self.heading.setText(heading)

        self.description.setReadOnly(True)
        self.description.setPlainText(description)
        print(123)

        self.label_category.setText(category)
        self.answer.setPlainText(answer)
        self.label_date.setText(self.timedelta[0])
        self.label_timer.setText(self.timedelta[1])
        self.label_user.setText(user)
        print(image)

        pixmap = QPixmap(image)
        self.label_img.setPixmap(pixmap)

        if status == 0:
            self.rb_waiting.setChecked(True)
            self.rb_waiting.setEnabled(True)
        elif status == 1:
            self.rb_reviewed.setChecked(True)
            self.rb_reviewed.setEnabled(True)
        else:
            self.rb_closed.setChecked(True)
            self.rb_closed.setEnabled(True)
        if self.admin:
            self.btn_close_cancel.setText('отменить')
            self.btn_close_cancel.clicked.connect(self.cancel)
            self.btn_delete_save.setText('сохранить')
            self.btn_delete_save.clicked.connect(self.save)
            self.answer.setReadOnly(False)
            self.rb_closed.setEnabled(True)
            self.rb_waiting.setEnabled(True)
            self.rb_reviewed.setEnabled(True)
        else:
            self.btn_close_cancel.clicked.connect(self.close_delete)
            self.btn_delete_save.clicked.connect(self.close_delete)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and \
                event.Key() == Qt.Key.Key_S and self.admin:
            self.save()
        if event.Key() == Qt.Key.Key_Escape:
            self.cancel()

    def cancel(self):
        self.close()

    def save(self):
        if self.rb_waiting.isChecked():
            status = 0
        elif self.rb_reviewed.isChecked():
            status = 1
        else:
            status = 2
        if not (status == self.status and self.ans == self.answer.toPlainText()):
            utils.update_ticket(self.ticket_id, status, self.answer.toPlainText(),
                                self.timedelta[0])
        self.close()

    def close_delete(self):
        closeDialog().exec()


class closeDialog(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.close_dialog)
        uic.loadUi(f, self)

        self.windowObj = self.sender().parent()
        self.is_delete = self.sender().text() == 'удалить'

        if self.is_delete:
            self.label.setText('Вы точно хотите удалить\nэто обращение?')

        self.btn_y.clicked.connect(self.edit_ticket)
        self.btn_n.clicked.connect(self.cancel)

    def edit_ticket(self):
        utils.manage_ticket(self.windowObj.ticket_id, self.is_delete)
        self.close()
        self.windowObj.close()

    def cancel(self):
        self.close()


class createPage(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.create)
        uic.loadUi(f, self)

        self.image = 'data\\img-placeholder.png'

        self.btn_img.clicked.connect(self.select_image)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)
        self.cb_category.addItems(utils.get_categories())
        pixmap = QPixmap(self.image)
        self.label_img.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.Key() == Qt.Key.Key_S:
            self.save()
        if event.Key() == Qt.Key.Key_Escape:
            self.cancel()

    def cancel(self):
        self.close()

    def save(self):
        utils.ticket_create(self.heading.text(), self.desc.toPlainText(),
                            self.cb_category.currentText(), self.image)
        self.close()

    def select_image(self):
        file_path = QFileDialog.getOpenFileName(self, 'Выберите изображение')
        if file_path:
            self.image = file_path[0]
        pixmap = QPixmap(self.image)
        self.label_img.setPixmap(pixmap)


class catPage(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.categories)
        uic.loadUi(f, self)

        self.categories = utils.get_categories(get_all=True)
        utils.create_connection()
        self.categories_update()

        self.btn_cat_add.clicked.connect(self.add_category)
        self.btn_cat_del.clicked.connect(self.delete_category)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.Key() == Qt.Key.Key_S:
            self.save()
        if event.Key() == Qt.Key.Key_Escape:
            self.cancel()

    def categories_update(self):
        self.table_cat.setColumnCount(1)
        self.table_cat.setRowCount(len(self.categories))
        self.table_cat.setHorizontalHeaderLabels(['категория'])
        self.table_cat.setVerticalHeaderLabels([str(data[0]) for data in self.categories])
        for i in range(len(self.categories)):
            self.table_cat.setItem(i, 0, QTableWidgetItem(self.categories[i][1]))

    def add_category(self):
        if self.cat_name.text() and \
                self.cat_name.text() not in [data[1] for data in self.categories]:
            result = utils.add_category(self.cat_name.text())
            self.categories.append(result)
            self.categories_update()
            self.label.setText('')
        else:
            self.label.setText('такая категория уже существует!')

    def delete_category(self):
        items = self.table_cat.selectedItems()
        for item in items:
            utils.delete_category(item.text())
            del self.categories[[data[1] for data in self.categories].index(item.text())]
        self.categories_update()

    def cancel(self):
        utils.cancel_connection()
        self.close()

    def save(self):
        utils.commit_connection()

        self.close()


class adminsPage(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui.admins)
        uic.loadUi(f, self)

        self.admins = utils.get_admins()
        utils.create_connection()
        self.admins_update()

        self.btn_admin_add.clicked.connect(self.add_admin)
        self.btn_admin_del.clicked.connect(self.delete_admin)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.save)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.Key() == Qt.Key.Key_S:
            self.save()
        if event.Key() == Qt.Key.Key_Escape:
            self.cancel()

    def admins_update(self):
        self.table_admins.setColumnCount(1)
        self.table_admins.setRowCount(len(self.admins))
        self.table_admins.setHorizontalHeaderLabels(['username'])
        self.table_admins.setVerticalHeaderLabels([str(data[0]) for data in self.admins])
        for i in range(len(self.admins)):
            self.table_admins.setItem(i, 0, QTableWidgetItem(self.admins[i][1]))

    def add_admin(self):
        if self.user_login.text() and \
                self.user_login.text() not in [data[1] for data in self.admins]:
            result = utils.add_admin(self.user_login.text())
            self.admins.append(result)
            self.admins_update()
            self.label.setText('')
        else:
            self.label.setText('этот пользователь уже администратор')

    def delete_admin(self):
        items = self.table_admins.selectedItems()
        for item in items:
            utils.delete_admin(item.text())
            del self.admins[[data[1] for data in self.admins].index(item.text())]
        self.admins_update()

    def cancel(self):
        utils.cancel_connection()
        self.close()

    def save(self):
        utils.commit_connection()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


def printt(s):
    print(s)
