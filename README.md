# JTY

Simple tool to convert from JSON/TOML/YAML to JSON/TOML/YAML. (J/T/Y)

## Requirements

* python3
* pipenv

## Installation

    pipenv install

## Usage

Here is some exemples

    jty.py file.json other_file.toml

    jty.py -i json -o t json_file_wo_extention toml_file_wo_extention

    jty.py kubernetes.yaml new_kube.toml


## Warnings

The convertion `yaml` to whatever could be problematic if the yaml contain multiple files