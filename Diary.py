from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    # content
    # timestamp

    class Meta:
        database = db


def menu_loop():
    '''Show the menu'''


def add_entry():
    '''Add an entry.'''


def view_entries():
    '''view previous entries'''


def delete_entry(entry):
    '''Delete and entry'''


if __name__ == '__main__':
    menu_loop()
