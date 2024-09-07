def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_num_words(text)
    print(f'--- Begin report of {path} ---')
    print(f"{num_of_words} words found in the document\n")
    nums_char = get_num_charactors(text)
    # print(nums_char)
    char_list = convert_dict_to_list(nums_char)
    # print(char_list)
    for dict in char_list:
        char_name = dict["name"]
        char_num = dict["num"]
        print(f"The '{char_name}' character wea found {char_num} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()  

def get_num_charactors(text):
    nums_char = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in nums_char:
            nums_char[char] += 1
        else:
            nums_char[char] = 1
    return nums_char

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"name" : key, "num" : dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

main()