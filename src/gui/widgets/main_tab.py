from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QTextEdit, QApplication
from PySide6.QtGui import QFont, QIcon, QPixmap
from crypto.cryptool import Cryptool

from gui.custom_widgets.custom_dialog import DialogType
import util.constant as Const
import gui.main_win as MainWindow


class MainTab(QWidget):
    def __init__(self, main_window: MainWindow):
        super().__init__()
        self._main = main_window
        self.txtKeyPass = None
        self._create_controls()

    def _create_controls(self):
        self.setObjectName(u"main")
        self.setMinimumSize(QSize(421, 421))
        self.setMaximumSize(QSize(421, 421))

        self.lblAbout = QLabel(self)
        self.lblAbout.setObjectName(u"lblAbout")
        self.lblAbout.setGeometry(QRect(3, 0, 300, 37))
        self.font = self.lblAbout.font()
        self.font.setPointSize(20)
        self.lblAbout.setFont(self.font)

        self.lblInputText = QLabel(self)
        self.lblInputText.setObjectName(u"lblInputText")
        self.lblInputText.setGeometry(QRect(0, 55, 411, 20))

        self.txtInputText = QTextEdit(self)
        self.txtInputText.setObjectName(u"txtInputText")
        self.txtInputText.setGeometry(QRect(0, 80, 411, 115))
        self.txtInputText.setLineWrapMode(QTextEdit.WidgetWidth)
        self.txtInputText.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.txtInputText.setAcceptRichText(False)

        self.lblResponseText = QLabel(self)
        self.lblResponseText.setObjectName(u"lblResponseText")
        self.lblResponseText.setGeometry(QRect(0, 250, 401, 20))

        self.txtResponseText = QTextEdit(self)
        self.txtResponseText.setObjectName(u"txtResponseText")
        self.txtResponseText.setGeometry(QRect(0, 275, 411, 80))
        self.txtResponseText.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.txtResponseText.setReadOnly(True)

        self.btnEncrypt = QPushButton(self)
        self.btnEncrypt.setObjectName(u"btnEncrypt")
        self.btnEncrypt.setGeometry(QRect(0, 200, 121, 34))
        self.btnEncrypt.setMinimumSize(QSize(121, 34))
        self.btnEncrypt.setMaximumSize(QSize(121, 34))
        self.btnEncrypt.setIcon(QPixmap(Const.ICON_ENCRYPT).scaled(18, 18))
        self.btnEncrypt.clicked.connect(self._btnEncrypt_click)

        self.btnClearInput = QPushButton(self)
        self.btnClearInput.setObjectName(u"btnClearInput")
        self.btnClearInput.setGeometry(QRect(145, 200, 121, 34))
        self.btnClearInput.setMinimumSize(QSize(121, 34))
        self.btnClearInput.setMaximumSize(QSize(121, 34))
        self.btnClearInput.setIcon(QPixmap(Const.ICON_ERASER).scaled(18, 18))
        self.btnClearInput.clicked.connect(self._btnClearInput_click)

        self.btnDecrypt = QPushButton(self)
        self.btnDecrypt.setObjectName(u"btnDecrypt")
        self.btnDecrypt.setGeometry(QRect(290, 200, 121, 34))
        self.btnDecrypt.setMinimumSize(QSize(121, 34))
        self.btnDecrypt.setMaximumSize(QSize(121, 34))
        self.btnDecrypt.setIcon(QPixmap(Const.ICON_DECRYPT).scaled(18, 18))
        self.btnDecrypt.clicked.connect(self._btnDecrypt_click)

        self.btnCopyResponse = QPushButton(self)
        self.btnCopyResponse.setObjectName(u"btnCopyResponse")
        self.btnCopyResponse.setGeometry(QRect(0, 370, 160, 34))
        self.btnCopyResponse.setIcon(
            QPixmap(Const.ICON_CLIPBOARD).scaled(18, 18))
        self.btnCopyResponse.clicked.connect(
            self._btnCopyResponse_click)

        self.btnClearResponse = QPushButton(self)
        self.btnClearResponse.setObjectName(u"btnClearResponse")
        self.btnClearResponse.setGeometry(QRect(252, 370, 160, 34))
        self.btnClearResponse.setIcon(
            QPixmap(Const.ICON_ERASER).scaled(18, 18))
        self.btnClearResponse.clicked.connect(
            self._btnClearResponse_click)

        self.lblNmApp = QLabel(self)
        self.lblNmApp.setObjectName(u"lblNmApp")
        self.lblNmApp.setGeometry(QRect(0, 0, 97, 37))
        font = QFont()
        font.setPointSize(20)
        self.lblNmApp.setFont(font)

        self.btnSettings = QToolButton(self)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(365, 5, 25, 25))
        self.btnSettings.setIconSize(QSize(20, 20))
        self.btnSettings.setIcon(QIcon(Const.ICON_SETTINGS))
        self.btnSettings.setStyleSheet('border-radius: 0px;')

        self.btnAbout = QToolButton(self)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(395, 5, 25, 25))
        self.btnAbout.setIconSize(QSize(20, 20))
        self.btnAbout.setIcon(QIcon(Const.ICON_ABOUT))
        self.btnAbout.setStyleSheet('border-radius: 0px;')

        self.clipboard = QApplication.clipboard()

    def _validate_text(self, min_text_size=1):
        result = True
        invalid_text = (self._main.lang_text[Const.ERROR_TXT_EMPTY]
                        if min_text_size == 1
                        else self._main.lang_text[Const.ERROR_INVALID_TXT])

        if len(self.txtInputText.toPlainText().strip()) < min_text_size:
            result = False
            self._main.show_dialog(invalid_text, DialogType.WARNING)

        return result

    def _btnEncrypt_click(self):
        if not self._validate_text():
            return

        crypto = Cryptool(self.txtKeyPass)

        txt = f"'{self.txtInputText.toPlainText().strip()}'"

        return_dto = crypto.txt_encrypt(txt)

        if not return_dto.has_success:
            dialog_type = None
            text = None

            if return_dto.object is None:
                dialog_type = DialogType.WARNING
                text = f'{self._main.lang_text[Const.ERROR_INPUT_TXT]}'
            else:
                text = f'{self._main.lang_text[Const.HAS_ERROR]} {self._main.lang_text[Const.ERROR_INPUT_TXT]}'
                dialog_type = DialogType.CRITICAL

            text = text.format(
                value=self._main.lang_text[Const.ENCRYPT].lower())

            self._main.show_dialog(text, dialog_type)
            return

        self._main.show_dialog(
            self._main.lang_text[Const.ENCRYPT_TXT], DialogType.INFORMATION)

        self.txtResponseText.setText(return_dto.result_msg)

    def _btnDecrypt_click(self):
        if not self._validate_text():
            return

        if not self._validate_text(min_text_size=5):
            return

        crypto = Cryptool(self.txtKeyPass)

        return_dto = crypto.txt_decrypt(
            self.txtInputText.toPlainText().strip())

        if return_dto.object is None:
            dialog_type = DialogType.WARNING
            text = f'{self._main.lang_text[Const.ERROR_INPUT_TXT]}'
        else:
            text = f'{self._main.lang_text[Const.HAS_ERROR]} {self._main.lang_text[Const.ERROR_INPUT_TXT]}'
            dialog_type = DialogType.CRITICAL

            text = text.format(
                value=self._main.lang_text[Const.DECRYPT].lower())

            self._main.show_dialog(text, dialog_type)
            return

        self._main.show_dialog(
            self._main.lang_text[Const.DECRYPT_TXT], DialogType.INFORMATION)

        self.txtResponseText.setText(return_dto.result_msg)

    def _btnClearInput_click(self):
        self.txtInputText.setText(None)

    def _btnCopyResponse_click(self):
        if len(self.txtResponseText.toPlainText().strip()) > 0:
            self.clipboard.setText(self.txtResponseText.toPlainText())
            self._main.show_dialog(
                self._main.lang_text[Const.TXT_COPIED_SUCCESS], DialogType.INFORMATION)

    def _btnClearResponse_click(self):
        self.txtResponseText.setText(None)
