from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QToolButton, QHBoxLayout
from PySide6.QtGui import QFont, QIcon, QPixmap
from gui.custom_widgets.custom_dialog import DialogType
import util.constant as Const
import gui.main_win as MainWindow


class SettingsTab(QWidget):
    def __init__(self, main_window: MainWindow):
        super().__init__()
        self.main = main_window
        self._create_controls()

    def _create_controls(self):
        self.setObjectName(u"settings")
        self.setMinimumSize(QSize(421, 421))
        self.setMaximumSize(QSize(421, 421))

        self.lblTabSettings = QLabel(self)
        self.lblTabSettings.setObjectName(u"lblTabSettings")
        self.lblTabSettings.setGeometry(QRect(0, 0, 300, 37))
        font = QFont()
        font.setPointSize(20)
        self.lblTabSettings.setFont(font)

        self.lblKeyPass = QLabel(self)
        self.lblKeyPass.setObjectName(u"lblKeyPass")
        self.lblKeyPass.setGeometry(QRect(10, 70, 151, 18))

        self.iconQuestion = QToolButton(self)
        self.iconQuestion.setIcon(QIcon(Const.ICON_QUESTION))
        self.iconQuestion.setStyleSheet('border-radius: 0px;')
        self.iconQuestion.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.iconQuestion.setObjectName(u"iconQuestion")
        self.iconQuestion.setGeometry(QRect(95, 70, 16, 16))
        self.iconQuestion.setMinimumSize(QSize(16, 16))
        self.iconQuestion.setMaximumSize(QSize(16, 16))
        self.iconQuestion.setIconSize(QSize(16, 16))
        self.iconQuestion.clicked.connect(self._iconQuestion_click)

        self.lblSelectLang = QLabel(self)
        self.lblSelectLang.setObjectName(u"lblSelectLang")
        self.lblSelectLang.setGeometry(QRect(10, 150, 151, 18))

        self.txtKeyPass = QLineEdit(self)
        self.txtKeyPass.setObjectName(u"txtKeyPass")
        self.txtKeyPass.setGeometry(QRect(10, 90, 241, 32))
        self.txtKeyPass.setMaxLength(20)

        self.cmbSelectLang = QComboBox(self)
        self.cmbSelectLang.setObjectName(u"cmbSelectLang")
        self.cmbSelectLang.setGeometry(QRect(10, 170, 241, 32))

        self.btnSaveSettings = QPushButton(self)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        self.btnSaveSettings.setGeometry(QRect(150, 360, 131, 34))
        self.btnSaveSettings.setMinimumSize(QSize(131, 34))
        self.btnSaveSettings.setMaximumSize(QSize(131, 34))
        self.btnSaveSettings.clicked.connect(self._save_settings_click)
        self.btnSaveSettings.setIcon(QPixmap(Const.ICON_SAVE).scaled(18, 18))

        self.btnGoBack = QToolButton(self)
        self.btnGoBack.setObjectName(u"btnGoBack")
        self.btnGoBack.setGeometry(QRect(395, 5, 20, 20))
        self.btnGoBack.setIconSize(QSize(20, 20))
        self.btnGoBack.setIcon(QIcon(Const.ICON_GO_BACK))
        self.btnGoBack.setStyleSheet('border-radius: 0px;')

    def _iconQuestion_click(self):
        text = self.iconQuestion.toolTip().replace(".", ".\n")
        self.main.show_dialog(text,
                              DialogType.INFORMATION)

    def _validate_save_settings(self):
        is_valid = True
        msg_validate = ""
        txt_input = self.txtKeyPass.text().strip()

        if not (len(txt_input) == 0 or len(txt_input) == 20):
            msg_validate = self.main.lang_text[Const.ERROR_INVALID_TXT]
            is_valid = False

        if self.cmbSelectLang.currentData() == None:
            msg_validate = f"{msg_validate}" if is_valid else f"{msg_validate}\n"
            msg_validate += self.main.lang_text[Const.ERROR_LANG_REQUIRED]
            is_valid = False

        if not is_valid:
            self.main.show_dialog(msg_validate, DialogType.WARNING)

        return is_valid

    def _save_settings_click(self):
        if not self._validate_save_settings():
            return

        self.key_pass = self.txtKeyPass.text().strip()
        self.lang = self.cmbSelectLang.currentData()
        self.cmbSelectLang.clear()
        self.main.save_user_settings()
        self.main.show_dialog(
            self.main.lang_text[Const.SET_SAVED], DialogType.INFORMATION)
