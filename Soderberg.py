file_name = 'data/pi_digits.txt'
with open(file_name) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    for line in file_object:
        print(line)
