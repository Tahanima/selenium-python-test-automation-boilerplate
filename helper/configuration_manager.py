from jproperties import Properties


class ConfigurationManager:
    def __init__(self):
        self.configs = Properties()

        with open('resources/config.properties', 'rb') as config_file:
            self.configs.load(config_file)

    def fetch(self, property_key: str) -> str:
        return self.configs.get(property_key)[0]

    def headless(self) -> bool:
        return self.fetch('headless') == 'True'

    def timeout(self) -> int:
        return int(self.fetch('timeout'))

    def base_url(self) -> str:
        return self.fetch('base.url')
