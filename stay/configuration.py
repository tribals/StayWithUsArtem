import sys

if sys.platform == 'win32':
    import toml


class EnvConfig(object):
    _APP_NAME = 'STAY_WITH_US'

    def __init__(self, env):
        self.TELEGRAM_API_ID = env[self._env_key('TELEGRAM_API_ID')]
        self.TELEGRAM_API_HASH = env[self._env_key('TELEGRAM_API_HASH')]
        self.TELEGRAM_PHONE = env[self._env_key('TELEGRAM_PHONE')]
        self.TELEGRAM_TARGET_GROUP_ID = int(env[self._env_key('TELEGRAM_TARGET_GROUP_ID')])
        self.TELEGRAM_TARGET_USER_ID = int(env[self._env_key('TELEGRAM_TARGET_USER_ID')])

    def _env_key(self, key):
        return f'{self._APP_NAME}_{key}'


class TOMLFileConfig(object):
    def __init__(self, file):
        config = toml.load(file)

        self.TELEGRAM_API_ID = config['telegram']['api_id']
        self.TELEGRAM_API_HASH = config['telegram']['api_hash']
        self.TELEGRAM_PHONE = config['telegram']['phone']
        self.TELEGRAM_TARGET_GROUP_ID = config['telegram']['target_group_id']
        self.TELEGRAM_TARGET_USER_ID = config['telegram']['target_user_id']
