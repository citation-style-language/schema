#! /usr/bin/env bash
# This assumes you have trang installed via package manager
# which installs a script to provide a "trang" command.
# Make sure you run this before commiting any changes to the 
# rnc files.

trang csl.rnc csl.rng
trang csl.rng csl.rnc
rm -f csl.rng csl-*.rng

