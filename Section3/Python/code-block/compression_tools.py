# -*- coding: utf-8 -*-
#
# :copyright: (c) 2019-2020 Dahua Technology, Inc. All rights reseved worldwide.
# :license: ZHEJIANG DAHUA TECHNOLOGY CO.,LTD.
# :author: 45128 <yang_kaige@dahuatech.com>
# :createTime: 2020.06.03
#
"""将文件或目录压缩到已有的压缩包中"""
import os
import shutil
import tempfile

from common import compression, uncompression, utils
from global_base import LOG, WORKPATH


def get_format(filename):
    # 重新打包成文件
    formats = ".".join(filename.split('/')[-1].split('.')[1:])
    if formats in ['tar.gz', 'tgz']:
        _format = "gztar"
    elif formats in ['tar.bz2', 'tbz2']:
        _format = "bztar"
    elif formats in ['tar.xz', 'txz']:
        _format = "xztar"
    elif formats in ['7z']:
        _format = "7z"
    elif formats in ['rar']:
        _format = "rar"
    else:
        _format = "zip"
    LOG.debug("[%s] file format: %s", filename, _format)
    return _format


dst = 'D:/jk/workspace/Module_IVSVideoDiagnosisClient_W_domestic_windows/code_path/IVSVideoDiagnosisClient/Bin/Setup/VQC_Chn.rar'
d = tempfile.mkdtemp(dir='').replace('\\', '/')
uncompression.unpack_archive(dst, d)

def addfile(dst, src):
    """将文件/目录压缩到已有的压缩包中：如果压缩包存在顶级目录，将文件压缩到顶级目录下。

    dst: 压缩包的名称
    src: 待压缩的文件/目录"""
    LOG.debug("add %s to %s", src, dst)
    dst = os.path.normpath(dst).replace('\\', '/')
    d = tempfile.mkdtemp(dir=WORKPATH).replace('\\', '/')
    uncompression.unpack_archive(dst, d)
    # 如果有同名目录包裹，使用同名目录进行包裹
    dirname = '/'.join(dst.split('/')[:-1])
    name = dst.split('/')[-1].split('.')[0]
    dst_name = d + '/' + name
    LOG.debug('dirname:' + dirname)
    LOG.debug('name:' + name)
    LOG.debug('dst_name: ' + dst_name)
    if os.path.exists(dst_name):
        t = dst_name
    else:
        t = d
    LOG.debug('t: ' + t)
    LOG.debug('src: ' + src)
    if os.path.isdir(src):
        LOG.debug('src type: directory')
        shutil.copytree(src, t + '/' + src.strip('/').split('/')[-1])
    else:
        LOG.debug('src type: file')
        shutil.copy(src, t)
    _format = get_format(dst)
    LOG.debug(_format)
    compression.make_archive(dirname + '/' + name, _format, d)
    utils.rmtree(d)


if __name__ == '__main__':
    # 测试代码
    s = '/home/weops/Development/compression/src/Evo-eims.tar.gz'
    s1 = '/home/weops/Development/compression/src/Evo-eims-1.tar.gz'
    z = '/home/weops/Development/compression/src/Evo-eims.zip'
    z1 = '/home/weops/Development/compression/src/Evo-eims-1.zip'
    r = '/home/weops/Development/compression/src/Evo-eims.rar'
    r1 = '/home/weops/Development/compression/src/Evo-eims-1.rar'

    filename = 'uncompression.py'
    addfile(r1, filename)
