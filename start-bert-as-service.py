# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:22:32 2022

@author: johnv
"""

import sys

from bert_serving.server import BertServer
from bert_serving.server.helper import get_run_args


if __name__ == '__main__':
    args = get_run_args()
    server = BertServer(args)
    server.start()
    server.join()