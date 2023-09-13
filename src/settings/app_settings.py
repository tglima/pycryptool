import json
import util.constant as Const
import os
from settings.user_settings import UserSettings


class AppSettings:

    def get_user_settings(self):

        self._get_config_folder()

        self.file_name = f"{self._config_folder}/user_config.json"

        # Se nao existir o arquivo no caminho ele sera criado
        if not os.path.exists(f"{self.file_name}"):
            self._create_default_user_settings()

        with open(self.file_name, 'r') as file_json:
            config = json.load(file_json)

        # Caso a propriedade nao exista no arquivo ela sera criada
        if not Const.LANGUAGE in config:
            config[Const.LANGUAGE] = ""

        # Caso a propriedade nao exista no arquivo ela sera criada
        if not Const.KEY_PASS in config:
            config[Const.KEY_PASS] = ""

        user_set = UserSettings(
            lang=config[Const.LANGUAGE],
            key_pass=config[Const.KEY_PASS])

        return user_set

    def save_user_settings(self, user_settings):

        # Abrir o arquivo JSON
        with open(self.file_name, 'r') as file_json:
            config = json.load(file_json)

        # Atualiza as propriedades com os novos valores
        config[Const.LANGUAGE] = user_settings.lang
        config[Const.KEY_PASS] = user_settings.key_pass

        # Salva as alteracoes no arquivo
        with open(self.file_name, 'w') as file:
            json.dump(config, file, indent=4)

    def get_lang_txt(self, lang):
        file_path = f"{Const.PATH_I18n}/{lang}.json"

        # Se nao existir o arquivo no caminho ele usara o padrao ingles
        if not os.path.exists(f"{file_path}"):
            file_path = f"{Const.PATH_I18n}/en.json"

        with open(file_path, "r", encoding="utf-8") as file:
            lang_txt = json.load(file)
        return lang_txt

    def _get_config_folder(self):
        home = os.path.expanduser("~")
        dot_config_folder = os.path.join(home, f".config")
        self._config_folder = os.path.join(
            home, f".config/{Const.NM_APP.lower()}")

        if not os.path.exists(dot_config_folder):
            os.makedirs(dot_config_folder)

        if not os.path.exists(self._config_folder):
            os.makedirs(self._config_folder)

    def _create_default_user_settings(self):
        config = {Const.KEY_PASS: "", Const.LANGUAGE: "pt"}

        # Cria o arquivo com as configuracoes pre definidas
        with open(self.file_name, 'w') as file_json:
            json.dump(config, file_json, indent=4)
