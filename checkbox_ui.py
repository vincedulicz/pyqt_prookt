# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerWYSECV.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(617, 478)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPrize = QLabel(Form)
        self.labelPrize.setObjectName(u"labelPrize")

        self.horizontalLayout.addWidget(self.labelPrize)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSelect = QLabel(Form)
        self.labelSelect.setObjectName(u"labelSelect")

        self.horizontalLayout_2.addWidget(self.labelSelect)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBoxCheese = QCheckBox(Form)
        self.checkBoxCheese.setObjectName(u"checkBoxCheese")

        self.verticalLayout.addWidget(self.checkBoxCheese)

        self.checkBoxBacon = QCheckBox(Form)
        self.checkBoxBacon.setObjectName(u"checkBoxBacon")

        self.verticalLayout.addWidget(self.checkBoxBacon)

        self.checkBoxCola = QCheckBox(Form)
        self.checkBoxCola.setObjectName(u"checkBoxCola")

        self.verticalLayout.addWidget(self.checkBoxCola)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.labelTotal = QLabel(Form)
        self.labelTotal.setObjectName(u"labelTotal")

        self.verticalLayout_2.addWidget(self.labelTotal)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelPrize.setText(QCoreApplication.translate("Form", u"Pizza Prize", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"$ 10", None))
        self.labelSelect.setText(QCoreApplication.translate("Form", u"Select Extra", None))
        self.checkBoxCheese.setText(QCoreApplication.translate("Form", u"Extra Cheese 1$", None))
        self.checkBoxBacon.setText(QCoreApplication.translate("Form", u"Extra Bacon 2$", None))
        self.checkBoxCola.setText(QCoreApplication.translate("Form", u"Extra Cola 1$", None))
        self.labelTotal.setText(QCoreApplication.translate("Form", u"Total: $", None))
    # retranslateUi


