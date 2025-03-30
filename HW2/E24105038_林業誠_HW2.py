import requests
import json

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None 

def extract_entitles(input, output):
    if not output: 
        return None
    
    # Retrieving data from the output(dictionary)
    ### Syntax rule: .get("dictionary_key, default"), [0] returns the first list cuz it is nested list
    words = output.get("ws", [[]])[0]
    entities = output.get("pos", [[]])[0]
    
    # Creating a dictionary
    extracted_answer = {
        "people" : [],  # Creating list
        "time" : [],
        "places" : [],  
        "objects" : [],
        "simplified_events" : []
    }

    index = 0
    verb_stack = []     # Stack to store verbs
    # Looping 
    ### zip() : pairs corresponding elements from words and pos
    for word, entity in zip(words, entities):
        
        start_index = input.find(word, index)   # Find the word in the input from index onward
        end_index = start_index + len(word)
        index = end_index

        word_info = (word ,start_index, end_index)

        if entity == "Nb":
            extracted_answer["people"].append(word_info)
        elif entity == "Nd":
            extracted_answer["time"].append(word_info)
        elif entity == "Nc":
            extracted_answer["places"].append(word_info)
        elif entity == "Na":
            extracted_answer["objects"].append(word_info)
            if verb_stack:
                last_verb = verb_stack.pop()
                simplified_event = last_verb + word
                extracted_answer["simplified_events"].append(simplified_event)
        elif entity in ["VCL", "VJ"]:
            verb_stack.append(word)
        elif entity == "VC":
            if verb_stack:
                last_verb = verb_stack.pop()
                simplified_event = last_verb + word
                extracted_answer["simplified_events"].append(simplified_event)
            else:
                verb_stack.append(word)
        

    return extracted_answer

def save_output(file_name, output):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Extracted Entities:\n")     # file.write only works with string
        file.write("人名: " + str(extracted_answer["people"]) + "\n")
        file.write("時間: " + str(extracted_answer["time"]) + "\n")
        file.write("地點: " + str(extracted_answer["places"]) + "\n")
        file.write("物件: " + str(extracted_answer["objects"]) + "\n")
        file.write("精簡事件： " + str(extracted_answer["simplified_events"]) + "\n")

if __name__ == "__main__":
    token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZCI6ODI1LCJzZXJ2aWNlX2lkIjoiMSIsImV4cCI6MTc1NjE4NjgxMywic3ViIjoiIiwidXNlcl9pZCI6IjUyNSIsInZlciI6MC4xLCJzY29wZXMiOiIwIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJuYmYiOjE3NDA2MzQ4MTMsImlhdCI6MTc0MDYzNDgxMywiaXNzIjoiSldUIn0.tYXhqeJSDM1XAOEFndDhB_vOVPjgG82yMoBsaIVlH4G3A763iTIosXeqw-8TRS8rQzdNL4zYw_kf-agJVaQkD_8YUN_qdxKiu1qn9BIV0dC133msvCczjXGxxYBDtoGIfjWc6T9nemK-0FnSlXns-N0QssgCLPR04HtdS2WIV7Y" # Go 'WMMKS API' website to get your token
    input = "早在今年4月，就已經有駭客入侵美國民主黨全國委員會網路，竊取川普所有的研究資料；希拉蕊克林頓也在今年7月證實，該陣營由美國民主黨全國委員會負責維護的「選民分析數據程式」遭到駭客不當入侵存取。"
    r = request(input, token)
    #print(r) # Output: type = dictionary

    extracted_answer = extract_entitles(input, r)
    print(extracted_answer)
    print("人名:", extracted_answer["people"])
    print("時間:", extracted_answer["time"])
    print("地點:", extracted_answer["places"])
    print("物件:", extracted_answer["objects"])
    print("精簡事件", extracted_answer["simplified_events"])
    #print("完整事件：")

    if r:
        save_output("E24105038_林業誠_HW2.txt", extracted_answer)