import re

#grouping with findall(pattern, text)

#literal string followed by group, group gets extracted if literal is found

log_data = '''
INFO: Processing Complete.
ERROR: Invalid username or password. 122200
INFO: log in successful
ERROR: YOUR WORNG. 34526''' 

errors = re.findall(r'ERROR: (.+)\.', log_data)
print(errors)




my_string_again = "M4x Smith, aaron rodgers, Sam Darnold-Alexander, LeBron James, Micheal Jordan, Kevin Durant, Patrick McCormick, Sean O'Malley"

names = re.split(r', ', my_string_again)


for name in names:
    name_match = re.match(r"([A-Z][A-Za-z]+) ([A-Z]'?[A-Za-z-]+)", name)
    if name_match:
        print(name_match.group())
    else:
        print('Invalid Name')