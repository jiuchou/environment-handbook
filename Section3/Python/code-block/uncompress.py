# version: python2.7
# 1.keep file mode when unpack zipfile
# 2.add function that unpack 7zfile(can't keep pack file mode)

import os

try:
    import zlib
    del zlib
    _ZLIB_SUPPORTED = True
except ImportError:
    _ZLIB_SUPPORTED = False

try:
    import bz2
    del bz2
    _BZ2_SUPPORTED = True
except ImportError:
    _BZ2_SUPPORTED = False

try:
    import lzma
    del lzma
    _LZMA_SUPPORTED = True
except ImportError:
    _LZMA_SUPPORTED = False

try:
    import rarfile
    del rarfile
    _RARFILE_SUPPORTED = True
except ImportError:
    _RARFILE_SUPPORTED = False

try:
    import pylzma
    del pylzma
    _PYLZMA_SUPPORTED = True
except ImportError:
    _PYLZMA_SUPPORTED = False

__all__ = ["get_unpack_formats", "unpack_archive"]

class ReadError(OSError):
    """Raised when an archive cannot be read"""

def _unpack_tarfile(filename, extract_dir):
    """Unpack tar/tar.gz/tar.bz2/tar.xz `filename` to `extract_dir`
    """
    import tarfile  # late import for breaking circular dependency
    try:
        tarobj = tarfile.open(filename)
    except tarfile.TarError:
        raise ReadError(
            "%s is not a compressed or uncompressed tar file" % filename)
    try:
        tarobj.extractall(extract_dir)
    finally:
        tarobj.close()

def _ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

def _unpack_zipfile(filename, extract_dir):
    """Unpack zip `filename` to `extract_dir`
    """
    import zipfile  # late import for breaking circular dependency

    if not zipfile.is_zipfile(filename):
        raise ReadError("%s is not a zip file" % filename)

    zip = zipfile.ZipFile(filename)
    try:
        for info in zip.infolist():
            name = info.filename

            # don't extract absolute paths or ones with .. in them
            if name.startswith('/') or '..' in name:
                continue

            target = os.path.join(extract_dir, *name.split('/'))
            if not target:
                continue

            # keep file mode
            if platform.system() == "Linux":
                mode = oct(info.external_attr >> 16)
                os.chmod(target, int(mode, 8))

            _ensure_directory(target)
            if not name.endswith('/'):
                # file
                data = zip.read(info.filename)
                f = open(target, 'wb')
                try:
                    f.write(data)
                finally:
                    f.close()
                    del data
    finally:
        zip.close()


def _unpack_rarfile(filename, extract_dir):
    """Unpack rar `filename` to `extract_dir`
    """
    import rarfile  # late import for breaking circular dependency

    if not rarfile.is_rarfile(filename):
        raise ReadError("%s is not a rar file" % filename)

    rar = rarfile.RarFile(filename)
    try:
        for name in rar.namelist():
            rar.extract(name, extract_dir)
    finally:
        rar.close()


def _unpack_7zfile(filename, extract_dir):
    import py7zlib
    fp = open(filename, 'rb')
    archive = py7zlib.Archive7z(fp)
    try:
        for name in archive.getnames():
            # don't extract absolute paths or ones with .. in them
            if name.startswith('/') or '..' in name:
                continue

            target = os.path.join(extract_dir, *name.split('/'))
            if not target:
                continue

            _ensure_directory(target)
            if not name.endswith('/'):
                # file
                data = archive.getmember(name).read()
                f = open(target, 'wb')
                try:
                    f.write(data)
                finally:
                    f.close()
                    del data
    finally:
        fp.close()

_UNPACK_FORMATS = {
    'tar': (['.tar'], _unpack_tarfile, [], "uncompressed tar file"),
}

if _ZLIB_SUPPORTED:
    _UNPACK_FORMATS['gztar'] = (['.tar.gz', '.tgz'], _unpack_tarfile,
                                [('compress', 'gzip')], "gzip'ed tar-file")
    _UNPACK_FORMATS['zip'] = (['.zip'], _unpack_zipfile, [], "ZIP file")

if _BZ2_SUPPORTED:
    _UNPACK_FORMATS['bztar'] = (['.tar.bz2', '.tbz2'], _unpack_tarfile,
                                [('compress', 'bzip2')], "bzip2'ed tar-file")

if _LZMA_SUPPORTED:
    _UNPACK_FORMATS['xztar'] = (['.tar.xz', '.txz'], _unpack_tarfile,
                                [('compress', 'xz')], "xz'ed tar-file")

if _RARFILE_SUPPORTED:
    _UNPACK_FORMATS['rar'] = (['.rar'], _unpack_rarfile, [], "RAR file")

if _PYLZMA_SUPPORTED:
    _UNPACK_FORMATS['7z'] = (['.7z'], _unpack_7zfile, [], "7z-zip file")

def get_unpack_formats():
    """Returns a list of supported formats for unpacking.
    Each element of the returned sequence is a tuple
    (name, extensions, description)
    """
    formats = [(name, info[0], info[3]) for name, info in
               _UNPACK_FORMATS.items()]
    formats.sort()
    return formats

def _find_unpack_format(filename):
    for name, info in _UNPACK_FORMATS.items():
        for extension in info[0]:
            if filename.endswith(extension):
                return name
    return None

def unpack_archive(filename, extract_dir=None, format=None):
    """Unpack an archive.
    `filename` is the name of the archive.

    `extract_dir` is the name of the target directory, where the archive
    is unpacked. If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
    or "xztar".  Or any other registered format.  If not provided,
    unpack_archive will use the filename extension and see if an unpacker
    was registered for that extension.

    In case none is found, a ValueError is raised.
    """
    if extract_dir is None:
        extract_dir = os.getcwd()

    if format is None:
        format = _find_unpack_format(filename)
        if format is None:
            raise ReadError("Unknown archive format '{0}'".format(filename))

    try:
        format_info = _UNPACK_FORMATS[format]
    except KeyError:
        raise ValueError("Unknown unpack format '{0}'".format(format))

    func = format_info[1]
    kwargs = dict(format_info[2])
    func(filename, extract_dir, **kwargs)

