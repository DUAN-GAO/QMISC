import importlib.resources as ir
from pathlib import Path
import os


with ir.path("QMISC.scripts") as resource:
    ROOT = Path(resource).parent.parent.parent.resolve()

PATH_R_SCRIPTS = ROOT / "QMISC" / "scripts"
PATH_TO_EXAMPLES = ROOT / "QMISC"/ "examples"


__VERSION__ = '1.0'

SEP = f"{'-' * 80}"

__COPYRIGHT_NOTICE__ = """
QMISC: Quantifying Mutation-Induced Surface Changes
Copyright (C) 2025  Duan Gao
Version: {}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
{}""".format(__VERSION__, SEP)

__COPYRIGHT_FULL__ = f"{__COPYRIGHT_NOTICE__}{__COPYRIGHT_MSMS__}"
print(__COPYRIGHT_FULL__)