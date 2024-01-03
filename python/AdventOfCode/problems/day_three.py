
def day_three():

    input_file = open("InputFiles/day_three.txt")

    numbers = [str(num) for num in range(10)]
    result = 0
    engine_esq = [] 

    for line in input_file:
        engine_esq.append(list(line))

    current_number = ""
    i,j = 0, 0
    for row in engine_esq:
        j = 0
        for e in row:

            if e in numbers:
                current_number = current_number + e

            else:
                
                if current_number != "":

                    valid = False

                    indexes = [(i,j), (i, j-len(current_number)-1)]

                    indexes = indexes + [(i+1, new_j) for new_j in range(j-len(current_number)-1, j+1, 1)]#adding the lower elements

                    indexes = indexes + [(i-1, new_j) for new_j in range(j-len(current_number)-1, j+1, 1)]#adding the upper relements
                    
                    for index in indexes:

                        try:
                            element = engine_esq[index[0]][index[1]]
                        
                        except IndexError:
                            continue

                        if ( element != "." and element != "\n" and element not in numbers):
                            valid = True
                            continue

             
                    if valid==True:
                        result += int(current_number)

                    current_number = ""

            j += 1
        
        i += 1


    print("Resultado del día 3 parte 1: ", result)


