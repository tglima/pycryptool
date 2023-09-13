from PySide6.QtCore import QSize, QRect
from PySide6.QtWidgets import QWidget, QLabel, QToolButton
from PySide6.QtGui import QIcon
import util.constant as Const
import gui.main_win as MainWindow


class AboutTab(QWidget):
    def __init__(self, main_window: MainWindow):
        super().__init__()
        self.main_window = main_window
        self._create_controls()

    def _create_controls(self):

        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.setMinimumSize(QSize(421, 421))
        self.setMaximumSize(QSize(421, 421))

        self.lblAbout = QLabel(self)
        self.lblAbout.setObjectName(u"lblAbout")
        self.lblAbout.setGeometry(QRect(3, 0, 300, 37))
        self.font = self.lblAbout.font()
        self.font.setPointSize(20)
        self.lblAbout.setFont(self.font)

        self.lblVersion = QLabel(self)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setGeometry(QRect(3, 50, 150, 20))

        self.lblCopyright = QLabel(self)
        self.lblCopyright.setObjectName(u"lblCopyright")
        self.lblCopyright.setGeometry(QRect(3, 80, 300, 20))

        self.lblSite = QLabel(self)
        self.lblSite.setObjectName(u"lblSite")
        self.lblSite.setGeometry(QRect(3, 110, 300, 20))

        self.lblLicense = QLabel(self)
        self.lblLicense.setObjectName(u"lblLicense")
        self.lblLicense.setGeometry(QRect(3, 130, 380, 60))
        self.lblLicense.setWordWrap(True)

        self.lblTranslators = QLabel(self)
        self.lblTranslators.setObjectName(u"lblTranslators")
        self.lblTranslators.setGeometry(QRect(3, 150, 380, 100))
        self.lblTranslators.setWordWrap(True)

        self.btnGoBack = QToolButton(self)
        self.btnGoBack.setObjectName(u"btnGoBack")
        self.btnGoBack.setGeometry(QRect(395, 0, 20, 20))
        self.btnGoBack.setIconSize(QSize(20, 20))
        self.btnGoBack.setIcon(QIcon(Const.ICON_GO_BACK))
        self.btnGoBack.setStyleSheet('border-radius: 0px;')
