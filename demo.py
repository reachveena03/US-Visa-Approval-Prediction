from us_Visa.logger import logging
from us_Visa.exception import USvisaException
import sys
try:
    a=1/"10"
except Exception as e:
    raise USvisaException(e, sys) from e

