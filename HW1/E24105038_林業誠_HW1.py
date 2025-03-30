"""
> Store all words from the dictionary txt into a set
> Using a set allows O(1) in checking a wrod
"""
"""
Match the longest word by reading in reverse order to let characters matching with more suitable characters
>> The result is better than reading in the regular order
"""
# Load the dictionary
def load_dictionary(file_path):
    dictionary = set()
    with open(file_path, 'r', encoding='utf-8') as file:  # Set encoding to prevent garbled text
        for line in file:
            dictionary.add(line.strip())  # Remove extra spaces or newlines
    return dictionary

# Define delimiters (sorted by length for precedence)
delimiters_set = ["……", "。", "？", "！", "：", "；", "，", "「", "」", "《", "》", "、"]

# Longest Word Matching Segmentation with Delimiters
def longest_word_matching(sentence, dictionary, delimiters):
    words = []
    i = len(sentence)  # Start from the end of the sentence

    while i > 0:
        # Check for delimiters first
        delimiter_found = False
        for delimiter in delimiters:
            if sentence[i - len(delimiter):i] == delimiter:  # Match from the end
                words.append(delimiter)
                i -= len(delimiter)
                delimiter_found = True
                break  

        if delimiter_found:
            continue  

        # Perform longest word matching (Check normally from left to right)
        max_word = None
        match_start = i - 1  # Start to check whether previous char + current char will have a word in dictionary
        for j in range(match_start, -1, -1):  # Read in reverse order
            if sentence[j:i] in dictionary:
                max_word = sentence[j:i]  # Store the longest match
                match_start = j  # Update the match starting point

        if max_word:
            words.append(max_word)
            i = match_start  # Move pointer back to where the match started
        else:  # Single word and those words that dont exist in dictionary will also be segmented as single word
            words.append(sentence[i - 1])
            i -= 1

    return words[::-1]  # Reverse the list to restore the correct order


# Save segmentation result to file
def save_output(file_name, segmented_words):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(', '.join(f'"{word}"' for word in segmented_words)) # Output format: "word" "word" (after segmented)

### Main 
dictionary_path = "chinese_dictionary.txt"  
#input_text = "吳德榮指出，明日會有中層水氣通過，中部以北雲量稍增、局部山區偶有零星飄小雨的機率，很不明顯，其他各地多雲時晴；周四中層水氣東移，雲量逐漸減少，天氣穩定。周三、周四都是北舒適南微熱、早晚涼，易起霧的天氣。吳德榮分析，周五起至下周一白天晴朗穩定，本島各地區最高氣溫皆升至30度以上，各地白天暖如夏，易起霧。下周一晚間鋒面接近，大氣趨不穩定，有對流發生的機率；下周二鋒面通過伴隨降雨，冷空氣南下、氣溫驟降，應特別注意氣溫的劇烈變化。"  
input_text = "吳德榮指出，明日會有中層水氣通過，中部以北雲量稍增、局部山區偶有零星飄小雨的機率，很不明顯，其他各地多雲時晴；周四中層水氣東移，雲量逐漸減少，天氣穩定。周三、周四都是北舒適南微熱、早晚涼，易起霧的天氣。" 
#input_text = "……,？！：；，「」《》、"

# Load dictionary
dictionary = load_dictionary(dictionary_path)

# Perform segmentation
segmented_result = longest_word_matching(input_text, dictionary, delimiters_set)

# Print and save output
print(segmented_result)
save_output("E24105038_林業誠_HW1.txt", segmented_result)


"""
Segmentation method with declaring delimiters set
>> The result is not good
"""
# # Load the dictionary
# def load_dictionary(file_path):
#     dictionary = set()
#     with open(file_path, 'r', encoding='utf-8') as file:  # Set encoding to prevent garbled text
#         for line in file:
#             dictionary.add(line.strip())  # Remove extra spaces or newlines
#     return dictionary

# # Define delimiters (sorted by length for precedence)
# delimiters_set = ["……", "。", "？", "！", "：", "；", "，", "「", "」", "《", "》", "、"]

# # Longest Word Matching Segmentation with Delimiters
# def longest_word_matching(sentence, dictionary, delimiters):
#     words = []
#     i = 0
#     while i < len(sentence):
#         # Check for delimiters first
#         delimiter_found = False
#         for delimiter in delimiters:
#             if sentence[i:].startswith(delimiter):  # Match longer delimiters first
#                 words.append(delimiter)
#                 i += len(delimiter)
#                 delimiter_found = True
#                 break  # Stop checking once a delimiter is found
        
