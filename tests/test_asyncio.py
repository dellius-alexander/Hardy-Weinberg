import logging
from time import perf_counter
from src.utils.generators.population_generator import generate_population, least_common_divisor
from src.config import get_logger

log = get_logger(__name__, level=logging.INFO)


def test_lcm():
    div = least_common_divisor(1255)
    log.info(f"\nDivisor: {div}")
    assert div == 5


def test_asyncio():
    start = perf_counter()
    sample = 1255
    res = generate_population(sample)
    end = perf_counter()
    log.info(f"\nTime Elapsed: {end - start:0.4f} seconds")
    log.info(f"\nFinal chunk size: {len(res)}")
    log.info(f"\nFinal chunk: {res[0].to_json()}")
    assert len(res) == sample

