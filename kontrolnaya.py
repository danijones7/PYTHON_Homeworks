import json
import datetime


class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def create_note(self, title, content):
        title = title.strip().lower()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = {"id": len(self.notes) + 1, "title": title,
                "content": content, "timestamp": timestamp}
        self.notes.append(note)
        self.save_notes()
        print("Note created.")

    def read_notes(self):
        for note in self.notes:
            print(
                f"\nID: {note['id']}\nTitle: {note['title']}\nContent: {note['content']}\nTimestamp: {note['timestamp']}\n{'='*20}")

    def read_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                print(
                    f"\nID: {note['id']}\nTitle: {note['title']}\nContent: {note['content']}\nTimestamp: {note['timestamp']}")
                return
            print("Note not found.")

    def read_notes_titles(self):
        for note in self.notes:
            print(
                f"\nID: {note['id']}\nTitle: {note['title']}\n{'='*20}")

    def get_notes_by_date_range(self, start_date, end_date):
        matching_notes = []
        for note in self.notes:
            note_timestamp = datetime.datetime.strptime(
                note['timestamp'], '%Y-%m-%d %H:%M:%S')
            if start_date <= note_timestamp and note_timestamp <= end_date:
                matching_notes.append(note)
        return matching_notes

    def edit_note_by_id(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                new_content = input("Enter new note content: ")
                note['content'] = new_content.strip()
                note['timestamp'] = datetime.datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print(f"\nNote {note_id} updated.")
                return
        print("\nNote not found.")

    def update_note_ids(self):
        for index, note in enumerate(self.notes):
            note['id'] = index + 1

    def delete_note_by_id(self, note_id):
        note_found = False
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                note_found = True
                self.update_note_ids()
                self.save_notes()
                print(f"\nNote {note_id} deleted.")
                break
        if not note_found:
            print("\nNote not found.")

    def delete_all_notes(self):
        self.notes = []
        self.save_notes()
        print("\nAll notes deleted.")

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f, indent=4)

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    notes_manager = NotesManager()

    while True:
        print("\nNote Manager\n")
        print("1. Create Note")
        print("2. Read All Notes")
        print("3. Read Note by ID")
        print("4. Read Notes - Titles")
        print("5. Select Notes by Date")
        print("6. Edit Note by ID")
        print("7. Delete Note by ID")
        print("8. Delete ALL Notes")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            notes_manager.create_note(title, content)
        elif choice == "2":
            notes_manager.read_notes()
        elif choice == "3":
            note_id = int(input("Enter note ID: "))
            notes_manager.read_note_by_id(note_id)
        elif choice == "4":
            notes_manager.read_notes_titles()

        elif choice == "5":
            start_date_str = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date_str = input("Enter end date (YYYY-MM-DD): ").strip()
            print(f"start_date_str: {start_date_str}")
            print(f"end_date_str: {end_date_str}")
            try:
                start_date = datetime.datetime.strptime(
                    start_date_str, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(
                    end_date_str + " 23:59:59", '%Y-%m-%d %H:%M:%S')
                selected_notes = notes_manager.get_notes_by_date_range(
                    start_date, end_date)
                if not selected_notes:
                    print("\nNo notes found in the selected date range.")
                else:
                    print("\nSelected Notes\n")
                    for note in selected_notes:
                        print(
                            f"ID: {note['id']}\nTitle: {note['title']}\nTimestamp: {note['timestamp']}\n{'='*20}")
            except ValueError as e:
                print("Invalid date format. Please use YYYY-MM-DD.")
                print(f"Error details: {e}")

        elif choice == "6":
            note_id = int(input("Enter note ID to edit: "))
            notes_manager.edit_note_by_id(note_id)
        elif choice == "7":
            note_id = int(input("Enter note ID to delete: "))
            notes_manager.delete_note_by_id(note_id)
        elif choice == "8":
            print(
                "This action can not be undone. Are you sure you want to delete ALL notes?")
            confirm = input("Press 1 to Confirm\n Press 2 to Cancel: ")
            if confirm == "1":
                notes_manager.delete_all_notes()
            else:
                print("\nOperation cancelled.")
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select a valid option.")
