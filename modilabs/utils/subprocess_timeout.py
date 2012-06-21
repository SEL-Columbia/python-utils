import subprocess
import threading

class ProcessTimedOut(Exception):
    pass

class Subprocess(object):
    """
    Enables to run subprocess commands in a different thread
    with TIMEOUT option!

    Based on http://github.com/dimagi/dimagi-utils/blob/master/dimagi/utils/\
    subprocess_timeout.py
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.process = None

    def run(self, timeout=None):
        def target(*args, **kwargs):
            self.process = subprocess.Popen(*args, **kwargs)
            self.process.communicate()

        thread = threading.Thread(target=target, args=self.args,
                kwargs=self.kwargs)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            self.process.terminate()
            thread.join()
            raise ProcessTimedOut("Process `%s` timed out after %s seconds" % (
                ' '.join(self.args[0] if self.args else self.kwargs.get('args')),
                timeout
            ))
        else:
            return self.process.returncode
