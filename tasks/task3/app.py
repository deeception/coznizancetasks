with open('about.txt', 'r') as file:

    content = file.read()

    words = content.split()
    words_6 = [word for word in words if len(word) >= 6]

    word_freq = {}
    for word in words_6:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    most_freq_word = max(word_freq, key=word_freq.get)

    print("Words with at least 6 letters:", words_6)
    print("Most frequently used word:", most_freq_word)
