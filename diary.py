#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they dont exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry."""
    print("Enter your entry. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input("Save entry? [Yn] ").lower() != 'n':
            Entry.create(content=data)
            print("Entry saved successfully")


def view_entries():
    """view previous entries"""


def delete_entry(entry):
    """Delete and entry"""


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])


if __name__ == '__main__':
    initialize()
    menu_loop()
