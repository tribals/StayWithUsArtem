_TELEGRAM_API_ID = 'TELEGRAM_API_ID'
_TELEGRAM_API_HASH = 'TELEGRAM_API_HASH'
_TELEGRAM_TARGET_GROUP_ID = 'TELEGRAM_TARGET_GROUP_ID'
_TELEGRAM_TARGET_USER_ID = 'TELEGRAM_TARGET_USER_ID'


class EnvConfig(object):
    _APP_NAME = 'STAY_WITH_US'

    def __init__(self, env):
        self.TELEGRAM_API_ID = env[self._env_key(_TELEGRAM_API_ID)]
        self.TELEGRAM_API_HASH = env[self._env_key(_TELEGRAM_API_HASH)]
        self.TELEGRAM_TARGET_GROUP_ID = int(env[self._env_key(_TELEGRAM_TARGET_GROUP_ID)])
        self.TELEGRAM_TARGET_USER_ID = int(env[self._env_key(_TELEGRAM_TARGET_USER_ID)])

    def _env_key(self, key):
        return f'{self._APP_NAME}_{key}'
