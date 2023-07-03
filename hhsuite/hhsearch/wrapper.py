"""Snakemake wrapper for searching a database of HMMs with a query alignment or query HMM with HHsearch"""

__author__ = "Leighton Payne"
__copyright__ = "Copyright 2023, Leighton Payne"
__email__ = "leighton@duck.com"
__license__ = "MIT"

from snakemake.shell import shell
import argparse

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
  "hhsearch "
  "-i {snakemake.input} "
  "-d {snakemake.database} "
  "-o {snakemake.output} "
  "-cpu {snakemake.threads} "
  "{extra} "
  "{log}"
)
