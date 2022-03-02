read = 0
written = 0

with open("06.04 EmptyLinesInput.txt") as lines:
    line = lines.readline()
    with open("06.04 EmptyLinesOutput.txt", "w") as n:
        while line:
            if line != "\n":
                n.write(line)
                written += 1
            else:
                pass
            read += 1
            line = lines.readline()

print(f'{read} records read\n{written} records written')