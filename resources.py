import json
import os
from test_json import entry

def print_with_indent(value, indent=0):
    indentation = indent * ' '
    print(f"{indentation}{value}")

class Entry():
    def __init__(self, title, entries=None, parent=None):
        if entries == None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent
    def __str__(self):
        return self.title
    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent+1)
    def json(self):
        res = {'title':self.title, 'entries': [x.json() for x in self.entries]}
        return res
    @classmethod
    def entry_from_json(cls, value:dict):
        new_entry = Entry(value['title'])
        for item in value['entries']:
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry

    def save(self, path):
        with open(os.path.join(path, f'{self.title}.json'), 'w', encoding='utf-8') as file:
            json.dump(self.json(), file)

    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            file_dict = json.load(file)
            return cls.from_json(file_dict)

# new_entry = Entry.entry_from_json(entry)
# new_entry.print_entries()
# print(new_entry.json())
# new_entry.save(r'C:\Users\User\PycharmProjects\file.json')
