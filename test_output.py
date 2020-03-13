# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktopAppTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 10, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lcd_temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_temp.setGeometry(QtCore.QRect(330, 62, 161, 61))
        self.lcd_temp.setObjectName("lcd_temp")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(240, 40, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_temp.setPalette(palette)
        self.label_temp.setObjectName("label_temp")
        self.label_humid = QtWidgets.QLabel(self.centralwidget)
        self.label_humid.setGeometry(QtCore.QRect(250, 140, 47, 13))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_humid.setPalette(palette)
        self.label_humid.setObjectName("label_humid")
        self.lcd_humid = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_humid.setGeometry(QtCore.QRect(330, 160, 161, 61))
        self.lcd_humid.setObjectName("lcd_humid")
        self.lcd_light_exposure = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_light_exposure.setGeometry(QtCore.QRect(330, 250, 161, 61))
        self.lcd_light_exposure.setObjectName("lcd_light_exposure")
        self.label_light_exposure = QtWidgets.QLabel(self.centralwidget)
        self.label_light_exposure.setGeometry(QtCore.QRect(230, 230, 71, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_light_exposure.setPalette(palette)
        self.label_light_exposure.setObjectName("label_light_exposure")
        self.label_app = QtWidgets.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(100, 10, 181, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_app.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_app.setFont(font)
        self.label_app.setObjectName("label_app")
        self.time_example_1 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.time_example_1.setGeometry(QtCore.QRect(10, 70, 194, 21))
        self.time_example_1.setObjectName("time_example_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 2, 531, 311))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("joseph-barrientos-KV7n8nARXng-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.comboBoxX = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxX.setGeometry(QtCore.QRect(10, 110, 69, 22))
        self.comboBoxX.setObjectName("comboBoxX")
        self.comboBoxX.addItem("")
        self.comboBoxX.addItem("")
        self.comboBoxY = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxY.setGeometry(QtCore.QRect(90, 110, 69, 22))
        self.comboBoxY.setObjectName("comboBoxY")
        self.comboBoxY.addItem("")
        self.comboBoxY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.submit.setObjectName("submit")
        self.label_xor_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xor_result.setGeometry(QtCore.QRect(100, 150, 47, 21))
        self.label_xor_result.setObjectName("label_xor_result")
        self.label.raise_()
        self.progressBar.raise_()
        self.lcd_temp.raise_()
        self.label_temp.raise_()
        self.label_humid.raise_()
        self.lcd_humid.raise_()
        self.lcd_light_exposure.raise_()
        self.label_light_exposure.raise_()
        self.label_app.raise_()
        self.time_example_1.raise_()
        self.comboBoxX.raise_()
        self.comboBoxY.raise_()
        self.submit.raise_()
        self.label_xor_result.raise_()
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionPaste.setObjectName("actionPaste")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        
        #triggered is like clicked but accounts for keyboard short cuts
        #lambda stands for a function that is defined on one line and takes a cb
        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionSave.triggered.connect(self.show_popup)


    #     self.comboBoxX.addItem("Hello")
    # #change default
    #     index = self.comboBoxX.findText("1", QtCore.Qt.MatchFixedString) 
    #     self.comboBoxX.setCurrentIndex(index)

        self.submit.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_temp.setText(_translate("MainWindow", "temperature"))
        self.label_humid.setText(_translate("MainWindow", "humidity"))
        self.label_light_exposure.setText(_translate("MainWindow", "light exposure"))
        self.label_app.setText(_translate("MainWindow", "SENSORS"))
        self.comboBoxX.setItemText(0, _translate("MainWindow", "0"))
        self.comboBoxX.setItemText(1, _translate("MainWindow", "1"))
        self.comboBoxY.setItemText(0, _translate("MainWindow", "0"))
        self.comboBoxY.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit XOR"))
        self.label_xor_result.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy selected element"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))

        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste copied element"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))

        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def clicked(self, text):
        self.label_app.setText(text)
        self.label_app.adjustSize()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Save file")
        msg.setText("Do you want to save this file?")
        msg.setIcon(QMessageBox.Question) #Critical, warning, Information
        msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel) #Ok, Open, Save, Cancel, Close, Yes No, Abort, Retry, Ignore
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText("really? in this condition???")

        msg.setDetailedText("details")

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self, button_passed):
        print(button_passed.text())


    def pressed(self):
        x = int(self.comboBoxX.currentText())
        y = int(self.comboBoxY.currentText())
        xor = (x and not y) or (not x and y)
        if xor == True:
            xor = 1
        else:
            xor = 0

        self.label_xor_result.setText(str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
