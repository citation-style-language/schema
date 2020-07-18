#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ruamel.yaml
from pathlib import Path
import json
import glob
import sys

# grab the yaml files
files = glob.glob('schemas/input/csl-*.yaml')

for file in files:
    ofns = Path(file).stem
    ofn = ofns + '.json'
    yaml = ruamel.yaml.YAML(typ='safe')

    with open(file) as jsonf:
        data = yaml.load(jsonf)
    with open(ofn, 'w') as fpo:
        json.dump(data, fpo, indent=2)
