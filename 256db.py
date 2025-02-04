import sqlite3
import hashlib

def main():
    # Ask for words.txt location
    file_path = input("Enter the path to words.txt: ")

    # Open the words.txt file
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    # Connect to SQLite database (it will create words.db if it doesn't exist)
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        word TEXT PRIMARY KEY,
        hash TEXT NOT NULL
    )
    """)

    # Prepare the insert statement
    insert_stmt = "INSERT OR IGNORE INTO words (word, hash) VALUES (?, ?)"

    # Process each word, generate hash and store in DB
    for word in words:
        word = word.strip()  # Remove any extra newlines or spaces
        if word:
            hash_value = generate_sha256_hash(word)
            cursor.execute(insert_stmt, (word, hash_value))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Hashes successfully stored in words.db!")

# Function to generate SHA-256 hash
def generate_sha256_hash(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    main()
