# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designereerAFk.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(555, 562)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonAdd = QPushButton(Form)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.verticalLayout.addWidget(self.pushButtonAdd)

        self.pushButtonEdit = QPushButton(Form)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")

        self.verticalLayout.addWidget(self.pushButtonEdit)

        self.pushButtonRemove = QPushButton(Form)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")

        self.verticalLayout.addWidget(self.pushButtonRemove)

        self.verticalSpacer = QSpacerItem(20, 298, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButtonSort = QPushButton(Form)
        self.pushButtonSort.setObjectName(u"pushButtonSort")

        self.verticalLayout.addWidget(self.pushButtonSort)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("Form", u"EDIT", None))
        self.pushButtonRemove.setText(QCoreApplication.translate("Form", u"REMOVE", None))
        self.pushButtonSort.setText(QCoreApplication.translate("Form", u"SORT", None))
    # retranslateUi

