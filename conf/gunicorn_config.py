import confs

command = confs.project_path + '/env/bin/gunicorn'
pythonpath = confs.project_path
bind = confs.host + ':' + confs.port
workers = 3
