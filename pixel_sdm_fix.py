#!/usr/bin/env python

# Copyright (c) 2021 handymenny
# This file is licensed under the MIT LICENSE.
# A copy of this license may be found at https://opensource.org/licenses/MIT

import shutil
import sys


def backup(filepath):
    shutil.copy2(filepath, filepath + '.bak')


def replace_header(filepath):
    f = open(filepath, 'rb+')

    # check if third byte is already ok
    f.seek(3)
    if f.read(1) == b'\xfd':
        print(f'{filepath} already has the right header')
        return

    # replace third byte
    f.seek(3)
    f.write(bytes((0xfd,)))
    f.close()
    return


inputArgs = sys.argv

if len(inputArgs) < 2:
    print("Missing file operand")
    print("Usage: SDM_FILE...\nFix the header of the SDM_FILE(s).\nA backup file (.bak) is generated automatically")
    exit(1)

for i in inputArgs[1:]:
    try:
        backup(i)
        replace_header(i)
    except Exception as e:
        print(e)
