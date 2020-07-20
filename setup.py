
"""Setup definition project"""

# Env
from src.config.server import configuration as conf

# App
from src.__main__ import app

if __name__ == '__main__':
    app.run(
        host=conf['host'],
        debug=conf['debug'],
        port=conf['port']
    )
