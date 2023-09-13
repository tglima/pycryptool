from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QLabel, QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon, QPixmap
import util.constant as Const
import gui.main_win as MainWindow
from enum import Enum
from typing import Type


class DialogType(Enum):
    QUESTION = "Question"
    WARNING = "Warning"
    CRITICAL = "Critical"
    INFORMATION = "Information"


class DialogIcon(Enum):
    QUESTION = "dialog-question"
    WARNING = "dialog-warning"
    CRITICAL = "dialog-critical"
    INFORMATION = "dialog-information"


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Configuração do diálogo
        self.setWindowFlag(Qt.FramelessWindowHint)  # Remover a moldura
        self.setModal(True)  # Tornar o diálogo modal
        self.resize(400, 200)

        _main_layout = QVBoxLayout()

        self._icon_dialog = DialogIcon.INFORMATION.value
        self._icon_img = QPixmap.fromImage(QIcon.fromTheme(
            self._icon_dialog).pixmap(QSize(64, 64)).toImage())

        self._icon = QLabel(self)
        self._icon.setPixmap(self._icon_img)
        self._icon.setAlignment(Qt.AlignHCenter)
        _main_layout.addWidget(self._icon)

        self._msg_text = QLabel(self)
        self._msg_text.setAlignment(Qt.AlignHCenter)
        self._msg_text.setContentsMargins(0, 5, 0, 0)
        _main_layout.addWidget(self._msg_text)

        self._layout_buttons = QHBoxLayout()

        self.btn_yes = QPushButton("", self)
        self.btn_yes.clicked.connect(self.accept)
        self.btn_yes.setMaximumWidth(100)
        self._layout_buttons.addWidget(self.btn_yes)

        self.btn_no = QPushButton("", self)
        self.btn_no.clicked.connect(self.reject)
        self.btn_no.setMaximumWidth(100)
        self._layout_buttons.addWidget(self.btn_no)

        self.btn_close = QPushButton(None, self)
        self.btn_close.clicked.connect(self.accept)
        self._layout_buttons.addWidget(self.btn_close)

        self._layout_buttons.setAlignment(Qt.AlignHCenter)
        self._layout_buttons.setContentsMargins(0, 20, 0, 0)
        _main_layout.addLayout(self._layout_buttons)
        _main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(_main_layout)

    def _set_icon_dialog(self, type: Type[DialogType]):

        icons = {
            DialogType.INFORMATION: Const.ICON_INFO,
            DialogType.WARNING: Const.ICON_WARNING,
            DialogType.QUESTION: Const.ICON_QUESTION,
            DialogType.CRITICAL: Const.ICON_CRITICAL
        }

        self._icon_img = QPixmap.fromImage(QIcon.fromTheme(
            icons.get(type)).pixmap(QSize(48, 48)).toImage())

        self._icon.setPixmap(self._icon_img)

    def show(self, text: str, type: Type[DialogType]):
        self.btn_close.setVisible(False)
        self.btn_yes.setVisible(False)
        self.btn_no.setVisible(False)

        self._msg_text.setText(text)
        self.icon_dialog = DialogIcon[type.name].value
        self._set_icon_dialog(type)
        result = 0

        if type == DialogType.QUESTION:
            result = self._show_question()
        else:
            result = self._show_basic_dialog()

        return result

    def _show_question(self):
        self.btn_yes.setVisible(True)
        self.btn_no.setVisible(True)
        return self.exec()

    def _show_basic_dialog(self):
        self.btn_close.setVisible(True)
        return self.exec()
