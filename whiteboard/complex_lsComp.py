names = ['Connor', 'Max', 'Evan', 'Jordan']

# Using the 'if' statement ... if always comes after the for
c_names = [first_name for first_name in names if first_name[0] == 'C']

print(c_names)

# for loop version
c_names_reg = []

for first_name in names:
    if first_name[0] == 'C':
        c_names_reg.append(first_name)
        
print('\n')
print(c_names_reg)