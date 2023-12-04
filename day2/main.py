def main():
    file = open("input/input.txt")
    content = file.readlines()
    
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    sum = 0
    power = 0
    
    for i, line in enumerate(content):
        split_col = line.strip().split(":")
        split_semi = split_col[1].strip().split(";")

        passed = True
        min_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        for draw in split_semi:
            individual_cube = draw.strip().split(",")

            for cube in individual_cube:
                processed_cube = cube.strip().split(" ")
                if (max_cubes[processed_cube[1]] < int(processed_cube[0])):
                    passed = False

                if (min_cubes[processed_cube[1]] < int(processed_cube[0])):
                    min_cubes[processed_cube[1]] = int(processed_cube[0])

        if passed:
            sum += 1 + i

        power += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

    print("Sum is: ", sum)
    print("Power is: ", power)




if __name__ == "__main__":
    main()