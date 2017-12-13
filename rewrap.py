def rewrap(path, max_width, max_lines):
    with open(path) as file:
        width = 0
        lines = 0
        for line in file:
            for word in line.split() or ['']:  # note: word '' indicates a blank line!
                if word and width > 0 and width + len(word) < max_width:
                    print(' ', end='')  # prints a space without a newline
                    width += 1
                elif width > 0 or lines > 0:
                    print('')  # prints a newline
                    width = 0
                    lines += 1
                    if lines >= max_lines: return
                print(word, end='')  # prints the word without a newline
                width += len(word)

if __name__ == '__main__':
    rewrap('1342.txt', 40, 200)
