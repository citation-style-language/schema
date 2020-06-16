#!/usr/bin/env python3
import subprocess
from pathlib import Path


def main():

    proc = subprocess.Popen(
        ["git", "diff", "--name-only", "--cached"], stdout=subprocess.PIPE
    )
    changed_files = proc.stdout.readlines()
    changed_files = [f.decode("utf-8") for f in changed_files]
    changed_files = [f.strip() for f in changed_files]

    # I don't understand why, but this currently isn't working
    for rncfile in changed_files:
        if rncfile.endswith(".rnc"):
            rngfile = Path(rncfile).stem
            subprocess.call(["trang", rncfile])
            subprocess.call(["trang", rngfile, rncfile])
            subprocess.call(["git", "add", rncfile])


main()
