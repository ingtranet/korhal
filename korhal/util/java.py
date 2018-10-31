import subprocess
import os
import atexit
import shlex

from korhal import install_path

def init_server():
    if os.getenv('JAVA_HOME'):
        java_path = os.path.join(os.getenv('JAVA_HOME'), 'bin', 'java')
    else:
        java_path = 'java'
    jar_path = os.path.join(install_path, 'korhal-java-server-0.1.2.jar')
    
    args = [java_path, '-jar', jar_path]
    server = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    def _call_at_exit():
        server.kill()
        server.wait()
    atexit.register(_call_at_exit)
    
    while server.poll() is None:
        line = server.stderr.readline()
        if b'Server started' in line:
            break

    if server.poll() is not None:
        stdout, stderr = server.communicate()
        raise Exception(stdout + stderr)


