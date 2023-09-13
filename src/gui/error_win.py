import datetime
import os
from PySide6.QtCore import (
    QCoreApplication, QLocale, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QMainWindow, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QTextEdit, QWidget, QFileDialog)
import util.constant as Const


class ErrorWindow(QMainWindow):

    def __init__(self, exception_text=None):
        super().__init__()
        self._exception_text = exception_text
        self._create_controls(self)

    def _create_controls(self, Frame: QMainWindow):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")

        Frame.setMinimumSize(QSize(460, 460))
        Frame.setMaximumSize(QSize(460, 460))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMaximumSize(QSize(460, 460))
        icon = QIcon(QIcon.fromTheme(u"error"))
        Frame.setWindowIcon(icon)
        Frame.setWindowFilePath(u"")
        self.gridLayoutWidget = QWidget(Frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 460, 460))
        self.main_layout = QGridLayout(self.gridLayoutWidget)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(10, 5, 10, 20)
        self.vertSpacer2 = QSpacerItem(
            5, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertSpacer2, 3, 0, 1, 1)

        self.vertSpace3 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertSpace3, 5, 0, 1, 1)

        self.textLog = QTextEdit(self.gridLayoutWidget)
        self.textLog.setObjectName(u"textLog")
        self.textLog.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textLog.setText(self._exception_text)
        self.textLog.setLineWidth(2)
        self.textLog.setReadOnly(True)

        self.main_layout.addWidget(self.textLog, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSaveLog = QPushButton(self.gridLayoutWidget)
        self.btnSaveLog.setObjectName(u"btnSaveLog")
        self.btnSaveLog.setText(u"btnSaveLog")
        self.btnSaveLog.setMinimumHeight(40)
        self.btnSaveLog.clicked.connect(self._btnSaveLog_click)
        self.horizontalLayout.addWidget(self.btnSaveLog)

        self.horizontalSpacer = QSpacerItem(
            30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCloseApp = QPushButton(self.gridLayoutWidget)
        self.btnCloseApp.setObjectName(u"btnCloseApp")
        self.btnCloseApp.setText(u"btnCloseApp")
        self.btnCloseApp.setMinimumHeight(40)
        self.btnCloseApp.clicked.connect(self.close)
        self.horizontalLayout.addWidget(self.btnCloseApp)

        self.main_layout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.lblDesc = QLabel(self.gridLayoutWidget)
        self.lblDesc.setObjectName(u"lblDesc")
        self.lblDesc.setMaximumSize(QSize(460, 460))

        self.lblDesc.setLineWidth(1)
        self.lblDesc.setText(u"lblDesc")
        self.lblDesc.setTextFormat(Qt.PlainText)
        self.lblDesc.setWordWrap(True)
        self.lblDesc.setMargin(0)

        self.main_layout.addWidget(self.lblDesc, 2, 0, 1, 1)

        self.vertSpacer1 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertSpacer1, 1, 0, 1, 1)

        self.lblNmApp = QLabel(self.gridLayoutWidget)
        self.lblNmApp.setObjectName(u"lblNmApp")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblNmApp.setFont(font)

        self.lblNmApp.setText(Const.NM_APP)
        self.lblNmApp.setTextFormat(Qt.PlainText)
        self.lblNmApp.setTextInteractionFlags(Qt.NoTextInteraction)

        self.main_layout.addWidget(self.lblNmApp, 0, 0, 1, 1)

        self.setLangApp(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def setLangApp(self, Frame):
        self._lang_app = "en"

        if QLocale.system().name() == "pt_BR":
            self._lang_app = "pt"

        lblDesc = next(
            txt[self._lang_app] for txt in Const.TXTS_ERROR_WIN if txt["text"] == "lblDesc")
        btnCloseApp = next(
            txt[self._lang_app] for txt in Const.TXTS_ERROR_WIN if txt["text"] == "btnCloseApp")
        btnSaveLog = next(
            txt[self._lang_app] for txt in Const.TXTS_ERROR_WIN if txt["text"] == "btnSaveLog")

        self.lblDesc.setText(lblDesc)
        self.btnCloseApp.setText(btnCloseApp)
        self.btnSaveLog.setText(btnSaveLog)
        Frame.setWindowTitle(
            QCoreApplication.translate("Frame", Const.NM_APP, None))
    # setLangApp

    def _btnSaveLog_click(self):

        now = datetime.datetime.now()
        format = "%Y-%m-%d_%H-%M-%S"
        nm_file_log = f"Log_{now.strftime(format)}.txt"
        folder_path = QFileDialog().getExistingDirectory()

        if folder_path:
            file_path = os.path.join(folder_path, nm_file_log)

            with open(file_path, "w") as file:
                file.write(str(self._exception_text))
