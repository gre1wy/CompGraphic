input_list = [3, 5, 10, 251, 10, 251] 

# Building and initializing the dictionary.
dictionary_size = 256                   
dictionary = {i: tuple([i]) for i in range(dictionary_size)}  
string = []  # String is initially empty
compressed_data = []  # Variable to store the compressed data

# LZW Compression algorithm
for symbol in input_list:
    string_plus_symbol = string + [symbol]  # Get input symbol.
    if tuple(string_plus_symbol) in dictionary.keys(): 
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[tuple(string)])
        string = [symbol]

if tuple(string) in dictionary:
    compressed_data.append(dictionary[tuple(string)])
print(dictionary)
