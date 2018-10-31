import subprocess
import os
import atexit
import shlex

from korhal import install_path

def init_server():
    if os.getenv('JAVA_HOME'):
        run_command = '{} -jar {}'.format(
            os.path.join(os.getenv('JAVA_HOME'), 'bin', 'java'),
            os.path.join(install_path, 'korhal-java-server-0.1.1.jar')
        )
    else:
        run_command = 'java -jar {}'.format(os.path.join(install_path, 'korhal-java-server-0.1.1.jar'))

    args = shlex.split(run_command)
    server = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    def _call_at_exit():
        server.kill()
        server.wait()
    atexit.register(_call_at_exit)
    
    while server.poll() is None:
        line = server.stderr.readline().decode()
        if 'Server started' in line:
            break

    if server.poll() is not None:
        stdout, stderr = server.communicate()
        raise Exception(stdout + stderr)
