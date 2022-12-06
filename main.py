import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from Ui_main import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, QDateTime

auto_mode = False
gongde = 0
time = 0.5
xt = "running"


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.action_auto.triggered.connect(self.mode_change_to_auto)
        self.action_no_auto.triggered.connect(self.mode_change_to_no_auto)
        self.pushButton.clicked.connect(self.button_clicked)
        self.action1_2.triggered.connect(self.clean_gongde)
        self.actiond.triggered.connect(self.show_message)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_add_gongde)
        self.timer.start(time*1000)
        self.action1.triggered.connect(self.g1)
        self.action2.triggered.connect(self.g2)
        self.action5.triggered.connect(self.g5)
        self.action5.setChecked(True)
        self.label_4.hide()
    def g1(self):
        global time
        time = 0.2
        self.action1.setChecked(True)
        self.action2.setChecked(False)
        self.action5.setChecked(False)
        self.timer.start(time*1000)
    def g2(self):
        global time
        time = 0.5
        self.action1.setChecked(False)
        self.action2.setChecked(True)
        self.action5.setChecked(False)
        self.timer.start(time*1000)
    def g5(self):
        global time
        time = 1
        self.action1.setChecked(False)
        self.action2.setChecked(False)
        self.action5.setChecked(True)
        self.timer.start(time*1000)
    def show_message(self):
        QMessageBox.about(self, "关于", "author:雪中明月\nweb:雪中明月.ml")

    def mode_change_to_auto(self):
        # 菜单模式勾选切换，木鱼按钮变灰，模式切换
        self.action_no_auto.setChecked(False)
        self.action_auto.setChecked(True)
        self.menu_3.setEnabled(True)
        self.label_4.show()
        global auto_mode
        auto_mode = True
        pass

    def mode_change_to_no_auto(self):
        self.action_no_auto.setChecked(True)
        self.action_auto.setChecked(False)
        self.menu_3.setEnabled(False)
        self.label_4.hide()
        global auto_mode
        auto_mode = False
        pass


    def clean_gongde(self):
        global gongde
        gongde = 0
        self.update_gongde()

    def auto_add_gongde(self):
        global gongde
        global xt
        xt = xt + "."
        if xt == "running........":
            xt = "running"
        self.label_4.setText(xt)
        if auto_mode == True:
            gongde = gongde + 1
            self.update_gongde()

    def update_gongde(self):
        # 刷新功德显示label
        global gongde
        self.label_3.setText(str(gongde))

    def button_clicked(self, button):
        # 木鱼点击函数
        print("功德加一")
        global gongde
        gongde = gongde + 1
        print(gongde)
        self.update_gongde()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
