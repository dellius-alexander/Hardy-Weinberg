[![Build test and deploy to package repository](https://github.com/dellius-alexander/Hardy-Weinberg/actions/workflows/deploy.yml/badge.svg)](https://github.com/dellius-alexander/Hardy-Weinberg/actions/workflows/deploy.yml)

---

# Hardy Weinberg Equilibrium


Hardy-Weinberg Equilibrium Calculator. Calculates the expected 
genotype frequencies based on the allele frequencies of a 
population in Hardy-Weinberg equilibrium.

## Installation

```bash
pip install hardyweinbergcalculator
```

## Usage

```text
usage: hwc [-h] [--version] [--verbose] [--debug] [--samples SAMPLES] [--p P] [--q Q] [--tpop TPOP] [--ppop PPOP] [--qpop QPOP] [--pq2pop PQ2POP] [--genes GENES [GENES ...]] [--json JSON [JSON ...]]

Hardy-Weinberg Equilibrium Calculator. Calculates the expected genotype frequencies based on the allele frequencies of a population in Hardy-Weinberg equilibrium. See: https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle


optional arguments:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  --verbose          Enable verbose logging. (default: False)
  --debug            Enable debug logging. (default: False)
  --samples SAMPLES  Number of samples to generate, if using random data generator. (default: None)
  --p P              Frequency of dominant allele. (default: None)
  --q Q              Frequency of recessive allele. (default: None)
  --tpop TPOP        Total population. (default: None)
  --ppop PPOP        Original population of dominant allele. (default: None)
  --qpop QPOP        Original population of recessive allele. (default: None)
  --pq2pop PQ2POP    Original population of heterozygous allele. (default: None)

Example: python3 -m hwc --ppop 10 --qpop 10 --pq2pop 200 --verbose
```
