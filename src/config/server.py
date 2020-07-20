# Develop Vmgabriel


"""Module that Define the configuration of server"""

import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


def get_base_path():
    """Define the path base"""
    return str(Path(__file__).resolve().parent.parent.parent)


configuration = {
    'host': '0.0.0.0',
    'port': 7203,

    'debug': True,

    'cookie_secret': os.getenv('COOKIE_SECRET'),
    'cookie_name': os.getenv('COOKIE_NAME'),

    'jwt_location': ['cookies'],
    'jwt_secret': os.getenv('JWT_SECRET'),

    'verify_ip': False,  # True | False

    'limit_max': 200,
    'limit_min': 0,

    'db_name_database': 'daga-iot',
    'db_name_schema': '',
    'user_database': os.getenv('USER_DATABASE'),
    'password_database': os.getenv('PASSWORD_DATABASE'),
    'host_database': os.getenv('HOST_DATABASE'),
    'port_database': '27017',

    'persistency': 'mongo',

    'persistency_secundary': 'sqlite',
    'path_migration': get_base_path() + '/migrations/',
    'file_database': 'process.db'
}
