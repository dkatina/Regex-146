# Metacharacters, Special Sequences, Position Anchors and so Much More!!!

# 1.  Dot (.) - The Wildcard Character
#     - Task: Find any three-character sequence in a text, where the middle 
#       character can be anything, the first has to be ‘c’ and the last has to be ‘t’.
#     - Regex Pattern: `c.t`
#     - Test Sentence: "I found a cat, a cot, and a cut in the room."
#     - Expected Matches: `['cat', 'cot', 'cut']`
#     - Explanation: The dot `.` matches any single character (except newline), 
#       so it finds sequences where 'c' and 't' are separated by any character.

# 2. Caret (^) - The Beginning Anchor
#     - Task: Find strings that start with 'Py'.
#     - Regex Pattern: `^Py`
#     - Test Sentence: "Python is fun Py"
#     - Expected Matches: `[’Py’]` from 'Python' at the beginning of the 
#       sentence.
#     - Explanation: The caret `^` ensures that the match must occur at the 
#       start of the string or line.

# 3. Dollar ($) - The End Anchor
#     - Task: Identify strings that end with 'fun'.
#     - Regex Pattern: `fun$`
#     - Test Sentence: "Learning regex is fun"
#     - Expected Matches: `['fun']` from 'Learning regex is fun'
#     - Explanation: The dollar `$` ensures that 'fun' is matched only if 
#       it's at the end of the string or line.

# 4. Asterisk (*) - Zero or More Occurrences
#     - Task: Match a character followed by zero or more 'a's.
#     - Regex Pattern: `ba*`
#     - Test Sentence: "I saw a bat, and a ball in my bed, baaah!"
#     - Expected Matches: `['ba', 'ba', 'b', 'baaa']` from ‘bat’, ‘ball’, 
#       ‘bed’, and ‘baaah!’.
#     - Explanation: The pattern starts with the literal character 'b'. 
#       This means it will first look for occurrences of 'b' in the text. 
#       Following the 'b', we have 'a*'. Then, the asterisk  `*` which matches 
#       zero or more occurrences of the preceding character ('a' in this case).

# 5. Plus (+) - One or More Occurrences
#     - Task: Find a character followed by one or more 'a's.
#     - Regex Pattern: `ba+`
#     - Test Sentence: "The battle of ba and baat."
#     - Expected Matches: `['ba', 'ba', 'baa']` from ‘battle’, ‘ba’, and 
#       ‘baat’.
#     - Explanation: The plus `+` matches one or more occurrences of the 
#       preceding character ('a' in this case).

# 6. Question Mark (?) - Zero or One Occurrence Making a Character Optional
#     - Task: Match 'colour' or 'color'.
#     - Regex Pattern: `colou?r`
#     - Test Sentence: "The color is nice. I like this colour."
#     - Expected Matches: `['color', 'colour']`
#     - Explanation: The question mark `?` makes the preceding character 
#       ('u' in this case) optional.

# 7. Backslash (\) - Escaping Special Characters Removes power from metachars
#     - Task: Match a period character in a sentence.
#     - Regex Pattern: `\.`
#     - Test Sentence: "End of sentence. Start of a new one."
#     - Expected Matches: The periods `[., .]` at the end of 'sentence.' 
#       and before 'Start'.
#     - Explanation: In regex, the period (.) is a special character used as
#        a wildcard. To match an actual period, the backslash `\` is used to 
#       escape the special meaning of the period, treating it as a literal 
#       character. The pattern `\.` specifically looks for the period 
#       character in the text.

# 8. Square Brackets ([]) - Character Sets
#     - Task: Find all vowels in a word.
#     - Regex Pattern: `R[aeiou]`
#     - Test Word: "Regular Radicals"
#     - Expected Matches: `['Re', 'Ra']`
#     - Explanation: The square brackets `[]` define a set of characters, 
#       any of which can be matched.

# 9. Pipe (|) - The OR Operator great for scouting multiple key words
#     - Task: Match 'cat' or 'dog'.
#     - Regex Pattern: `cat|dog|cow|hamster`
#     - Test Sentence: "I have a cat and a dog."
#     - Expected Matches: `['cat', 'dog']`
#     - Explanation: The pipe `|` acts as an OR operator, matching either 
#       the pattern before or after it.

# 10. Parentheses (()) - Grouping
#     - Task: Find repetitions of 'woof' or 'meow'.
#     - Regex Pattern: `(woof|meow)+`
#     - Test Sentence: "The pets say woofwoof and meow."
#     - Expected Matches: `['woofwoof', 'meow']`
#     - Explanation: Parentheses `()` group patterns, allowing the plus `+` 
#       to apply to the entire group.

