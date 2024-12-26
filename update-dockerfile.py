#!/usr/bin/env python3

import os
import sys

node_version = "23"

glibc_version = "2.34-r0"

def read_file(file):
    with open(file, "r") as f:
        return f.read()

def write_file(file, contents):
    dir = os.path.dirname(file)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    with open(file, "w") as f:
        f.write(contents)

def update_alpine_gblic():
    template = read_file("Dockerfile-alpine-glibc.template")

    rendered = template \
        .replace("%%TAG%%", node_version) \
        .replace("%%GLIBC-VERSION%%", glibc_version)

    write_file(f"{node_version}/alpine-glibc/Dockerfile", rendered)

def usage():
    print(f"Usage: {sys.argv[0]} update")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    task = sys.argv[1]
    if task == "update":
        update_alpine_gblic()
    else:
        usage()
