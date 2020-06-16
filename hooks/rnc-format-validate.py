#!/usr/bin/env python3
import platform
import subprocess


def main():

    cmd = ["git", "diff", "--name-only", "--cached"]
    changed_files = subprocess.check_output(cmd, text=True).splitlines()

    for rncfile in changed_files:
        if rncfile.endswith(".rnc"):

            cmd = "where" if platform.system() == "Windows" else "which"
            try:
                subprocess.call([cmd, "trang"])
            except Exception:
                print("trang commnd not found; please install")

            rngfile = rncfile + ".rng"
            subprocess.run(["trang", rncfile, rngfile])
            subprocess.run(["trang", rngfile, rncfile])
            subprocess.run(["git", "add", rncfile])


main()
