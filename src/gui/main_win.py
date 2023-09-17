from typing import Type
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QMainWindow, QStackedWidget
from gui.widgets.about_tab import AboutTab
from gui.custom_widgets.custom_dialog import CustomDialog, DialogType
from gui.widgets.main_tab import MainTab
from gui.widgets.settings_tab import SettingsTab
from settings.app_settings import AppSettings
from settings.user_settings import UserSettings
import util.constant as Const


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._app_set = AppSettings()
        self._settings = self._app_set.get_user_settings()

        self._create_controls(self)

    def _create_controls(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self._MainWindow = MainWindow
        self._MainWindow.resize(460, 460)
        self._MainWindow.setMinimumSize(QSize(460, 460))
        self._MainWindow.setMaximumSize(QSize(460, 460))
        self._MainWindow.setWindowTitle(Const.NM_APP)
        self._MainWindow.setWindowIcon(QIcon(Const.ICON_APP))
        self._centralwidget = QWidget(self._MainWindow)
        self._centralwidget.setObjectName(u"centralwidget")
        self._stackedWidget = QStackedWidget(self._centralwidget)
        self._stackedWidget.setObjectName(u"stackedWidget")
        self._stackedWidget.setGeometry(QRect(20, 20, 421, 421))
        self._stackedWidget.setMinimumSize(QSize(421, 421))
        self._stackedWidget.setMaximumSize(QSize(421, 421))

        self._main_tab = MainTab(main_window=self)
        self._main_tab.btnSettings.clicked.connect(self._settings_click)
        self._main_tab.btnAbout.clicked.connect(self._about_click)

        self._settings_tab = SettingsTab(main_window=self)
        self._settings_tab.btnGoBack.clicked.connect(self._go_back_click)

        self._about_tab = AboutTab(main_window=self)
        self._about_tab.btnGoBack.clicked.connect(self._go_back_click)

        self._stackedWidget.addWidget(self._main_tab)
        self._stackedWidget.addWidget(self._settings_tab)
        self._stackedWidget.addWidget(self._about_tab)

        self._MainWindow.setCentralWidget(self._centralwidget)
        self._stackedWidget.setCurrentIndex(Const.IDX_TAB_MAIN)

        self._set_key_pass_widgets()
        self._dialog = CustomDialog()
        self._set_translate_controls()

    def _go_back_click(self):
        self._stackedWidget.setCurrentIndex(Const.IDX_TAB_MAIN)

    def _settings_click(self):
        self._stackedWidget.setCurrentIndex(Const.IDX_TAB_SETTINGS)

    def _about_click(self):
        self._stackedWidget.setCurrentIndex(Const.IDX_TAB_ABOUT)

    def show_dialog(self, text: str, type: Type[DialogType]):
        return self._dialog.show(text, type)

    def save_user_settings(self):
        user_settings = UserSettings(
            lang=self._settings_tab.lang, key_pass=self._settings_tab.key_pass)

        self._app_set.save_user_settings(user_settings)
        self._settings = user_settings
        self._set_key_pass_widgets()
        self._set_translate_controls()

    def _set_key_pass_widgets(self):
        self._main_tab.txtKeyPass = self._get_key_pass()
        self._settings_tab.txtKeyPass.setText(self._get_key_pass())

    def _get_key_pass(self):
        if len(self._settings.key_pass) != 20:
            return None
        return self._settings.key_pass

    def _set_translate_controls(self):

        # Carrega os textos de acordo com as configs de linguagens definidas
        txt = self.lang_text

        # Carrega os textos para os controles da main_tab
        self._main_tab.lblAbout.setText(Const.NM_APP)
        self._main_tab.lblInputText.setText(txt[Const.INPUT_TEXT])
        self._main_tab.lblResponseText.setText(txt[Const.RESULT])
        self._main_tab.btnEncrypt.setText(" " + txt[Const.ENCRYPT])
        self._main_tab.btnClearInput.setText(" " + txt[Const.CLEAR_TXT])
        self._main_tab.btnDecrypt.setText(" " + txt[Const.DECRYPT])
        self._main_tab.btnCopyResponse.setText(" " + txt[Const.COPY_TXT])
        self._main_tab.btnClearResponse.setText(
            "  " + txt[Const.CLEAR_RESPONSE])
        self._main_tab.btnSettings.setToolTip(txt[Const.SETTINGS])
        self._main_tab.btnAbout.setToolTip(txt[Const.ABOUT])

        # Carrega os textos para os controles da settings_tab
        self._settings_tab.lblTabSettings.setText(txt[Const.SETTINGS])
        self._settings_tab.lblKeyPass.setText(txt[Const.KEY_PASS])
        self._settings_tab.iconQuestion.setToolTip(txt[Const.KEYWORD_TOOLTIP])
        self._settings_tab.lblSelectLang.setText(txt[Const.SELECT_LANGUAGE])
        self._settings_tab.btnSaveSettings.setText(" " + txt[Const.SAVE])
        self._settings_tab.cmbSelectLang.clear()

        for item in txt[Const.LANGUAGES]:
            self._settings_tab.cmbSelectLang.addItem(
                item[Const.LANG], item[Const.VALUE])

        self._settings_tab.cmbSelectLang.setCurrentIndex(
            self._settings_tab.cmbSelectLang.findData(self._settings.lang))

        # Carrega os textos para os controles da about_tab
        self._about_tab.lblAbout.setText(Const.NM_APP)
        self._about_tab.lblVersion.setText(
            txt[Const.VERSION] + Const.NU_VERSION)
        self._about_tab.lblCopyright.setText(
            txt[Const.COPYRIGHT] + txt[Const.COPYRIGHT_TXT])
        self._about_tab.lblSite.setText(
            txt[Const.VISIT] + txt[Const.GITHUB_LINK])
        self._about_tab.lblLicense.setText(
            txt[Const.LICENSE] + txt[Const.LICENSE_TXT])
        self._about_tab.lblTranslators.setText(
            txt[Const.TRANSLATORS] + txt[Const.TRANSLATORS_NAME])
        self._about_tab.btnGoBack.setToolTip(txt[Const.GO_BACK])

        # Carrega os textos para os controles do custom_dialog
        self._dialog.btn_close.setText(txt[Const.CLOSE])
        self._dialog.btn_no.setText(txt[Const.NO])
        self._dialog.btn_yes.setText(txt[Const.YES])

    @property
    def lang_text(self):
        return self._app_set.get_lang_txt(self._settings.lang)
