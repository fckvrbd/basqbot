import configparser
import os


class Setup:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file = os.path.join(os.path.dirname(__file__), 'utils', 'config.ini')
        self.token = input("What's your token?: ").replace('"', '')
        self.prefix = input("What's your prefix?: ")

    def write(self):
        self.config.add_section('DISCORD')
        self.config.set('DISCORD', 'TOKEN', self.token)
        self.config.set('DISCORD', 'PREFIX', self.prefix)
        with open(self.file, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)


if __name__ == "__main__":
    setup = Setup()
    setup.write()
