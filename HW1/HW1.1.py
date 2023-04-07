import csv
from datetime import datetime
import os

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.timestamp}"

class Notes:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

        if os.path.isfile(self.file_path):
            with open(self.file_path, "r") as f:
                reader = csv.reader(f)
                for note_data in reader:
                    note = Note(note_data[0], note_data[1], note_data[2])
                    note.timestamp = note_data[3]
                    self.notes.append(note)

    def add(self, note):
        self.notes.append(note)
        self.save()

    def delete(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save()
                return True
        return False

    def edit(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                self.save()
                return True
        return False

    def list(self):
        return "\n".join([str(note) for note in self.notes])

    def save(self):
        with open(self.file_path, "w", newline='') as f:
            writer = csv.writer(f)
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.timestamp])

if __name__ == "__main__":
    notes = Notes("notes.csv")

    while True:
        print("\nМеню:")
        print("1. Добавить заметку;")
        print("2. Удалить заметку;")
        print("3. Редактировать заметку;")
        print("4. Список заметок;")
        print("5. Выход;")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            id = str(len(notes.notes) + 1)
            title = input("Введите заголовок: ")
            body = input("Введите содержимое заметки: ")
            note = Note(id, title, body)
            notes.add(note)
            print("Заметка создана!")
        elif choice == "2":
            note_id = input("Введите ID заметки: ")
            if notes.delete(note_id):
                print("Заметка удалена!")
            else:
                print("Заметка не найдена!")
        elif choice == "3":
            note_id = input("Введите ID заметки: ")
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое содержимое заметки: ")
            if notes.edit(note_id, new_title, new_body):
                print("Заметка изменена!")
            else:
                print("Заметка не найдена!")
        elif choice == "4":
            print(notes.list())
        elif choice == "5":
            break
        else:
            print("Некорректный ввод! Введите число от 1 до 5.")
