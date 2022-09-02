# читаем адресную книгу в формате CSV в список contacts_list
import regex as re
from func.func import change_name, change_number, concatenation_of_repeated_lines
from func.open_writer_func import open_csv, writer_csv


# TODO 1: выполните пункты 1-3 ДЗ
pattern_name = re.compile(r'\W+')
pattern_phone = re.compile(
    r'(\+7|8)[\s(]{0,3}(\d{3})[\s)-]{0,3}(\d{3})[-\s]{0,3}(\d{2})[-\s]{0,3}(\d{2})[\s(]{0,3}(доб\.)?[\s]?(\d+)?[\s)]?')
subs_phone = r'+7(\2)\3-\4-\5 \6\7'


if __name__ == "__main__":
    contacts_list = open_csv('phonebook_raw.csv')
    change_name(contacts_list, pattern_name)
    change_number(contacts_list, pattern_phone, subs_phone)
    result = concatenation_of_repeated_lines(contacts_list)
    writer_csv(result)





