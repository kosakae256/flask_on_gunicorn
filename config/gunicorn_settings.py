import os

bind = '127.0.0.1:' + str(os.getenv('PORT', 1000))
proc_name = 'default'
workers = 1
