def read_file(filename):
    with open(filename,'r') as f :
        lines = []
        for line in f :
            lines.append(line.strip())
            # if 'Allen,Tom' in line:
            #     continue
    return lines

def covert(lines):
    new = []
    person = None #避免person是空值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line )
    return new

def write_file(filename, lines):
    with open(filename,'w') as f:
        for line in lines :
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    # print(message)
    lines = covert(lines)
    write_file('output.txt',lines)
    
main()