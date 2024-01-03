
def day_three():

    input_file = open("InputFiles/day_three.txt")

    numbers = [str(num) for num in range(10)]
    result = 0
    engine_esq = [] 
    part_numbers = []

    for line in input_file:
        engine_esq.append(list(line))

    current_number = ""
    i,j = 0, 0
    for row in engine_esq:
        j = 0
        num_index = []
        for e in row:

            if e in numbers:
                current_number = current_number + e
                num_index.append((i,j))

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
                        part_numbers.append({"num":int(current_number), "indexes": num_index})

                    current_number = ""
                    num_index = []

            j += 1
        
        i += 1

    result_2 = 0
    i,j = 0,0
    for row in engine_esq:
        j = 0
        for e in row:
            if e == "*":
                
                valid = False
                indexes = [(i,j+1), (i, j-1), (i+1, j+1), (i+1, j), (i+1, j-1), (i-1, j+1), (i-1, j), (i-1, j-1)]
                gears = []

                for part_num in part_numbers:

                    br = False
                    for ind in indexes:
                    
                        if ind in part_num["indexes"]:
                            gears.append(part_num["num"])
                            br = True
                            break
                    
                if len(gears) == 2:
                    result_2 += gears[0]*gears[1]

            j += 1

        i += 1

    print("Resultado del día 3 parte 1: ", result)
    print("Resultado del día 3 parte 2:", result_2)

