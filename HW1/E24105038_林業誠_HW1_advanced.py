# Load all dictionaries into a single set
def load_dictionaries(file_paths):
    dictionary = set()
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                dictionary.add(line.strip())  # Remove spaces or newlines
    return dictionary

# Define delimiters (sorted by length for precedence)
delimiters_set = ["……", "。", "？", "！", "：", "；", "，", "「", "」", "《", "》", "、"]

# Longest Word Matching Segmentation
def longest_word_matching(sentence, dictionary, delimiters):
    words = []
    i = len(sentence)  # Start from the end of the sentence
    
    while i > 0:
        # Check for delimiters first
        delimiter_found = False
        for delimiter in delimiters:
            if sentence[i - len(delimiter):i] == delimiter:  # Match longer delimiters first
                words.append(delimiter)
                i -= len(delimiter)
                delimiter_found = True
                break  
        
        if delimiter_found:
            continue  

        # Perform longest word matching 
        max_word = None
        match_start = i - 1 # Start to check whether previous char + current char will have a word in dictionary
        for j in range(match_start, -1, -1):  # Read in reverse order
            if sentence[j:i] in dictionary:
                max_word = sentence[j:i]  # Store the longest match
                match_start = j  # Update the match starting point
        
        if max_word:
            words.append(max_word)
            i = match_start  # Move pointer back to where the match started
        else:  # Single word segmentation if no match
            words.append(sentence[i - 1])
            i -= 1
    
    return words[::-1]  # Reverse the list to restore the correct order

# Save segmentation result to file
def save_output(file_name, segmented_words):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(', '.join(f'"{word}"' for word in segmented_words))  # Format as "word", "word"

### Main 
dictionary_paths = ["chinese_dictionary.txt", "taiwanese_dictionary.txt", "hakka_dictionary.txt"]
input_text = "今天的天氣很好，我們一起去公園散步吧。人工智慧正在改變世界，未來的發展令人期待。今仔日个天氣真好，阮來去公園遛跤。人工智慧當咧改變世界，將來个發展誠期待。今晡日个天氣當好，等下我哋去公園行下。人工智能正改變世界，後日个發展分人期待。"

# Load dictionaries
dictionary = load_dictionaries(dictionary_paths)

# Perform segmentation
segmented_result = longest_word_matching(input_text, dictionary, delimiters_set)

# Print and save output
print(segmented_result)
save_output("E24105038_林業誠_HW1_advanced.txt", segmented_result)
