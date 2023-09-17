import traceback
from PySide6.QtWidgets import QApplication
from gui.error_win import ErrorWindow
from gui.main_win import MainWindow
from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale
from PySide6.QtWidgets import QApplication
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    translator = QTranslator()

    try:
        # Identifica o idioma do sistema operacional
        lang_os = f"qt_{QLocale.system().name()}"

        # Carrega os arquivos de idioma
        translator.load(
            lang_os, QLibraryInfo.path(QLibraryInfo.TranslationsPath))

        # Seta o idioma para os menus de contexto da aplicacao
        app.installTranslator(translator)

        main_window = MainWindow()
        main_window.show()

    except Exception as ex:
        stacktrace = traceback.format_exc()
        error_win = ErrorWindow(stacktrace)
        error_win.show()

    sys.exit(app.exec())
