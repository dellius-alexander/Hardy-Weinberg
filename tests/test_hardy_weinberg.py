import json
import random
import sys
from hardyweinbergcalculator import generate_population, get_logger, app

log = get_logger(__name__)


def test_using_generated_samples():
    population = generate_population(1000)
    log.info(f"\nPopulation: {len(population)}")
    json_population = json.dumps(population, default=lambda o: o.__dict__(), sort_keys=False)
    sys.argv = [sys.argv[0], "--genes", json_population]
    res = app()
    log.info(f"Result: {res}")



def test_using_populations():
    sys.argv = [sys.argv[0], "--verbose",
                "--ppop", str(random.randint(0, 500)),
                "--qpop", str(random.randint(0, 500)),
                "--pq2pop", str(random.randint(0, 500))]
    res = app()
    log.info(f"Result: {res}")


def test_population_generator():
    population = generate_population(100)
    log.info(f"\nPopulation: {len(population)}")
