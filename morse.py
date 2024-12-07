morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',     
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',  
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',   
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',     
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',  
    'Z': '--..'
}

code_list = []
string = input(f"enter the string that you want to convert into morse code:").upper()
for letter in string:
    code_list.append(morse_code_dict[letter])
    
        
code = "".join(code_list)
print(code)        


