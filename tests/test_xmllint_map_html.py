# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import xmllint_map_html.xmllint_map_html as xmh


def test_parse_ok_minimal():
    job = ['[]']
    parser = xmh.parse(job)
    assert next(parser) == NotImplemented
