
def day_one():
    input_file = open("InputFiles/day_one.txt")

    resultado = 0

    for line in input_file:
        first_digit, last_digit = "", ""
        first_digit_found = False

        for character in line:
            
            if (not first_digit_found and character in [str(num) for num in list(range(10))]):
                first_digit_found = True
                first_digit = character
            
            elif(character in [str(num) for num in list(range(10))]):
                last_digit = character

        if (first_digit == ""):
            continue

        elif (last_digit == ""):
            last_digit = first_digit

        resultado += int(first_digit + last_digit)

    print("Resultado del dia 1: ", resultado)

def day_two():
    input_file = open("InputFiles/day_two.txt")

    permited_red_cubes = 12
    permited_green_cubes = 13
    permited_blue_cubes = 14

    result_1 = 0
    result_2 = 0

    for line in input_file:
        biggest_red = 0
        biggest_green = 0
        biggest_blue = 0
        id, game  = line.split(":")
        
        id = id.split(" ")[1]

        sets = game.split(";")
        allowed = True

        for s in sets:
            cubes  = s.split(",")

            for cube in cubes:

                cleaned_cube = cube.strip()
                amount, color = cleaned_cube.split(" ")

                amount = int(amount)

                if (color == "red"):

                    if (amount > biggest_red):
                        biggest_red = amount

                    if (amount > permited_red_cubes):
                        allowed = False
                        

                elif (color == "green"):

                    if (amount > biggest_green):
                        biggest_green = amount          

                    if (amount > permited_green_cubes):
                        allowed = False
                        

                elif (color == "blue"):

                    if (amount > biggest_blue):
                        biggest_blue = amount   

                    if (amount > permited_blue_cubes):
                        allowed = False
                        
        result_2 += biggest_blue * biggest_green * biggest_red
        if (allowed):
            result_1 += int(id)
    
    print("Resultado del dia 2 parte 1: ", result_1)
    print("Resultado del dia 2 parte 2: ", result_2)


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


    print("Resultado del día 3 parte: ", result)



    # print(engine_esq[0][1])


if __name__ == "__main__":

    # day_one()
    day_two()
    day_three()