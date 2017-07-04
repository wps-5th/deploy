from config.wsgi.base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

