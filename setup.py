#!/usr/bin/python
# Copyright © 2024- Luka Ivanović
# This code is licensed under the terms of the MIT Licence (see LICENCE for details).

import subprocess
from datetime import datetime
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--project", type=str, default="demo", required=False, help="project's name")
parser.add_argument("--author", type=str, required=True, help="author's name")
args = parser.parse_args()

project = args.project
author = args.author

def ex(command: str, verbose: bool = True, shell: bool = False) -> str | None:
    if verbose:
        print(command)
    result = subprocess.run(command.split(" "),capture_output=True, text=True, shell=shell)
    return result.stdout if result.stdout else None


def isDir(path: str) -> bool:
    if os.path.exists(path) and os.path.isdir(path):
        return True
    return False

def isFile(path: str) -> bool:
    if os.path.exists(path) and os.path.isfile(path):
        return True
    return False

def isActive() -> bool:
    return sys.prefix != sys.base_prefix

def year() -> str:
    return datetime.now().strftime("%Y")

if not isDir("venv/"):
    # TODO: handle errors
    ex(f"python -m venv venv --prompt {project}")

if not isDir(".git/"):
    ex("git init")

if not isFile(".gitignore"):
    with open(".gitignore", "w") as f:
        f.write(f"""venv/
""")

# TODO: pick the right script based on the current shell
print("Run `source venv/bin/activate.fish` to activate the environment.")

if not isFile("LICENCE"):
    with open("LICENCE", "w") as f:
        f.write(f"""MIT Licence

Copyright © {year()}- {author}

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")

if not isFile("README.md"):
    with open("README.md", "w") as f:
        f.write(f"""# {project}

### TODO:
- []

### Licence

This code is licensed under the terms of the MIT Licence (see LICENCE for details).

""")

if not isFile("pyrightconfig.json"):
    with open("pyrightconfig.json", "w") as f:
        f.write(f"""{{
    "venvPath": ".",
    "venv": "venv/"
}}
""")
