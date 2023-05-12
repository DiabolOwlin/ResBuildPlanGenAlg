# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMinimumSize(QSize(37, 0))
        self.side_menu_container.setMaximumSize(QSize(37, 16777215))
        self.side_menu_container.setStyleSheet(u"QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"}\n"
"QPushButton{\n"
"background-color: transparent;\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 2px solid transparent;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"\n"
"")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.side_menu_container.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.side_menu_container)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(37, 0))
        self.side_menu.setMaximumSize(QSize(37, 16777215))
        self.side_menu.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.side_menu.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.app_name_frame = QFrame(self.side_menu)
        self.app_name_frame.setObjectName(u"app_name_frame")
        self.app_name_frame.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.app_name_frame.setFrameShape(QFrame.StyledPanel)
        self.app_name_frame.setFrameShadow(QFrame.Raised)
        self.app_name_frame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.app_name_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 6, 0, 0)
        self.app_icon = QLabel(self.app_name_frame)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy)
        self.app_icon.setLineWidth(0)
        self.app_icon.setPixmap(QPixmap(u":/icons/icons/cil-airplane-mode-off.png"))
        self.app_icon.setScaledContents(False)
        self.app_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.app_icon, 0, Qt.AlignLeft|Qt.AlignTop)

        self.app_name = QLabel(self.app_name_frame)
        self.app_name.setObjectName(u"app_name")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"QLabel{\n"
"color: #fff;\n"
"margin-left: 20px\n"
"}")
        self.app_name.setLineWidth(0)
        self.app_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.app_name, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.app_name_frame)

        self.menu = QFrame(self.side_menu)
        self.menu.setObjectName(u"menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy1)
        self.menu.setStyleSheet(u"")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.menu)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(12, 15, 0, 0)
        self.Show_hide_button = QPushButton(self.menu)
        self.Show_hide_button.setObjectName(u"Show_hide_button")
        self.Show_hide_button.setEnabled(True)
        self.Show_hide_button.setMinimumSize(QSize(12, 12))
        self.Show_hide_button.setMaximumSize(QSize(12, 12))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Show_hide_button.setIcon(icon)
        self.Show_hide_button.setIconSize(QSize(12, 12))
        self.Show_hide_button.setFlat(False)

        self.verticalLayout_6.addWidget(self.Show_hide_button)

        self.home_button = QPushButton(self.menu)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(12, 12))
        self.home_button.setMaximumSize(QSize(12, 12))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(12, 12))

        self.verticalLayout_6.addWidget(self.home_button)

        self.new_button = QPushButton(self.menu)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setMinimumSize(QSize(12, 12))
        self.new_button.setMaximumSize(QSize(12, 12))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_button.setIcon(icon2)
        self.new_button.setIconSize(QSize(12, 12))

        self.verticalLayout_6.addWidget(self.new_button)

        self.save_button = QPushButton(self.menu)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(12, 12))
        self.save_button.setMaximumSize(QSize(12, 12))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon3)
        self.save_button.setIconSize(QSize(12, 12))

        self.verticalLayout_6.addWidget(self.save_button)

        self.exit_button = QPushButton(self.menu)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(12, 12))
        self.exit_button.setMaximumSize(QSize(12, 12))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon4)
        self.exit_button.setIconSize(QSize(12, 12))

        self.verticalLayout_6.addWidget(self.exit_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.menu)

        self.settings_frame = QFrame(self.side_menu)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}\n"
"")
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 0, 0, 9)
        self.settings_button = QPushButton(self.settings_frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(12, 12))
        self.settings_button.setMaximumSize(QSize(12, 12))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon5)
        self.settings_button.setIconSize(QSize(12, 12))

        self.verticalLayout_7.addWidget(self.settings_button, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.settings_frame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.side_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"QFrame{\n"
"background-color: rgb(40, 44, 52);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.main_body.setLineWidth(5)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.main_body)
        self.header.setObjectName(u"header")
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet(u"QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"border: none;\n"
"}\n"
"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_frame = QFrame(self.header)
        self.close_frame.setObjectName(u"close_frame")
        self.close_frame.setStyleSheet(u"QFrame{\n"
"margin: 6px 6px 6px 6px;\n"
"border: none;\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton: hover { \n"
"background-color: rgb(44, 49, 57);\n"
"border-style: solid;\n"
"border-radius: 4px; \n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"background-color: rgb(23, 26, 30);\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.close_frame.setFrameShape(QFrame.StyledPanel)
        self.close_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.close_frame)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.close_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setMaximumSize(QSize(16, 16))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.close_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16, 16))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.close_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16, 16))
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.close_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.main_body_content = QFrame(self.main_body)
        self.main_body_content.setObjectName(u"main_body_content")
        sizePolicy1.setHeightForWidth(self.main_body_content.sizePolicy().hasHeightForWidth())
        self.main_body_content.setSizePolicy(sizePolicy1)
        self.main_body_content.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}")
        self.main_body_content.setFrameShape(QFrame.StyledPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_body_content)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 7px;\n"
"color: rgb(113, 126, 149);\n"
"padding: 3px 10px 3px 10px;\n"
"}")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.author_label = QLabel(self.frame_4)
        self.author_label.setObjectName(u"author_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        self.author_label.setFont(font1)
        self.author_label.setStyleSheet(u"QLabel{\n"
"color: #fff;\n"
"}")

        self.verticalLayout_4.addWidget(self.author_label, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version_label_2 = QLabel(self.frame_5)
        self.version_label_2.setObjectName(u"version_label_2")

        self.verticalLayout_5.addWidget(self.version_label_2, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignVCenter)

        self.header.raise_()
        self.footer.raise_()
        self.main_body_content.raise_()

        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_icon.setText("")
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"ArchitEvo", None))
        self.Show_hide_button.setText("")
        self.home_button.setText("")
        self.new_button.setText("")
        self.save_button.setText("")
        self.exit_button.setText("")
        self.settings_button.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.author_label.setText(QCoreApplication.translate("MainWindow", u"By: Andrii Banyk", None))
        self.version_label_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

