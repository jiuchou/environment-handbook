# version: python2.7
# resolve windows shutl.rmtree problem

import os
import shutil
import sys

def rmtree(path):
    """解决shutil.rmtree删除失败报错问题，参考 https://trac.edgewall.org/ticket/12776
    os.remove() doesn't work for read-only files on Windows.
    WindowsError: [Error 5] : 'D:\\code_path\\.svn\\all-wcprops'
    """
    import errno
    def onerror(function, path, excinfo, retry=1):
        # `os.remove` fails for a readonly file on Windows.
        # Then, it attempts to be writable and remove.
        if function != os.remove:
            raise
        e = excinfo[1]
        if isinstance(e, OSError) and e.errno == errno.EACCES:
            mode = os.stat(path).st_mode
            os.chmod(path, mode | 0666)
            try:
                function(path)
            except Exception:
                # print "%d: %s %o" % (retry, path, os.stat(path).st_mode)
                if retry > 10:
                    raise
                time.sleep(0.1)
                onerror(function, path, excinfo, retry + 1)
        else:
            raise
    if os.name == 'nt' and isinstance(path, str):
        # Use unicode characters in order to allow non-ansi characters
        # on Windows.
        path = unicode(path, sys.getfilesystemencoding())
    shutil.rmtree(path, onerror=onerror)

