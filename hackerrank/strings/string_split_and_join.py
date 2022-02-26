def split_and_join(line):
    line_list = line.split(" ")
    joined_string = "-".join(line_list)
    return joined_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

