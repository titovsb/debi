import os.path
import sys

class Document:
    def __init__(self):
        pass

    @staticmethod
    def is_letter_exists(inn)->bool:
        tmp =os.path.join(os.path.abspath(), setup.EXPORT_LETTERS_PATH);
        print(tmp)

if __name__ == '__main__':
    Document.is_letter_exists()

