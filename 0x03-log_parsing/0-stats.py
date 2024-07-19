#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            # Split the line into parts and check if it has the right format
            parts = line.split()
            if len(parts) < 9:
                continue

            # Extract the file size
            try:
                size += int(parts[-1])
            except (ValueError, IndexError):
                continue

            # Extract the status code
            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    if status_code not in status_codes:
                        status_codes[status_code] = 1
                    else:
                        status_codes[status_code] += 1
            except IndexError:
                continue

            # Print stats every 10 lines
            if count == 10:
                print_stats(size, status_codes)
                count = 0

        # Print stats at the end if there are remaining lines
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(size, status_codes)
        raise
