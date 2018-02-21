import os

import chops


HERE = os.path.abspath(os.path.dirname(__file__))
SETTINGS = dict()


SETTINGS['project_name'] = 'Chops Project'
SETTINGS['project_path'] = HERE


SETTINGS['plugins'] = [
    'chops.plugins.dotenv',

    # Uncomment to use Docker plugin
    # 'chops.plugins.docker',

    # Uncomment to use Travis CI plugin
    # 'chops.plugins.travis',
]


SETTINGS['dotenv'] = {
    'env_files': {
        'main_dotenv_path': os.path.join(SETTINGS['project_path'], '.env'),
    },
    'template': os.path.join(chops.utils.PLUGINS_PATH, 'env.template'),
    'template_lock': os.path.join(SETTINGS['project_path'], 'env.template.lock'),
}

SETTINGS['docker'] = {
    'docker_root': os.path.join(SETTINGS['project_path'], 'docker'),
    'project_name': 'chops' * 3,
    'repository_prefix': None,
}
