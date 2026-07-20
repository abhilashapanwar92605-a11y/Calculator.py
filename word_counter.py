try:
    # Open the text file
    with open("Sample.txt", "r") as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Count the number of words
    word_count = len(words)

    # Display the content and word count
    print("File Content:")
    print(content)
    print("\nTotal Number of Words:", word_count)

except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.")

except Exception as e:
    print("An error occurred:", e)