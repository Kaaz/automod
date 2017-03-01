import configparser


def set_default_settings():
    parser = configparser.ConfigParser()
    parser.add_section('general')
    parser.set('general', 'enabled', 'false')
    parser.add_section('discord')
    parser.set('discord', 'bot_token', '?')
    parser.set('discord', 'creator_id', '?')
    parser.add_section('database')
    parser.set('database', 'host', 'localhost')
    parser.set('database', 'user', 'root')
    parser.set('database', 'pass', '')
    parser.set('database', 'database', 'discord')
    return parser


class Config:
    discord_token = None
    enabled = False

    def __init__(self, file):
        config = set_default_settings()
        if not config.read(file, encoding='utf-8'):
            print('Config file {0} does not exist'.format(file))
        self.load_settings(config)
        with open(file, 'w') as cf:
            config.write(cf)

    def validate(self):
        pass

    def load_settings(self, parser):
        self.discord_token = parser.get('discord', 'bot_token')
        self.enabled = parser.getboolean('general', 'enabled')


@property
def discord_token(self):
    return self.discord_token
