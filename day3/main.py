def main():
    file = open("input/input.txt")
    content = file.readlines()
    num_rows_idx = len(content) - 1 # length to last idx
    
    sum = 0
    
    for row, line in enumerate(content):
        col = 0
        line_striped = line.strip()
        num_col_idx = len(line_striped) - 1

        while col <= num_col_idx:
            if (line[col].isnumeric()):
                min_row = max(0, row - 1)
                max_row = min(num_rows_idx, row + 1)

                min_col = max(0, col - 1)
                max_col = col
                while(max_col < num_col_idx):
                    if line[max_col].isnumeric():
                        max_col += 1
                    else:
                        break

                is_valid = False
                for i in range(min_row, max_row+1):
                    for j in range(min_col, max_col+1):
                        if content[i][j] != '.' and not content[i][j].isnumeric():
                            is_valid = True
                
                if max_col == num_col_idx and content[row][max_col].isnumeric():
                    max_col += 1

                num = int(line_striped[col:max_col])

                if is_valid:  
                    sum += num

                col = max_col
            else:
                col += 1

    print("Sum is: ", sum)

if __name__ == "__main__":
    main()