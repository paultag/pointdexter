import shlex
import subprocess

def run_command(command):
    """
    Run a synchronized command. The argument must be a list of arguments.
    Returns a triple (stdout, stderr, exit_status)

    If there was a problem to start the supplied command, (None, None, -1) is
    returned
    """
    if not isinstance(command, list):
        command = shlex.split(command)
    try:
        pipe = subprocess.Popen(command,
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    except OSError as e:
        logger.error("Could not execute %s: %s" % (" ".join(command), e))
        return (None, None, -1)
    (output, stderr) = pipe.communicate()
    return (output, stderr, pipe.returncode)
