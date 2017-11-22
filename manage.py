# -*- coding:utf-8 -*-

import os
from sinit import create_app
from flask_script import Manager, Shell

CONFIGURE_MODE = os.environ.get('FLASK_MODE') or 'heroku'

app = create_app(CONFIGURE_MODE)
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
