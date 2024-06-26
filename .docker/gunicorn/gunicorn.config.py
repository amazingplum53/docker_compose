
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ

max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8001')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()
