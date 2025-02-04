import sqlite3

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()

    while True:
        # Ask the user for a hash to search
        hash_to_find = input("Enter the hash to find (or type 'exitexit1423' to quit): ").strip()

        # If the user wants to exit the program
        if hash_to_find.lower() == 'exitexit1423':
            print("Exiting...")
            break

        # Search for the hash in the database
        cursor.execute("SELECT word FROM words WHERE hash = ?", (hash_to_find,))
        result = cursor.fetchall()

        if result:
            # If multiple words match, join them with commas
            words = [row[0] for row in result]
            print(f"Word(s) found: {', '.join(words)}")
        else:
            print("Hash not found in the database.")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
