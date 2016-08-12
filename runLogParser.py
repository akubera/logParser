#!/usr/bin/env python

from logParser import logParser
from argparse import ArgumentParser


def cli_arg_parser():
    parser = ArgumentParser("logParser")
    parser.add_argument("filename", help="File name of log to parse")
    return parser


if __name__ == '__main__':
    args = cli_arg_parser().parse_args()
    parser = logParser(args.filename)