#         if delimiter_found:
#             continue  # Skip word matching if a delimiter was matched

#         # Perform longest word matching
#         max_word = None
#         for j in range(i + 1, len(sentence) + 1):  # Check the longest word 
#             if sentence[i:j] in dictionary:
#                 max_word = sentence[i:j]  # Find the longest match

#         if max_word:
#             words.append(max_word)
#             i += len(max_word)  # Move pointer forward
#         else: # Single word and those words that dont exist in dictionary will also be segmented as single word
#             words.append(sentence[i])  
#             i += 1
#     return words

# # Save segmentation result to file
# def save_output(file_name, segmented_words):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(', '.join(f'"{word}"' for word in segmented_words)) # Output format: "word" "word" (after segmented)

# ### Main 
# dictionary_path = "chinese_dictionary.txt"  
# #input_text = "吳德榮指出，明日會有中層水氣通過，中部以北雲量稍增、局部山區偶有零星飄小雨的機率，很不明顯，其他各地多雲時晴；周四中層水氣東移，雲量逐漸減少，天氣穩定。周三、周四都是北舒適南微熱、早晚涼，易起霧的天氣。吳德榮分析，周五起至下周一白天晴朗穩定，本島各地區最高氣溫皆升至30度以上，各地白天暖如夏，易起霧。下周一晚間鋒面接近，大氣趨不穩定，有對流發生的機率；下周二鋒面通過伴隨降雨，冷空氣南下、氣溫驟降，應特別注意氣溫的劇烈變化。"  
# input_text = "吳德榮指出，明日會有中層水氣通過，中部以北雲量稍增、局部山區偶有零星飄小雨的機率，很不明顯，其他各地多雲時晴；周四中層水氣東移，雲量逐漸減少，天氣穩定。周三、周四都是北舒適南微熱、早晚涼，易起霧的天氣。⋯⋯" 
# #input_text = "……,？！：；，「」《》、"

# # Load dictionary
# dictionary = load_dictionary(dictionary_path)

# # Perform segmentation
# segmented_result = longest_word_matching(input_text, dictionary, delimiters_set)

# # Print and save output
# print(segmented_result)
# save_output("E24105038_林業誠_HW1.txt", segmented_result)


"""
Basic segmentation method without declare delimiters set
>> Cannot segment "……" into one part, only can segment it to "…" "…" two parts
"""

# # Load the dictionary
# def load_dictionary(file_path):
#     dictionary = set() 
#     with open(file_path, 'r', encoding='utf-8') as file:   # Set encoding to prevent garbled text
#         for line in file:
#             dictionary.add(line.strip())  # Remove extra spaces or newlines
#     return dictionary

# # Longest Word Matching Segmentation
# def longest_word_matching(sentence, dictionary):
#     words = []
#     i = 0
#     while i < len(sentence):
#         max_word = None
#         for j in range(i + 1, len(sentence) + 1):  # Check the longest word 
#             if sentence[i:j] in dictionary:
#                 max_word = sentence[i:j]  # Find the longest match
#         if max_word: # More than 1 word
#             words.append(max_word)
#             i += len(max_word)  # Move pointer forward
#         else: # Single word and those words that dont exist in dictionary will also be segmented as single word
#             words.append(sentence[i])  
#             i += 1
#     return words

# # Save segmentation result to file
# def save_output(file_name, segmented_words):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(', '.join(f'"{word}"' for word in segmented_words)) # Output format: "word" "word" (after segmented)

# ### Main 
# dictionary_path = "chinese_dictionary.txt"  
# #input = "吳德榮指出，明日會有中層水氣通過，中部以北雲量稍增、局部山區偶有零星飄小雨的機率，很不明顯，其他各地多雲時晴；周四中層水氣東移，雲量逐漸減少，天氣穩定。周三、周四都是北舒適南微熱、早晚涼，易起霧的天氣。吳德榮分析，周五起至下周一白天晴朗穩定，本島各地區最高氣溫皆升至30度以上，各地白天暖如夏，易起霧。下周一晚間鋒面接近，大氣趨不穩定，有對流發生的機率；下周二鋒面通過伴隨降雨，冷空氣南下、氣溫驟降，應特別注意氣溫的劇烈變化。"  
# input = "……"
# # Load dictionary
# dictionary = load_dictionary(dictionary_path)

# # Perform segmentation
# segmented_result = longest_word_matching(input, dictionary)

# # Print and save output
# print(segmented_result)
# save_output("E24105038_林業誠_HW1.txt", segmented_result)
