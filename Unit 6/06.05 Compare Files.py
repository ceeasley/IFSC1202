#You have a two files. You want to compare them line by line and print the differences.
#Create a program that performs the following:
#    Opens the file 06.05 CompareFileA.txt file for reading
#    Opens the file 06.05 CompareFileB.txt file for reading
#    Read a line from both files
#    If the line from both files is not the same, print the line number and the contents of both lines
#    Print the number of differences

with open("06.05 CompareFileA.txt") as FileA, open("06.05 CompareFileB.txt") as FileB:
    A = FileA.readline()
    B = FileB.readline()

    line = 1
    difference = 0

    while A:
        while B:
            if A != B:
                line +=1
                difference += 1
                print(f'Line: {line} - File A: {A}\nLine: {line} - File B: {B}')
            else:
                line +=1
            A = FileA.readline()
            B = FileB.readline()
            
print(f'{difference} differences')
        
