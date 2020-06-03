# -*- coding: utf-8 -*-

import coloredlogs
import logging
import os

def get_logger():
    """Configuration Logger info"""
    fmt = "%(levelname)-5s [%(asctime)s [%(filename)s line:%(lineno)d]] %(message)s"
    formatter = logging.Formatter(fmt)

    # Linux 平台下日志添加颜色：控制台显示
    # 不设置日志级别，使用logger.setLevel进行日志级别设置
    coloredlogs.install(logging.NOTSET, fmt=fmt)

    log_name = os.path.dirname(os.path.abspath(__file__)) + "/../build.log"
    handler = logging.FileHandler(log_name)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)

    # 设置文件的默认权限为 logging.INFO
    logger.setLevel(logging.INFO)

    return logger

LOG = logger.get_logger()

# 动态设置日志权限
level = getattr(logging, args.log_level)
LOG.setLevel(level)
