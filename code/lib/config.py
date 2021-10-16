'''
Создаем конфигурационный файл и читаем его
'''

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

CONFIG_NAME: str = "debi.ini"
MAIN_SECTION = ''
IFNS_KEY = '00000000000'
POCHTA_KEY = '1111111111111'
IFNS_ADDR = 'https://egrul.nalog.ru'
POCHTA_ADDR = 'http://pochta.ru'



class DebiConfig:
    def __init__(self, name=CONFIG_NAME):
        self.path = name
        self.cfg = configparser.ConfigParser()

    def update(self):
        with open(self.path, "w") as config_file:
            self.cfg.write(config_file)

    def cmake(self):
        self.cfg.add_section(MAIN_SECTION)
        self.cfg.set(MAIN_SECTION, 'ifns_key', IFNS_KEY)
        self.cfg.set(MAIN_SECTION, 'pochta_key', POCHTA_KEY)
        self.cfg.set(MAIN_SECTION, 'ifns_addr', IFNS_ADDR)
        self.cfg.set(MAIN_SECTION, 'pochta_addr', POCHTA_ADDR)
        self.update()

    def cread(self):
        pass


if __name__ == '__main__':
    config = DebiConfig()
    config.cmake()
    exit(0)
