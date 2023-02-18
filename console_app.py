## @file console_app.py
# @brief A console application to demonstrate interactive mode

######################################################################
# @brief Replaces characters in data with specified replacement chars
# @param[in] data: a 2d list of characters to use 
# @param[in] replacements: a 2d of characters and their replacements
######################################################################
def replace_characters(data, replacements):
    lines = []
    
    # Get single string from each sublist.
    for line in data:
        lines.append("".join(line))
    
    # Begin replacements.
    for index in range(len(lines)):
        for replacement in replacements:
            lines[index] = lines[index].replace(replacement[0], replacement[1])
        
        # Print result line by line.
        print(lines[index])

art3 = [
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','d','V','V','V','b'],
['U','U','U','U','U','U','U','U','U','U','_','_',',','.','-','-','-','"','"','"','-','.','U',
'U','U','U','U','U','U','U','U','U','V','V','V','V','V','V','V','U','U','U','U','U','U',
'U','U','U','U','.','-','"','"','"','-','-','-','.',',','_','_'],
['U','U','U','U','U','U','_','.','-','"','U','.','_','.','_','.','_','.','_',',','_','U','`','"','-',
'.','U','U','U','U','U','U','V','V','V','V','V','V','V','U','U','U','U','U','U','.','-',
'"','`','U','_',',','_','.','_','.','_','.','_','.','U','"','-','.','_'],
[',','_','_','.','-','"','U','_','*','_','*','_','*','_','*','_','*','_','*','_','*','_','*',
'_',',','_','`','"','.','U','U','U','U','Y','V','V','V','P','U','U','U','U','.','"','`','_',',','_',
'~','_','~','_','~','_','~','_','~','_','~','_','~','_','~','_','"','-','.','_','_',','],
['U','`','"','-','.','_','*','_','*','_','*','_','*','_','*','_','*','_','*','_','*','_','*','_',
'*','_','*',',','_','`','"','.','_','U','d','W','b','U','_','.','"','`','_',',','_','~','_','~',
'_','~','_','~','_','~','_','~','_','~','_','~','_','~','_','~','_','.','-','"','`'],
['U','U','U','U','U','U','"','-','L','-','*','_','*','_','*','_','*','_','*','_','*','_',
'*','_','*','_','*','_','.','-','-','.','U','W','W','W','W','W','U','.','L','L',',',
'_','~','_','~','_','~','_','~','_','~','_','~','_','~','_','~','_','~','-','L','-','"'],
['U','U','U','U','U','U','U','U','U','U','*','_','*','_','*','_','*','_','*','_','*','_','*','_',
'*','_','*','*','U','U','e','U','~','I','I','I','I','I','L','L','a','L','L','L','~','_','~','_','~',
'_','~','_','~','_','~','_','~','_','~','_','~'],
['U','U','U','U','U','U','U','U','U','U','U','U','"','-','*','_','*','_','*','_','*','_',
'*','_','*','U','*','U','U','U',',','-','"','I','I','I','I','I','"',
'=','L','L','L','L','L','U','~','_','~','_','~','_','~','_','~','_','~','-','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','*','_','*','_','*','_','*','_',
'U','*','U','U','U','*','U','U','U','V','V','V','V','V','U','U','U','L','L','L','L','L','U','_','~','_','~','_','~','_','~'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','"','-','*','_',
'*','|','U','U','U','|','U','U','U','V','V','V','V','V','U','U','U','L','L','L','L','L','~','_','~','-','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','~','U','U','U','~','U','U','V','V','V','V','V','U','U','L','L','L','L','L'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','"','.','U','U','"','.','"','V','V','V','"','.','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','"','.','U','U','"','V','V','V','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','"','.','U','.','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','.','L','L','L','L','"','.'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','.','L','L','L','L','V','.','U','U','"','.'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','.','L','L','L','L','"','V','V','V','"','.','U','U','"','.'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','.','L','L','L','L','U','U','V','V','V','U','U','~','U','U','U','~'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','L','L','L','L','U','U','U','V','V','V','U','U','|','U','U','U','|'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','"','L','L','L','L','U','U','V','V','V','U','U','*','U','U','U','*'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','"','L','L','L','L','.','V','V','V','.','"','U','U','.','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','"','L','L','L','L','V','"','U','U','.','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','"','L','"','U','U','.','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','.','"','U','U','.','L','L','L','.'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','*','U','U','U','*','V','~','L','L','L','L'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','*','U','U','U','*','V','V','V','L','L','L','L',','],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','|','U','U','U','|','V','V','V','U','L','L','L','L'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','~','U','U','U','~','V','V','V','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','"','.','U','U','"','V','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','U','"','.','L','L','L','L','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','U','U','U','L','L','L','L','`','U','~'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','U','L','L','L','L','V','|','U','U','|'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','"','L','L','L','V','*','U','U','*'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','U','U','"','-','"','V','"','-','"'],
['U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U',
'U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','U','V'],
]
replacements = [('*', '/'), ('~', '\\'), ('U', ' '), ('V', '8'), ('L', ';'), ('"', "'")]

print('{}\n\n'.format(("- "*40)))

# Function call.
replace_characters(art3, replacements)
print("ASCII Art 3")
print('{}\n\n'.format(("- "*40)))