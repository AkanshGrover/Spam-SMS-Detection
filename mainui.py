from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(487, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_ip = QTextEdit(self.centralwidget)
        self.message_ip.setObjectName(u"message_ip")
        self.message_ip.setFrameShape(QFrame.NoFrame)
        self.message_ip.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.message_ip)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.check_btn = QPushButton(self.centralwidget)
        self.check_btn.setObjectName(u"check_btn")

        self.horizontalLayout.addWidget(self.check_btn)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout.addWidget(self.clear_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scam or ham", None))
        self.message_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter message here", None))
        self.check_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

