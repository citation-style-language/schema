#!/usr/bin/env python3
import subprocess
from pathlib import Path


def main():

    cmd = ["git", "diff", "--name-only", "--cached"]
    changed_files = subprocess.check_output(cmd, text=True).splitlines()

    # I don't understand why, but this currently isn't working
    for rncfile in changed_files:
        if rncfile.endswith(".rnc"):
            rngfile = Path(rncfile).stem
            subprocess.call(["trang", rncfile])
            subprocess.call(["trang", rngfile, rncfile])
            subprocess.call(["git", "add", rncfile])


main()
