#!/usr/bin/env python3
import sys
current_word = None
current_count = 0
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    word, count = parts
    try:
        count = int(count)
    except ValueError:
        continue
    if word == current_word:
        current_count += count
    else:
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
if current_word is not None:
    print(f"{current_word}\t{current_count}")