#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ruamel.yaml
from pathlib import Path
import json
import glob
import sys

# grab the yaml files
yfiles = glob.glob('schemas/input/csl-*.yaml')

for yfile in yfiles:
    inf = Path(yfile)
    ofns = inf.stem
    ofn = Path('build/' + ofns + '.json')
    yaml = ruamel.yaml.YAML(typ='safe')
    data = yaml.load(inf)
    with open(ofn, "w") as write_file:
        json.dump(data, write_file, indent=2)
