#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ruamel.yaml
import json
import glob
import sys
import os

# grab the yaml files
files = glob.glob('schemas/input/csl-*.yaml')

for file in files:
    ofn = os.path.join('build', os.path.splitext(file)[0] + '.json')
    print(ofn)
    yaml = ruamel.yaml.YAML(typ='safe')

    with open(file) as jsonf:
        data = yaml.load(jsonf)
    with open(ofn, 'w') as fpo:
        json.dump(data, fpo, indent=2)
