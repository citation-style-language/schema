#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import argparse
from shutil import which
from glob import glob

# to validate and pretty print the rnc schema files before commit:
# tools/rnc-validate-format.py

parser = argparse.ArgumentParser(description="process csl schema files")
parser.add_argument("--commit", action="store_true", help="commit the file(s)")
args, unknown = parser.parse_known_args()

rncdir = os.path.join("schemas", "styles")


def rnc_format(rncfile):
    try:
        which("trang") is not None
    except Exception:
        raise SystemExit("trang commnd not found; please install")

    rng_new = rncfile + "_new.rng"

    # round-trip the rnc file through trang
    subprocess.run(["trang", rncfile, rng_new])
    subprocess.run(["trang", rng_new, rncfile])

    # remove the intermediate files
    tempfiles = glob(os.path.join(rncdir, "csl*.rng"))
    for file in tempfiles:
        os.remove(file)


def rnc_pre_commit():

    # this will only work as part of a pre-commit process, where it will run
    # rnc_format on any staged rnc files, and then restage
    cmd = ["git", "diff", "--name-only", "--cached"]
    changed_files = subprocess.check_output(cmd, text=True).splitlines()

    for changed_file in changed_files:
        if changed_file.endswith(".rnc"):
            rnc_format(changed_file)
            subprocess.run(["git", "add", changed_file])


def main():
    if args.commit:
        rnc_pre_commit()
    else:
        rnc_format(os.path.join("schemas", "styles", "csl.rnc"))
        print("\n====> rnc schema files validated and formatted .....")


if __name__ == "__main__":
    main()
