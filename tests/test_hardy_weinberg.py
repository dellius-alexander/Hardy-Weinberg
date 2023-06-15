import json
import random
import subprocess
import sys
from src import generate_population, get_logger, HardyWeinbergStats, HardyWeinberg
from src.__main__ import main, app

log = get_logger(__name__)


def test_using_generated_samples():
    population = generate_population(10)
    log.info(f"\nPopulation: {len(population)}")
    res = HardyWeinberg(genes=population)
    log.info(f"Result: {res}")


def test_using_population_data_on_main():
    sys.argv = [sys.argv[0],
                "--ppop", f"{random.randint(100, 500)}",
                "--qpop", f"{random.randint(100, 500)}",
                "--pq2pop", f"{random.randint(100, 500)}"]
    log.info(f"\nArgs: {sys.argv}")
    res = main()
    log.info(f"Result: {res}")


def test_population_generator_on_app():
    population = generate_population(10)
    log.info(f"\nPopulation: {len(population)}")
    json_population = json.dumps(population, default=lambda o: o.__dict__(), sort_keys=False)
    res = app(genes=population)
    log.info(f"Result: {res}")


def test_population_generator_and_get_population_count_from_generated_genes():
    population = generate_population(100)
    log.info(f"\nPopulation: {len(population)}")
    # json_population = json.dumps(population, default=lambda o: o.__dict__(), sort_keys=False)
    stats = HardyWeinbergStats.get_population_count_from_genes(population)
    log.info(f"Stats: {stats}")

