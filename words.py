def word_list(words):
    '''This takes a list of words and prints them each on separate lines.
        
    All in uppercase.
    '''
    
    for word in words:
        print(f'''
              {word.upper()}''')
            
def print_e_only(words, letter):
    for word in words:
        if word.startswith(f'{letter}') or word.upper().startswith(f'{letter}'.upper()):
            print(f'''
              {word.upper()}''')
        
print(word_list(["hello", "bye", "later" ]))
print(print_e_only(["hello", "bye", "later", "ello gov'na", "ELEPHANT" ],"e"))