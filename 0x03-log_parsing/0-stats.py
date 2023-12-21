#!/usr/bin/python3
import sys
import re

# Check expected string pattern
ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
date = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
request = r'"GET /projects/260 HTTP/1.1"'

pattern = re.compile(fr'^({ip}) - ({date}) {request} (\d{{3}}) (\d+)$')

total_size = 0
log_count = 0
status_codes = {}

try:
    for line in sys.stdin:
        match = pattern.match(line)

        if match:
            status_code = match.group(3)
            file_size = match.group(4)

            # Sum up file size
            if file_size.isdigit():
                total_size += int(file_size)

            # Collate the number of logs per status code
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            # Increment the log count
            log_count += 1

            if log_count % 10 == 0:
                print("File size:", total_size)

                for key, value in sorted(status_codes.items()):
                    print(f"{key}: {value}")

            # Clear status codes
            # status_codes = {}

except KeyboardInterrupt:
    print("File size:", total_size)

    for key, value in sorted(status_codes.items()):
        print(f"{key}: {value}")
