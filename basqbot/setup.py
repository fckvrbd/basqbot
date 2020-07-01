import configparser
import os


class Setup:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file = os.path.join(os.path.dirname(__file__), 'utils', 'config.ini')

    @staticmethod
    def ask_token():
        return input("What's your token?: ").replace('"', '')

    @staticmethod
    def ask_pwd():
        while True:
            pwd = input("What's your password?: ")
            pwd_conf = input("Confirm your password?: ")
            if pwd == pwd_conf:
                return pwd
            else:
                print("Password wasn't the same! Please try again.")

    @staticmethod
    def ask_prefix():
        return input("What's your prefix?: ")

    def write(self, token, pwd, prefix):
        self.config.add_section('DISCORD')
        self.config.set('DISCORD', 'TOKEN', token)
        self.config.set('DISCORD', 'PASSWORD', pwd)
        self.config.set('DISCORD', 'PREFIX', prefix)
        with open(self.file, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)


if __name__ == "__main__":
    setup = Setup()
    setup.write(setup.ask_token(), setup.ask_pwd(), setup.ask_prefix())
