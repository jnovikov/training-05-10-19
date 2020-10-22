#!/usr/bin/env python3
import subprocess
import sys
import os

_dir = 'services'
if len(sys.argv) > 1:
    _dir = sys.argv[1]

exclude = os.environ.get('EXCLUDE')
ignore = os.environ.get('IGNORE')
level = os.environ.get('LEVEL')
confidence = os.environ.get('CONFIDENCE')

cmd = ['python3', '-m', 'bandit', '-r', _dir]

if exclude:
    cmd += ['--exclude', exclude]
if ignore:
    cmd += ['--skip', ignore]

if level:
    if level.lower() == 'low':
        cmd += ['-l']
    elif level.lower() == 'medium':
        cmd += ['-ll']
    elif level.lower() == 'high':
        cmd += ['-lll'] 

if confidence:
    if confidence.lower() == 'low':
        cmd += ['-i']
    elif confidence.lower() == 'medium':
        cmd += ['-ii']
    elif confidence.lower() == 'high':
        cmd += ['-iii'] 

proc = subprocess.run(cmd, capture_output=True, check=False)

out = proc.stdout.decode()

print(out)

sys.exit(proc.returncode)
