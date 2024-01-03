
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
