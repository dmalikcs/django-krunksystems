#!/usr/bin/env python 

bind='192.168.1.101:8001'
workers=3

accesslog='/tmp/gcon_access.log'

errorlog='/tmp/gcone_error.log'
#worker-connections=1000
#max-request=10
#debug=True

###Loging details ###
#loglevel='debug' #debug,info,warning,error,critical
#logger_class
#logconfig                                  ## --log-config FILE
#syslog_addr                                ## --kig-syslog-to SYSLOG_ADDR
#syslog                                     ## --log-syslog
#syslog_prefix                              ## --log-syslog-prefix SYSLOG_PREFIX
#syslog_facility                            ##--log-syslog-faclility SYSLOG_FACILITY
#enable_studio_inheritance                  ##-R,--enable-studi-inheritance 
#proc_name='deepak'
#default_proc_name

#####################
###Django Setting ###
####################

#django_settings                            ##--settings STRING
#pythonpath                                 ##--pythonpath STRING



#####################
##Server hooks      #
####################
def on_starting(server):
    print "server has been started"


def when_ready(server):
    print "server is ready to accept the request"

def on_reload(server):
    print "server has been reloaded successfully"


def pre_fork(server,worker):
    print "Just called before worker load"


def post_fork(server,worker):
    print "post worker"
