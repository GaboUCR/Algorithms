
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

