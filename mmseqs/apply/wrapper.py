"""Snakemake wrapper for calling an external tool on each entry of an MMseqs2 database."""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2023, Leighton Payne"
__email__ = "leighton@duck.com"
__license__ = "MIT"

from snakemake.shell import shell
import argparse

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
  "mmseqs apply "
  "{snakemake.input} "
  "{snakemake.output} "
  "-- {snakemake.params.program} "
  "{extra} "
  "{log}"
)
