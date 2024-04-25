import re #make sure to import re (which is regex) 

#-- re.findall(pattern, text) : retrieves all non-overlaping matches the pattern
#and returns a list of all the matches

text = 'Hi my name is Dylan, and I like tog and do things and stuff.'

ands = re.findall(r'and', text)
print(len(ands))

#find all hashtags in post

post = 'I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Coder'

tags = re.findall(r'#\w+', post)
print(tags)

#find all words that start with b and end with the letter e

sentence = 'Abe asked to build a bridge be but he was told "beware of the beehives!".'

bes = re.findall(r'\bb\w*e\b', sentence)
print(bes)

#Finding emails

text = 'You can contact me at d.k@gmail.co or dylan-k2@codingtemple.com, dylankatina@email.com'

#username can include letters a-z, digits, _, -, .
#domain can include letters a-z, digits, _, - 
#domain extension needs to be only 2 or 3 character a-z


emails = re.findall(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', text)
print(emails)


#-- re.search(pattern, text) : searches a string for a pattern match, and returns
#the first occurance as a match object

email = 'dk@email.com'
found = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email)
if found:
    print(f'{found.group()} Is a Valid Email.')
else:
    print('Invalid Email')

#Validating Phone Numbers

# 000-000-0000
# 000 000 0000
# 0000000000

number = 'My phone number is: 770 888 1180'

phone = re.search(r'\d{3}(-| )?\d{3}(-|\s)?\d{4}', number)
print(phone)




#-- re.match(pattern, text) : Will return a match object if there is a pattern 
#match at the very beginning of the text

text = 'Hello, World'

obj = re.match(r'Hello', text)

print(obj)

#check to see if a website is secure
#https or http

url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print('This site is secure!')
else:
    print('This site is not very secure!')


#-- re.split(pattern, text) splits the text on occurances of the pattern, returns
#a list

#split on the garbage
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[.,;\s?-]+", text)
print(words)

words2 = text.split(r'[.,;]')
print(words2)

#-- re.sub(patter, replacer, text) : replaces occurances of the pattern in a string
#with a replacer

number = "(770) 888-1180"

formated_number = re.sub(r'\D', '', number)
print(formated_number)

#Anonymous chat

chat = '''
@Dylank123 : "I think i love regex"
@Travis : "Dont you have a wife"
@Dylank123 : "Its just not the same"
@Travis : "She better not see this!"
'''

anon_chat = re.sub(r"@\w+", "@user-anon", chat)
print(anon_chat)




