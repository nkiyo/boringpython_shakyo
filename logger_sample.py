#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import logging

logging.basicConfig(#filename = 'sample.log', # ファイルに出力
                    level= logging.DEBUG, # DEBUG以上のログだけ出力
                    #level= logging.WARNING, # WARNING以上のログだけ出力
                    format = '%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
logging.info('sample info')
logging.warning('sample warning')
logging.error('sample error')
logging.critical('sample error')
logging.debug('End of program')

