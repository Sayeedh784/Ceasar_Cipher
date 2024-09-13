
text = input("Enter the plain text or cipher text: ")
key = int(input("Enter the key: "))

total_alphabet = 26

if key < 1:
    num_add = (-key) // total_alphabet
    
    key = key + num_add * total_alphabet

if key > 26:
  
    num_sub = key // total_alphabet
    key = key - num_sub * total_alphabet

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""

for char in text:
    if char in lowercase:
        pos = lowercase.index(char) + 1  
        new_pos = pos + key
        if new_pos > 26:
            new_pos -= 26
        elif new_pos < 1:
            new_pos += 26
        new_char = lowercase[new_pos - 1]
        result += new_char
        
    elif char in uppercase:
        pos = uppercase.index(char) + 1  
        new_pos = pos + key
        if new_pos > 26:
            new_pos -= 26
        elif new_pos < 1:
            new_pos += 26
        new_char = uppercase[new_pos - 1]
        result += new_char

    else:
        result += char

print("Final Output text:", result)
