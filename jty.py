#! /usr/bin/env python3

import json
import os.path
import sys

import click
import toml
import yaml

FORMATS = {"j": json, "json": json, "t": toml, "toml": toml, "y": yaml, "yaml": yaml}

LIST_FORMATS = list(sorted(FORMATS.keys()))


def convert(input_mod, output_mod, input, output):
    with open(input) as input_h:
        with open(output, "w") as output_h:
            output_mod.dump(input_mod.load(input_h), output_h)


def find_format(format, file_name):
    module = None
    if format is not None:
        module = FORMATS.get(format)

    if module is None:
        # we try with the file_name extension
        format = os.path.splitext(file_name)[1][1:]
        module = FORMATS.get(format)

    if module is None:
        raise Exception("Unknow format: {}".format(file_name))
    return module


@click.command()
@click.option("-i", "in_format", required=False, type=click.Choice(LIST_FORMATS))
@click.option("-o", "ou_format", required=False, type=click.Choice(LIST_FORMATS))
@click.argument("input", required=True)
@click.argument("output", required=True)
def main(in_format, ou_format, input, output):
    input_mod = find_format(in_format, input)
    output_mod = find_format(ou_format, output)
    convert(input_mod, output_mod, input, output)


if __name__ == "__main__":
    main()
