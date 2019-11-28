# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['plex_posters',
 'plex_posters.__dev',
 'plex_posters.config',
 'plex_posters.lib']

package_data = \
{'': ['*'],
 'plex_posters': ['.mypy_cache/3.8/*',
                  '.mypy_cache/3.8/collections/*',
                  '.mypy_cache/3.8/email/*',
                  '.mypy_cache/3.8/http/*',
                  '.mypy_cache/3.8/importlib/*',
                  '.mypy_cache/3.8/logging/*',
                  '.mypy_cache/3.8/os/*',
                  '.mypy_cache/3.8/requests/*',
                  '.mypy_cache/3.8/requests/packages/*',
                  '.mypy_cache/3.8/requests/packages/urllib3/*',
                  '.mypy_cache/3.8/requests/packages/urllib3/packages/*',
                  '.mypy_cache/3.8/requests/packages/urllib3/packages/ssl_match_hostname/*',
                  '.mypy_cache/3.8/requests/packages/urllib3/util/*',
                  '.mypy_cache/3.8/urllib/*',
                  'test/*']}

install_requires = \
['praw>=6.4,<7.0', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'plex-posters',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'dtomlinson',
    'author_email': 'dtomlinson@panaetius.co.uk',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
