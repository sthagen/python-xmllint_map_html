# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
from copy import deepcopy
import json
import re
import sys

ENCODING = 'utf-8'
pattern = re.compile(r'^([^:]+):([^:]+):([^:]+):\s+([^:]+):\s+(.+)\s+\[([^]]+)\]\s*$')


def source(path_or_data):
    """Encapsulate the file entry point."""
    with open(path_or_data, "rt", encoding=ENCODING) as handle:
        for line in handle:
            yield line

def _strip(line):
    """Line endings variety shall not complicate the parser."""
    return line.strip().rstrip('\r')


def scan(lines):
    """Scan the source lines and yield records."""
    for line in lines:
        record = _strip(line)
        yield record


def parse(records):
    """Parse the source records and yield parsed result."""
    for record in records:
        if not record:
            continue
        m = pattern.match(record)
        if m:
            yield {
                'path': m.group(1),
                'line': int(m.group(2)),
                'column': int(m.group(3)),
                'severity': m.group(4).lower(),
                'message': m.group(5),
                'msg_code': m.group(6),
            }

        yield {}


