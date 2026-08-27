while True:
    text = input("Input your text (or 'Q' to quit): ")

    if text.upper() == 'Q':
        break

    words = text.split()

    word_count = len(words)

    print(f"Word count: {word_count}")