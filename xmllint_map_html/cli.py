#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import os
import sys

import xmllint_map_html.xmllint_map_html as xmh

DEBUG = os.getenv("XMLLINT_MAP_HTML_DEBUG")


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process ... TODO."""
    argv = argv if argv else sys.argv[1:]
    DEBUG and print(f"Arguments after hand over: ({argv})")
    report = xmh.parse(argv)
    sys.stdout.write(report)
    return 0
