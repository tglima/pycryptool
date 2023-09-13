import subprocess
from settings.app_settings import AppSettings

from util.return_dto import ReturnDTO
import util.constant as Const


class CryptoConsole:
    def __init__(self, user_key=None):

        self._key_crypt = None

        if not user_key is None:
            if len(user_key) != 20:
                raise ValueError(Const.ERROR_INVALID_LEN_USER_KEY)
            else:
                self._key_crypt = user_key

        self._load_lang_txt()
    # __init__

    def _load_lang_txt(self):
        _app_set = AppSettings()
        _settings = _app_set.get_user_settings()
        self._msg = _app_set.get_lang_txt(_settings.lang)
    # _load_lang_txt

    def _process_output(self, process):
        if process.returncode != 0:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.HAS_ERROR])

        # Recupera a saida do processo e salva em uma var
        txt_output = process.stdout.decode('utf-8')

        if txt_output == Const.DART_ERROR_INVALID_TXT or txt_output == Const.DART_ERROR_INVALID_KEY:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.HAS_ERROR])

        # Remove o \n que vem por padrao do console
        if txt_output.endswith("\n"):
            txt_output = txt_output[:-1]

        # Valida se o resultado do console tem algum texto
        if len(txt_output.strip()) == 0:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.HAS_ERROR])

        return ReturnDTO(has_success=True, result_msg=txt_output)
    # _process_output

    def _run_dart_crypto(self, params):
        command = f"cd {Const.PATH_DART_CRYPTO} && ./dart_crypto_console {params}"

        try:
            process = subprocess.run(
                command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return self._process_output(process)
        except Exception as e:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.HAS_ERROR], obj=e)
    # _run_dart_crypto

    def txt_encrypt(self, txt):
        if len(txt.strip()) == 0:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.ERROR_TXT_EMPTY])

        params = None
        if self._key_crypt is None:
            params = f"-t {txt} -o e"
        else:
            params = f"-t {txt} -o e -k {self._key_crypt}"

        return self._run_dart_crypto(params)
    # txt_encrypt

    def txt_decrypt(self, txt):
        if len(txt.strip()) < 4:
            return ReturnDTO(has_success=False, result_msg=self._msg[Const.ERROR_INVALID_TXT])

        params = f"-t {txt} -o d"
        if self._key_crypt is not None:
            params = f"-t {txt} -o d -k {self._key_crypt}"

        return self._run_dart_crypto(params)
    # txt_decrypt
