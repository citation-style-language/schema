#!/usr/bin/env python3
import subprocess


def main():

    cmd = ["git", "diff", "--name-only", "--cached"]
    changed_files = subprocess.check_output(cmd, text=True).splitlines()

    for rncfile in changed_files:
        if rncfile.endswith(".rnc"):
            rngfile = rncfile + ".rng"
            subprocess.run(["trang", rncfile, rngfile])
            subprocess.run(["trang", rngfile, rncfile])
            subprocess.run(["git", "add", rncfile])


main()