# 11. Curly Braces ({}) - Specifying Exact Occurrences
#     - Task: Match a word where 'l' is followed by exactly two 'o's.
#     - Regex Pattern: `lo{2}`
#     - Test Sentence: "Look at the loom and the balloon in the room."
#     - Expected Matches: 'loo' in 'loom' and 'balloon'
#     - Explanation: The pattern `lo{2}` searches for an 'l' followed by 
#       exactly two 'o's. In our test sentence, it successfully identifies 'loo' 
#       within the words 'loom' and 'balloon', demonstrating the ability of curly 
#       braces `{}` to specify an exact number of occurrences.

# 12. \d - Hunts down digits (0-9) in your text:
#     - Task: Extract all phone numbers from a text for a phone number in
#       the format 'XXX-XXX-XXXX', where each 'X' is a digit
#     - Regex Pattern: `\d{3}-\d{3}-\d{4}`
#     - Test Sentence: "Call me at 123-456-7890 or 987-654-3210."
#     - Expected Matches: `['123-456-7890', '987-654-3210']`
#     - Explanation: The `\d` sequence finds digits, and `{3}` specifies 
#       exactly three digits. The hyphen `-` is a literal character, It separates 
#       different segments of the phone number. Overall, this pattern searches for 
#sequences like a U.S. standard phone number format.

# 13. \w - Finds word characters (letters, digits, and underscores).
#     - Task: Identify words containing numbers.
#     - Regex Pattern: `\w*\d\w*`
#     - Test Sentence: "My username is user123 and my password is pass99word."
#     - Expected Matches: `['user123', 'pass99word']`
#     - Explanation: `\w*` matches any word character zero or more times, 
#        and `\d` ensures there's at least one digit. This pattern finds words mixed with numbers.

# 14. \s - - Seeks out whitespace (spaces, tabs, newlines).:
#     - Task: Split a sentence into words.
#     - Regex Pattern: `\s+`
#     - Test Sentence: "Welcome  to the world of regex!"
#     - Expected Matches: The spaces between ['Welcome', 'to', 'the,', 'world', 'of', 'regex!’]
#     - Explanation: `\s+` matches one or more whitespace characters. 
#       It does not match the characters of the words themselves but the empty space 
#       that separates them, allowing us to see where one-word ends and another begins.

# 15. \D- Finds any character that is not a digit.
#     - Task: Find non-digit characters in a string.
#     - Regex Pattern: `\D+`
#     - Test Sentence: "Room 101 is on floor 3"
#     - Expected Matches: `['Room ', ' is on floor ']`
#     - Explanation: `\D+` matches one or more non-digit characters,
#       capturing the words and spaces in the sentence.

# 16. \W - Matches any character that is not a word character (opposite of \w).
#     - Task: Identify characters that are not part of words.
#     - Regex Pattern: `\W`
#     - Test Sentence: "Hello, world! Are you ready?"
#     - Expected Matches: `[',', ' ', '!', ' ', ' ', ' ', '?']`
#     - Explanation: `\W` finds any character that is not a letter,
#       digit, or underscore, like punctuation and spaces in this case.

# 18.  \S  - Identifies any character that is not a whitespace.
#     - Task: Identify non-whitespace characters in a string.
#     - Regex Pattern: `\S`
#     - Test Sentence: "Python 3.12 - New Features"
#     - Expected Matches: Matches each non-space character individually,
#       including letters, numbers, dots, and dashes.`['P', 'y', 't', 'h', 'o', 
#       'n', '3', '.', '1', '2', '-', 'N', 'e', 'w', 'F', 'e', 'a', 't', 'u', 'r', 'e', 's']`

# 19.  \b - Used to mark start or end of word.
#     - Task: Find words that start with 'Py'.
#     - Regex Pattern: `\bPy\w*`
#     - Test Sentence: "Python is easy. Typing is fun."
#     - Expected Matches: `['Python']` from the beginning of the sentence.
#     - Explanation: `\b` ensures the match starts at a word boundary
#        and `\w*` matches any word characters following 'Py'.

# 20.  \B - used to mark something that isn't the start or end of a word
#     - Task: Find instances of 'll' not at the start or end of a word.
#     - Regex Pattern: `\Bll\B`
#     - Test Sentence: "The yellow mellow mushroom illuminated the room."
#     - Expected Matches: 'll' in 'yellow', 'mellow', and 'illuminate’.
#     - Explanation:`\B` is used to find matches where a word Boundary
#       does not exist. In this case, it ensures that the pattern 'oo' is not at 
#       the start or end of a word. The regex pattern `\Boo\B` specifically 
#       looks for occurrences of 'oo' where both the preceding and following 
#       characters are also word characters (like letters or digits). It ignores 
#       cases where 'oo' is at the beginning or end of a word.  
