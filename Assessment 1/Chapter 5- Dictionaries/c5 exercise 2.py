#create a glossary dictionary with programming words with meanings then print each word and its meaning with a newline between each pair
glossary = {
    'variable': 'A named storage location in a program that can hold different values.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'list': 'A collection of items, ordered and changeable, used to store multiple values in a single variable.',
    'loop': 'A control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'dictionary': 'A collection of key-value pairs, where each key must be unique.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

