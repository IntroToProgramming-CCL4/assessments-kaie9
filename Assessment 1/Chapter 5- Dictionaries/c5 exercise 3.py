#create a glossary dictionary with programming words with meanings add 5 mmore then print each word 
glossary = {
    'variable': 'A named storage location in a program that can hold different values.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'list': 'A collection of items, ordered and changeable, used to store multiple values in a single variable.',
    'loop': 'A control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'dictionary': 'A collection of key-value pairs, where each key must be unique.'
    'module': 'A file containing Python definitions and statements that can be used in other Python programs.',
    'syntax': 'The set of rules that dictate how programs written in a programming language are to be structured.',
    'tuple': 'An ordered, immutable sequence of elements, commonly used for heterogeneous data.',
    'algorithm': 'A step-by-step procedure or formula for solving a problem or accomplishing a task.',
    'inheritance': 'A mechanism in which a class inherits attributes and methods from another class.'
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

