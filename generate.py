#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from random import randrange
from datetime import datetime

DT = datetime.now()
TAG_SET = ("tag1", "tag2", "tag3", "tag4", "tag5", "tag6")
DIFFICULTY_SET = ("EASY", "MEDIUM", "HARD")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    print("Generating input quiz file ...")
    buff = ""
    for x in range(1, 601):
        tag_idx = randrange(1, 6)
        diff_idx = randrange(1, 3)
        buff += "Q%s|%s|%s\n" % (x, TAG_SET[tag_idx], DIFFICULTY_SET[diff_idx])
    file_path = "%s/data_dump/" % (BASE_DIR)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(
        "%squestions_%s.txt" % (
            file_path, int(DT.timestamp())), "w") as fp:
        fp.write(buff)


if __name__ == "__main__":
    main()
