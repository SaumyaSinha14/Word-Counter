def get_user_input():
    """Function to get text input from the user."""
    text = input("Enter the text you want to count words for:\n")
    return text

def count_words(text):
    """Function to count the number of words in a given text."""
    words = text.split()  # Splits the text into a list of words
    return len(words)

def display_word_count(count):
    """Function to display the word count."""
    print(f"The number of words in the given text is: {count}")

def main():
    """Main function to execute the program's logic."""
    print("Welcome to the Word Counter Program!")
    user_text = get_user_input()  # Step 1: Input Handling
    word_count = count_words(user_text)  # Step 2: Processing
    display_word_count(word_count)  # Step 3: Output

# Execute the main function
if __name__ == "__main__":
    main()
