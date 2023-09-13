import os


# ESSA VARIAVEL SERA CARREGADA QUANDO A APLICACAO INICIAR
_APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


ERROR_INVALID_LEN_USER_KEY = "Invalid value for 'user_key' parameter. The 'user_key' must be set to 20."
DART_ERROR_INVALID_KEY = "The key is invalid!"
DART_ERROR_INVALID_TXT = "The text is invalid!"
PATH_DART_CRYPTO = f"{_APP_PATH}/resources/dart_cryto_console/linux_x64/"
PATH_ICONS = f"{_APP_PATH}/resources/icons"
PATH_RESOURCES = f"{_APP_PATH}/resources"
PATH_I18n = f"{_APP_PATH}/i18n"
PATH_ICONS_2 = f"{_APP_PATH}"


ICON_ABOUT = f"{PATH_ICONS}/about.svg"
ICON_SETTINGS = f"{PATH_ICONS}/settings.svg"
ICON_INFO = f"{PATH_ICONS}/information.svg"
ICON_CRITICAL = f"{PATH_ICONS}/critical.svg"
ICON_QUESTION = f"{PATH_ICONS}/question.svg"
ICON_WARNING = f"{PATH_ICONS}/warning.svg"
ICON_GO_BACK = f"{PATH_ICONS}/go_back.svg"
ICON_SAVE = f"{PATH_ICONS}/save.svg"
ICON_ENCRYPT = f"{PATH_ICONS}/encrypt.svg"
ICON_DECRYPT = f"{PATH_ICONS}/decrypt.svg"
ICON_ERASER = f"{PATH_ICONS}/eraser.svg"
ICON_CLIPBOARD = f"{PATH_ICONS}/clipboard.svg"
ICON_APP = f"{PATH_ICONS}/pycryptool.svg"

NU_VERSION = "0.20230913.1"
IDX_TAB_MAIN = 0
IDX_TAB_ABOUT = 2
IDX_TAB_SETTINGS = 1
NM_APP = "PyCryptool"
LANGUAGE = "language"
KEY_PASS = "key_pass"
VALUE = "value"
LANGUAGES = "languages"
LANG = "lang"
CLOSE = "close"

# LANGUAGE CONSTANTS
RESULT = "result"
ERROR = "error"
YES = "yes"
NO = "no"
SET_SAVED = "settings_saved"
PASSWORD_SAVED = "password_saved"
KEYWORD_WARNING = "keyword_warning"
INPUT_TEXT = "input_text"
CLEAR_TXT = "clear_txt"
COPY_TXT = "copy_txt"
CLEAR_RESPONSE = "clear_response"
KEYWORD_TOOLTIP = "keyword_tooltip"
ENCRYPT = "encrypt"
DECRYPT = "decrypt"
ENCRYPT_TXT = "encrypt_txt"
DECRYPT_TXT = "decrypt_txt"
TXT_COPIED_SUCCESS = "txt_copied_success"
SETTINGS = "settings"
ABOUT = "about"
SELECT_LANGUAGE = "select_language"
SAVE = "save"
VERSION = "version"
COPYRIGHT = "copyright"
VISIT = "visit"
LICENSE = "license"
TRANSLATORS = "translators"
LICENSE_TXT = "license_txt"
GITHUB_LINK = "github_link"
TRANSLATORS_NAME = "translators_name"
COPYRIGHT_TXT = "copyright_txt"
HAS_ERROR = "has_error"
ERROR_OPEN_SITE = "error_open_site"
ERROR_INPUT_TXT = "error_input_txt"
ERROR_INVALID_TXT = "error_invalid_txt"
ERROR_LANG_REQUIRED = "error_lang_required"
ERROR_TXT_EMPTY = "error_txt_empty"
GO_BACK = "go_back"


TXTS_ERROR_WIN = [
    {
        "text": "lblDesc",
        "pt": "Ocorreu um erro durante a execução do programa, veja abaixo os detalhes técnicos do ocorrido",
        "en": "An error occurred during the program's execution. See the technical details below."
    },
    {
        "text": "btnSaveLog",
        "pt": "Salvar log",
        "en": "Save log"
    },
    {
        "text": "btnCloseApp",
        "pt": "Fechar App",
        "en": "Close APP"
    },
    {
        "text": "filterName",
        "pt": "Arquivos de texto (*.txt)",
        "en": "Text files (*.txt)"
    },
]
