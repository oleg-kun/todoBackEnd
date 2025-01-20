from resources import Entry
import os


class EntryManager():
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for file in os.listdir(self.data_path):
            if file.endswith('json'):
                loaded_entry = Entry.load(os.path.join(self.data_path, file))
                self.entries.append(loaded_entry)

    def add_entry(self, title: str):
        self.entries.append(Entry(title))




