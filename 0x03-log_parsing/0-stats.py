#!/usr/bin/python3
"""
Log parsing
"""
import sys
import re


def print_status(size, freqs):
    """
    Helper function to output status
    """
    print(f"File size: {size}")

    for code in sorted(freqs.keys()):
        if freqs[code] > 0:
            print(f"{code}: {freqs[code]}")


if __name__ == "__main__":
    ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    date = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
    request = r'"GET /projects/260 HTTP/1.1"'

    # Check expected string pattern
    pattern = re.compile(fr'^({ip}) - ({date}) {request} (\d{{3}}) (\d+)$')

    line_count = 0
    total_size = 0
    code_freqs =\
        {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line.strip()
            match = pattern.match(line)

            if match:
                code = int(match.group(3))
                file_size = int(match.group(4))

                # Sum up file size
                total_size += int(file_size)

                # Collate the number of lines per status code
                if code in code_freqs:
                    code_freqs[code] += 1

                # Increment the log count
                line_count += 1

                if line_count % 10 == 0:
                    print_status(total_size, code_freqs)

    finally:
        print_status(total_size, code_freqs)
