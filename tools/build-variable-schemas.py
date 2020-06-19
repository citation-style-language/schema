#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import json
from string import Template 

# 

# Read source file
vars = open('../schemas/variables/csl-variables.yaml', 'r').read()

# Input variables
dates_input = yaml.safe_load(vars)['variables.dates']
names_input = yaml.safe_load(vars)['variables.names']
numbers_input = yaml.safe_load(vars)['variables.numbers']
titles_input = yaml.safe_load(vars)['variables.titles']
strings_input = yaml.safe_load(vars)['variables.strings']
strings_without_short_input = yaml.safe_load(vars)['variables.strings.without.short']
json_input = yaml.safe_load(vars)['variables.json']

# Define functions to create the variants
def create_variable_variant(variables, modifier, affix):
    # creates a variable variants returned as a list
    # accepts three input parameters: a List of Variables, a modifier ("prefix"/"suffix", and the affix)
    # parameters should be supplied as key/value pairs:
    # create_variable_variant(variables = dates_input, modifier = "prefix", affix= "reviewed")
    new_vars = []
    if modifier=="prefix":
        for var in variables:
            new_vars.append(affix + "-" + var)
    else:
        for var in variables:
            new_vars.append(var + "-" + affix)
    return new_vars
  
def create_original_reviewed_variants(variables):
    # creates original and reviewed variants
    return \
        variables + \
        create_variable_variant(variables=variables , modifier="prefix", affix="original") + \
        create_variable_variant(variables=variables , modifier="prefix", affix="reviewed")


# Create lists with variants

## Dates
dates = create_original_reviewed_variants(dates_input)

## Names
names = create_original_reviewed_variants(names_input)

## Numbers
numbers = create_original_reviewed_variants(numbers_input)

## Stings
strings_full = create_original_reviewed_variants(strings_input)

strings_without_short_full = create_original_reviewed_variants(strings_without_short_input)

strings = \
    strings_full + \
    create_variable_variant(variables=strings_full, modifier="suffix", affix="short") + \
    strings_without_short_full

## Titles
titles_full = create_original_reviewed_variants(titles_input)

titles = \
    titles_full + \
    # -main, and -sub variant creation disabled for 1.0.2, uncomment for 1.1
    # create_variable_variant(variables=titles_full, modifier="suffix", affix="main") + \
    # create_variable_variant(variables=titles_full, modifier="suffix", affix="sub") + \
    create_variable_variant(variables=titles_full, modifier="suffix", affix="short") 
    


# Stringify the lists for RNC

rnc_join_character = "\n    | "

dates_stringified = rnc_join_character.join('"{0}"'.format(w) for w in dates)
names_stringified = rnc_join_character.join('"{0}"'.format(w) for w in names)
numbers_stringified = rnc_join_character.join('"{0}"'.format(w) for w in numbers)
strings_stringified = rnc_join_character.join('"{0}"'.format(w) for w in strings)
titles_stringified = rnc_join_character.join('"{0}"'.format(w) for w in titles)
    
# Define the RNC template, to assemble the complete RNC file, to pass to Trang.

rnc_template = '''namespace a = "http://relaxng.org/ns/compatibility/annotations/1.0"


## Variables
div {{
  
  ## All variables
  variables = variables.dates | variables.names | variables.standard
  
  ## Standard variables
  variables.standard = variables.numbers | variables.strings | variables.titles
  
  ## Date variables
  variables.dates = 
    {dates}
  
  ## Name variables
  variables.names = 
    {names}
  
  ## Number variables
  variables.numbers =
    {numbers}

  ## Ttile variables
  variables.titles = 
    {titles}
  
  ## String variables
  variables.strings =
    {strings}
}}
'''.format(
    dates = dates_stringified,
    names = names_stringified,
    numbers = numbers_stringified,
    titles = titles_stringified,
    strings= strings_stringified,
    )

# Write to csl-variables.rnc

rnc_filename = '../schemas/styles/csl-variables.rnc'
rnc_variables_file= open(rnc_filename,'w')
rnc_variables_file.write(rnc_template)
rnc_variables_file.close()