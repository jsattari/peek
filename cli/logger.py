#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import logging

log_fmt = \
    "%(asctime)s - %(filename)s - %(lineno)s - %(funcName)s - %(message)s"

# logger config
logging.basicConfig(
    filename="cli.log",
    filemode="a",
    format=log_fmt,
    level=logging.DEBUG
)

# logger object
logger = logging.getLogger(__name__)
