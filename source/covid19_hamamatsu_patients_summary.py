# patients_summary
# 検査陽性患者数

import covid19_hamamatsu_util
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def convert2json(csvData, dtUpdated):
    try:
        return "in preparation..."

    except Exception as e:
        logger.exception(e)
        return "raise exception..."
