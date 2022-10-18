from pkg_resources import DistributionNotFound, get_distribution

from .constants import *
from .functions1 import *

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
