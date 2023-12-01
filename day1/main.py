def findspelleddigits(line):
    spelled_digits = ["one","two","three","four","five","six","seven","eight","nine"]

    first_idx = -1
    first_digit = 0
    last_idx = -1
    last_digit = 0
    
    for i, spell_dig in enumerate(spelled_digits):
        low_idx = line.find(spell_dig)
        high_idx = line.rfind(spell_dig)
        if low_idx != -1:
            if first_idx == -1:
                first_idx = low_idx
                first_digit = str(i + 1)
                last_idx = high_idx
                last_digit = str(i + 1)
            else:
                if low_idx < first_idx:
                    first_idx = low_idx
                    first_digit = str(i + 1)
            
                if high_idx > last_idx:
                    last_idx = high_idx
                    last_digit = str(i + 1)

    return [first_idx, first_digit, last_idx, last_digit]

def finddigitidx(line):
    first_idx = -1
    first_digit = '0'
    last_idx = -1
    last_digit = '0'
    for i, charater in enumerate(line):
        if charater.isnumeric():
            if first_idx == -1:
                first_digit = charater
                last_digit = charater
                first_idx = i
                last_idx = i
            else:
                last_digit = charater
                last_idx = i

    return [first_idx, first_digit, last_idx, last_digit]

def main():
    file = open("input/input.txt")
    content = file.readlines()

    sum = 0
    
    for i, line in enumerate(content):
        # print("Processing line: ", i+1)
        spelled_indicies = findspelleddigits(line)
        actual_indicies = finddigitidx(line)

        if spelled_indicies[0] == -1 and actual_indicies[0] == -1:
            continue

        if spelled_indicies[0] == -1:
            first_char = actual_indicies[1]
            last_char = actual_indicies[3]
        elif actual_indicies[0] == -1:
            first_char = spelled_indicies[1]
            last_char = spelled_indicies[3]
        else:
            if actual_indicies[0] < spelled_indicies[0]:
                first_char = actual_indicies[1]
            else:
                first_char = spelled_indicies[1]

            if actual_indicies[2] > spelled_indicies[2]:
                last_char = actual_indicies[3]
            else:
                last_char = spelled_indicies[3]
        
        num_str = first_char + last_char
        print(num_str)
        sum += int(num_str)

    print("Sum is ", sum)

if __name__ == "__main__":
    main()