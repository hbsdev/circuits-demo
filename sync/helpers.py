def write_pid_file():
    import os
    pid = str(os.getpid())
    import conf.sync
    f = open(conf.sync.PIDFILE, 'w')
    f.write(pid)
    f.close()
