# -*- coding: utf-8 -*-
import os


def setup_loggers(logs_settings, logs_enabled, logs_level, logs_dir,
                  logs_max_size):
    import logging
    import logging.config

    if not logs_enabled:
        return False

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logs_settings['handlers'] = {
        'console': {
            'level': logs_level,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'all_file': {
            'level': logs_level,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'encoding': 'utf8',
            'maxBytes': logs_max_size,
            'backupCount': 20,
            'filename': "%s/all.log" % logs_dir
        },
        'gunicorn_file': {
            'level': logs_level,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'encoding': 'utf8',
            'maxBytes': logs_max_size,
            'backupCount': 20,
            'filename': "%s/gunicorn.log" % logs_dir
        }
    }

    logs_settings['loggers'] = {
        'web': {
            'level': logs_level,
            'handlers': ['console', 'all_file']
        },
        'models': {
            'level': logs_level,
            'handlers': ['console', 'all_file']
        },
        'gunicorn.error': {
            'level': logs_level,
            'handlers': ['console', 'gunicorn_file']
        },
        'gunicorn.access': {
            'level': logs_level,
            'handlers': ['console', 'gunicorn_file']
        },

    }
    logging.config.dictConfig(logs_settings)
