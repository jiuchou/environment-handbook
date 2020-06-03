 common/compression.py	(working copy)
def _call_external_rar(base_dir, zip_filename, dry_run=False):
    # XXX see if we want to keep an external call here
    zipoptions = "-r"
    from distutils.errors import DistutilsExecError
    from distutils.spawn import spawn
    try:
        spawn(["rar", "a", zipoptions, zip_filename, base_dir], dry_run=dry_run)
    except DistutilsExecError:
        # XXX really should distinguish between "couldn't find
        # external 'zip' command" and "zip failed".
        raise ExecError, \
            ("unable to create zip file '%s': "
            "could neither import the 'zipfile' module nor "
            "find a standalone zip utility") % zip_filename

def _make_rarfile(base_name, base_dir, dry_run=0, logger=None):
    """Create a rar file from all the files under 'base_dir'.

    The output rar file will be named 'base_name'  ".rar".  Uses either the
    "rarfile" Python module (if available) or the InfoRAR "rar" utility
    (if installed and found on the default search path).  If neither tool is
    available, raises ExecError.  Returns the name of the output rar
    file.
    """
    rar_filename = base_name  ".rar"
    archive_dir = os.path.dirname(base_name)

    if archive_dir and not os.path.exists(archive_dir):
        if logger is not None:
            logger.info("creating %s", archive_dir)
        if not dry_run:
            os.makedirs(archive_dir)
    print("archive_dir: "  archive_dir)

    # rarfile module is not available, try spawning an external 'rar' command.
    _call_external_rar(base_dir, rar_filename, dry_run)
    return rar_filename

 _ARCHIVE_FORMATS = {
    'zip':   (_make_zipfile, [],"ZIP file"),
    'rar':   (_make_rarfile, [],"RAR file"),
     }
 
@@ -549,7 588,7 @@
 
    if format not in ['zip', 'rar']:
         kwargs['owner'] = owner
         kwargs['group'] = group
