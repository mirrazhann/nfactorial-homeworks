def load_ascii_mapping(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    ascii_mapping = {}
    current_char = None
    ascii_art = []
    
    for line in lines:
        # Пустая строка обозначает окончание ASCII-графики символа
        if line.strip() == '' and ascii_art:
            ascii_mapping[current_char] = ''.join(ascii_art)
            ascii_art = []
            current_char = None
        elif line.strip() and current_char is None:
            # Начало нового символа
            current_char = line.strip()
        elif current_char:
            # Добавляем строку ASCII-графики к текущему символу
            ascii_art.append(line)

    return ascii_mapping

def ascii_art_from_string(input_string, ascii_mapping):
    result = []
    for char in input_string:
        if char in ascii_mapping:
            result.append(ascii_mapping[char])
        else:
            result.append(char)  # Неизвестный символ оставляем без изменений
    return '\n'.join(result)

if __name__ == "__main__":
    ascii_mapping = load_ascii_mapping('standard.txt')
    user_input = input("Введите строку: ")
    result = ascii_art_from_string(user_input, ascii_mapping)
    print(result)
