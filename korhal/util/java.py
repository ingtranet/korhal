import subprocess
import os
import atexit
import shlex

from korhal import install_path

def init_server():
    if os.getenv('JAVA_HOME'):
        run_command = '{}/bin/java -jar {}/korhal-java-server-0.1.1.jar'.format(os.getenv('JAVA_HOME'), install_path)
    else:
        run_command = 'java -jar {}/korhal-java-server-0.1.1.jar'.format(install_path)

    args = shlex.split(run_command)
    server = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    def _call_at_exit():
        server.kill()
        server.wait()
    atexit.register(_call_at_exit)
    
    if server.poll() is None:
        while server.poll() is None:
            line = server.stderr.readline().decode()
            if 'Server started' in line:
                break
    else:
        stdout, stderr = server.communicate()
        raise Exception(stdout + b'\n' + stderr)
