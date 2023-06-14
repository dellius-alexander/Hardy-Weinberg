__VERSION__ = '0.2.4'

from .utils import generate_population, random_chars, parse_args, parse_genes_from_cli
from .hardy_weinberg import HardyWeinberg, HardyWeinbergStats
from .genetics import Gene, Allele
from .config import get_logger

