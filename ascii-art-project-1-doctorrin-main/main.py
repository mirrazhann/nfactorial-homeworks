import sys
import argparse
import os



def main(align, output_file, text, file):
    print(f"Alignment: {align}")
    print(f"Output file: {output_file}")
    print(f"Text: {text}")
    print(f"File: {file}")

    symbols = dict()
    symbols = get_symbols()

    flags = {}
    if align != None and align != '':
        flags['align'] = align

    if output_file != None and output_file != '':
        flags['output_file'] = output_file

    if text != None:
        string_list = text.split('\\n')
        for line in string_list:
            string_process(line, symbols, file, flags)
    else:
        print_error(f"Enter text")
       


#  создаем словарь из символов и их строк в файле
def get_symbols():
    symbols = dict()
    line_start = 2
    for i in range(32, 127):
        ascii_code = i
        character = chr(ascii_code)
        # print(character) 
        symbols[character] = line_start
        line_start += 9
    return symbols

# есть ли нужный файл со шрифтом
def is_file_exist(filepath):
    if os.path.exists(filepath):
        return True
    else:
        return False

# имя файла
def get_filename(fontname):
    return fontname+".txt"

def string_process(str, symbols, fontname, flags):
    filename = get_filename(fontname)

    if str == '':
        print(str)
        return
    if len(symbols.items()) == 0:
        print_error("Empty symbols dictionary")
        return 
    if is_file_exist(filename) == False:
        print_error(f"File '{filename}' doesn`t exist")
        return 
    
    # ширина консоли
    if "align" in flags.keys():
        #получаем ширину
        console_width = get_console_width()
        print(f'Console width: {console_width}')
        flags['console_width'] = console_width
    
    # словарь символов построчно
    data = parsing_string(str, symbols)
    print_text(data, filename, flags)

    return 


def get_console_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 150  # Ширина по умолчанию


def print_text(data, filename, flags):
    # файл шрифтов
    with open(filename, 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    
    # файл для записи
    if "output_file" in flags.keys():
        file = open(flags['output_file'], "a", encoding="utf-8")

    for i, line in data.items():
        output = ''
        for j, line_number in line.items():
            if 0 < line_number <= len(file_lines):
                output += file_lines[line_number-1].replace('\n', '')

        # Если передали console_width
        if "align" in flags.keys():
            match flags['align']:
                case "center":
                    if "console_width" in flags.keys():
                        padding = int((flags['console_width'] - len(output))/2)
                        print(output.center(len(output)+padding, ' '), end="$\n")

                        if "output_file" in flags.keys():
                            text_format = output.center(len(output)+padding, ' ') + "$\n"
                            file.write(text_format)

                case "right":
                    if "console_width" in flags.keys():
                        padding = int((flags['console_width'] - len(output))/2)
                        print(output.rjust(len(output)+padding, ' '), end="$\n")

                        if "output_file" in flags.keys():
                            text_format = output.rjust(len(output) + padding, ' ') + "$\n"
                            file.write(text_format)
                        
                # case "justify":
                #     pass

                case _:
                    if "console_width" in flags.keys():
                        padding = int((flags['console_width'] - len(output))/2)
                        print(output.ljust(len(output)+padding, ' '), end="$\n")

                        if "output_file" in flags.keys():
                            text_format = output.ljust(len(output) + padding, ' ') + "$\n"
                            file.write(text_format)
            # print(padding)
            
    if "output_file" in flags.keys():
        file.close()
    return



def parsing_string(str, symbols):
    # словарь символов построчно
    result = {}
    for line in range (1, 9):
        result[line] = {}

        for char_p, char in enumerate(str):
            if line == 1 and char in symbols.keys():
                result[line][char_p] = symbols[char]
            else:
                result[line][char_p] = result[line-1][char_p]+1
    return result

def print_error(text):
    print("\033[31m{}\033[0;0m".format(text))



# string_process('Meruyert Bakimova', symbols, 'shadow')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASCII art project")
    parser.add_argument("--align", nargs="?", choices=["left", "center", "right", "justify"], default="left",
                        help="Specify text alignment: left, center, or right")
    parser.add_argument("--output", nargs="?", help="Save in file")
    parser.add_argument("text", nargs="?", help="Text to be processed")
    parser.add_argument("file", nargs="?", default="standard", help="Font file to be used")

    args = parser.parse_args()
  
    sys.argv[1].replace("\\", "")
    main(args.align, args.output, args.text, args.file)