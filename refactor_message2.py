def read_file(filename):
    with open(filename,'r') as f :
        lines = []
        for line in f :
            lines.append(line.strip())
    return lines

def covert(lines):
    person = None
    rita_words_count = 0
    yufi_words_count = 0
    for line in lines:
      s = line.split(' ')
      time = s[0]
      name = s[1]
      if name == 'Rita':
          for message in s[2:]:
            rita_words_count += len(message)
      elif name == 'yufi':
          for message in s[2:]:
            yufi_words_count += len(message)
    print('rita說了',rita_words_count ,'個字')
    print('yufi說了',yufi_words_count,'個字')
    
    #   print(s[0])

def write_file(filename, lines):
    with open(filename,'w') as f:
        for line in lines :
            f.write(line + '\n')


def main():
    lines = read_file('line_input.txt')
    # print(message)
    lines = covert(lines)
    # write_file('output.txt',lines)
    
main()