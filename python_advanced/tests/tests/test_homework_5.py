import unittest
from unittest.mock import patch
from Netology.python_advanced.tests.homework_5 import documents, directories
from Netology.python_advanced.tests.homework_5 import whose_docs, doc_in_shelf, share_docs, add_docs, del_doc


class TestFunction(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('start to test')

    def test_get_all_doc_owners_name(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = whose_docs(documents)
            self.assertEqual("Владелец документа - Василий Гупкин\n", result)
    def test_whose_docs(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = f"Владелец документа - Василий Гупкин\n"
            self.assertMultiLineEqual(whose_docs(documents), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f"Документ отсутствует.\n"
            self.assertMultiLineEqual(whose_docs(documents), result)

    def test_doc_in_shelf(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = f"Документ хранится на полке - 1\n"
            self.assertMultiLineEqual(doc_in_shelf(directories), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f"Документ отсутствует.\n"
            self.assertMultiLineEqual(doc_in_shelf(directories), result)

    def test_share_docs(self):
        self.assertIsInstance(share_docs(documents), list)

    def test_add_docs(self):
        with patch('builtins.input', return_value='1'):
            assert input() == '1'
            result = f'Документ уже существует\n'
            new_document = {
                'type': 'passport',
                'number': '11-2',
                'name': 'Витайлий Паравозов'
            }
            self.assertMultiLineEqual(add_docs(documents, directories, new_document), result)

    def test_del_doc(self):
        with patch('builtins.input', return_value='11-2'):
            assert input() == '11-2'
            result = f'Удаление прошло успешно.\n'
            self.assertMultiLineEqual(del_doc(documents, directories), result)


if __name__ == "__main__":
    unittest.main()
