with open("06.05 CompareFileA.txt") as FileA, open("06.05 CompareFileB.txt") as FileB:
    A = FileA.readline()
    B = FileB.readline()

    line = 0
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
        
