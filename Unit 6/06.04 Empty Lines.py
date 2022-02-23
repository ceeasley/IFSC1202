#You have a file that has text in it. Some of the lines are empty.
#Create a program that performs the following:
#    Opens the file 06.04 EmptyLinesInput.txt file for reading
#    Opens the file 06.04 EmptyLinesOutput.txt file for writing
#    Reads a line from the 06.04 EmptyLinesInput.txt file
#        If the line is not empty, write the line to 06.04 EmptyLinesOutput.txt
#        If the line is empty, do not write the line to 06.04 EmptyLinesOutput.txt
#Print the number of line read and the number of lines written.

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