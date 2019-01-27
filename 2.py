import sys
from collections import Counter


def part_1(lines):
    counts = [0, 0]
    for line in lines:
        duplicated_counts = Counter(line).values()
        counts[0] += (2 in duplicated_counts)
        counts[1] += (3 in duplicated_counts)
    print(f'counts={counts}, checksum={counts[0] * counts[1]}')


def part_2(lines):
    num_lines = len(lines)
    for i in range(num_lines):
        for j in range(i + 1, num_lines):
            num_diff = sum([1 for c1, c2 in zip(lines[i], lines[j]) if c1 != c2])
            if num_diff == 1:
                print(f"{lines[i]}\n{lines[j]}\n{''.join([c1 for c1, c2 in zip(lines[i], lines[j]) if c1 == c2])}")
                return


assert len(sys.argv) == 2, 'did you forget input?'
with open(sys.argv[1]) as in_fd:
    all_lines = [line for line in in_fd]

part_1(all_lines)
# part_2(all_lines)

