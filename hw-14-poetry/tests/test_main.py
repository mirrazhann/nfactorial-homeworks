import sys
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import parse_arguments, get_symbols, get_filename, string_process

@pytest.fixture
def flags():
    return {'align': 'left'}

@pytest.fixture
def symbols():
    return {chr(i): 9 * (i - 32) + 2 for i in range(32, 127)}

@pytest.fixture
def my_str():
    return 'HeLLo'

@pytest.fixture
def p_string(my_str, symbols):
    # словарь символов построчно
    p_str = {}
    for line in range (1, 9):
        p_str[line] = {}

        for char_p, char in enumerate(my_str):
            if line == 1 and char in symbols.keys():
                p_str[line][char_p] = symbols[char]
            else:
                p_str[line][char_p] = p_str[line-1][char_p]+1
    return p_str


def test_get_filename():
    assert get_filename("shadow") == "shadow.txt"
    assert get_filename("__") == "__.txt"
    assert get_filename("") == ".txt"


def test_get_symbols(symbols):
    assert get_symbols() == symbols


def test_parse_arguments(monkeypatch, my_str):
    test_args = ["program_name", "--align", "center", "--output", "output.txt", my_str, "fontfile"]
    # test_args = ["program_name", "Hello", "fontfile"]
    monkeypatch.setattr("sys.argv", test_args)
    args = parse_arguments()
    assert args.align == "center"
    # assert args.align == "left"
    assert args.output == "output.txt"
    # assert args.output == None
    assert args.text == "HeLLo"
    assert args.file == "fontfile"

# тут я так и не поняла, почему получаю ошибку Expected: print_text('standard')
@patch('main.get_filename', return_value = 'standard.txt')
@patch('main.is_file_exist', return_value = True)
@patch('main.get_console_width', return_value = 270)
@patch('main.parsing_string', return_value = {1: {0: 362, 1: 623, 2: 398, 3: 398, 4: 713}, 2: {0: 363, 1: 624, 2: 399, 3: 399, 4: 714}, 3: {0: 364, 1: 625, 2: 400, 3: 400, 4: 715}, 4: {0: 365, 1: 626, 2: 401, 3: 401, 4: 716}, 5: {0: 366, 1: 627, 2: 402, 3: 
402, 4: 717}, 6: {0: 367, 1: 628, 2: 403, 3: 403, 4: 718}, 7: {0: 368, 1: 629, 2: 404, 3: 404, 4: 719}, 8: {0: 369, 1: 630, 2: 405, 3: 405, 4: 720}})
@patch('main.print_text', return_value = True)
def test_string_process__valid_datas(mock_get_filename, mock_is_file_exist, mock_get_console_width, mock_parsing_string, mock_print_text, my_str, symbols, flags, p_string):
    print(p_string)
    string_process(my_str, symbols, "standard", flags)
    
    # Проверяем вызовы зависимых функций
    mock_get_filename.assert_called_once_with('standard') 
    mock_is_file_exist.assert_called_once_with('standard.txt') 
    mock_get_console_width.assert_called_once_with() 
    mock_parsing_string.assert_called_once_with(my_str, symbols) 
    mock_print_text.assert_called_once_with(p_string, 'standard.txt', flags)



    