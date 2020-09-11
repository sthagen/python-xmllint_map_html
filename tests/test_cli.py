# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import io
import json
import pytest  # type: ignore

import xmllint_map_html.cli as cli
import xmllint_map_html.xmllint_map_html as xmh


def test_main_ok_minimal(capsys):
    job = ['']
    report_expected = ''
    assert cli.main(argv=job) == 0
    out, err = capsys.readouterr()
    assert out.strip() == report_expected.strip()
