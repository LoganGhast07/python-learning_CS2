#LECTURE 3V2

#Unit 1 Excercise 1:
import re
texts = [
"Alice is 20 years old",
"Bob is 22 years old",
"Charlie is 19 years old",
]
for text in texts:
    match = re.match(r"(\w+) is (\d+) years old", text)
    if match:
        name = match.group(1)
        age = match.group(2)
        print(f"Name: {name}, Age: {age}")

print("="*50)


#Unit 1 Exercise 2:

import re
dates = ["03-15-2026", "12-25-2025", "01-01-2000"]
for date in dates:
    match = re.match(r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})", date)
    if match:
        # TODO 2: Extract using named groups
        info = match.groupdict()
        print(f"{info['month']}/{info['day']}/{info['year']}")

print("="*50)

#Unit 1 Exercise 3:

import re
log_entries = [
"[2026-03-10 14:30:45] Server started",
"[2026-03-10 09:15:02] User login",
"[2026-03-11 22:00:00] Backup complete",
]
for entry in log_entries:

    pattern = r"\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2})\] (?P<message>.+)"
    match = re.search(pattern, entry)
    if match:
        d = match.groupdict()
        print(f"Date: {d['date']}, Time: {d['time']}, Message: {d['message']}")
        
print("="*50)

#Unit 2 Exercise 1:

import re
text = "The price is $49.99 today"
match = re.search(r"\$\d+\.\d{2}", text)
if match:
    print(f"Price: {match.group()}")
    start, end = match.start(), match.end()
    print(f"Start: {start}, End: {end}")
    before = text[:start]
    after = text[end:]
    print(f"Before: '{before}'")
    print(f"After: '{after}'")

print("="*50)

#Unit 2 Exercise 2:
import re
sentences = [
"This is is a problem",
"The the cat sat down",
"No duplicates here",
"I really really like Python",
]
for sentence in sentences:
    match = re.search(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE)
    if match:
        print(f"Duplicate '{match.group(1)}' in: {sentence}")
    else:
        print(f"No duplicates in: {sentence}")

print("="*50)

#Unit 2 Exercise 3:

import re
records = [
"Name: Alice Smith | ID: EMP-001 | Dept: Engineering",
"Name: Bob Jones | ID: EMP-042 | Dept: Marketing",
"Name: Carol White | ID: EMP-108 | Dept: Sales",
]

pattern = r"Name: (?P<name>.+) \| ID: (?P<id>.+) \| Dept: (?P<dept>.+)"

for record in records:
    match = re.search(pattern, record)
    if match:
        d = match.groupdict()
        for key, value in d.items():
            print(f"{key.capitalize()}: {value}")
            id_span = match.span("id")
    print(f"ID field position: {id_span}")
    
print("="*50)

#Unit 3 Exercise 1:

import re
texts = [
"Hello there!",
"Hi everyone.",
"Hey you!",
"Goodbye now.",
"Howdy partner!"
]

for text in texts:
# TODO: Match "Hello", "Hi", or "Hey" at the start of the string
    match = re.match(r"^(Hello|Hi|Hey)", text)
    if match:
        print(f"Greeting found: '{match.group(1)}' in '{text}'")
    else:
        print(f"No greeting in: '{text}'")
        
print("="*50)

#Unit 3 Exercise 2:

import re

import re
files = [
"report.pdf", "photo.jpg", "data.csv",
"script.py", "style.css", "page.html",
"notes.txt", "image.png", "app.js"
]
for f in files:
    lower_f = f.lower()
# TODO 1: Match document extensions (.pdf, .doc, .txt, .csv)
    is_doc = re.search(r"\.(pdf|doc|txt|csv)$", lower_f)
# TODO 2: Match image extensions (.jpg, .jpeg, .png, .gif)
    is_img = re.search(r"\.(jpg|jpeg|png|gif)$", lower_f)
# TODO 3: Match code extensions (.py, .js, .html, .css)
    is_code = re.search(r"\.(py|js|html|css)$", lower_f)
    if is_doc:
        category = f"Document ({is_doc.group(1)})"
    elif is_img:
        category = f"Image ({is_img.group(1)})"
    elif is_code:
        category = f"Code ({is_code.group(1)})"
    else:
        category = "Other"
    print(f"{f:<15} → {category}")

print("="*50)

#Unit 3 Exercise 3:

import re
dates = [
"2026-03-15", # ISO: YYYY-MM-DD
"03/15/2026", # US: MM/DD/YYYY
"15 Mar 2026", # Text: DD Mon YYYY
"March 15, 2026", # Long: Month DD, YYYY
"not a date",
]

for date in dates:
# TODO 1: Try ISO format with named groups
    iso = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)
# TODO 2: Try US format
    us = re.search(r"(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})", date)
# TODO 3: Try text format (3-letter month abbreviation)
    text_fmt = re.search(
    r"(?P<day>\d{2}) (?P<month>[A-Za-z]{3}) (?P<year>\d{4})", date)
# TODO 4: Try long format — write the pattern yourself
    long_fmt = re.search(r"(?P<month>[A-Za-z]+) (?P<day>\d{2}), (?P<year>\d{4})", date)
    matched = iso or us or text_fmt or long_fmt
    if matched:
        d = matched.groupdict()
        print(f"'{date}' → month={d['month']}, day={d['day']}, year={d['year']}")
    else:
        print(f"'{date}' → no match")
        
print("="*50)

#LECTURE 4V2

#Unit 1 Exercise 1:
import re
texts = ["Python is great", "I love Python", "PYTHON", "python3"]
for text in texts:
# TODO 1: Use re.match to check if text starts with "Python"
    m = re.match(r"Python", text, re.IGNORECASE)
# TODO 2: Use re.search to check if text contains "Python" anywhere
    s = re.search(r"Python", text, re.IGNORECASE)
    starts = "yes" if m else "no"
    contains = "yes" if s else "no"
    print(f"'{text}' — starts with Python: {starts}, contains Python: {contains}")

print("="*50)


#Unit 1 Exercise 2:

import re
text = """
Student grades: Alice-92, Bob-78, Charlie-85, Diana-95.
Room numbers: A101, B204, C310.
Emails: alice@school.edu, bob@school.edu.
"""
# TODO 1: Find all names followed by scores (Name-Score)
name_scores = re.findall(r"(\b[A-Za-z]+-\d+\b)", text)
print(f"Scores: {name_scores}")
# TODO 2: Find all room numbers (letter + 3 digits)
rooms = re.findall(r"\b[A-Z]\d{3}\b", text)
print(f"Rooms: {rooms}")
# TODO 3: Find all email addresses
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(f"Emails: {emails}")

print("="*50)

#Unit 1 Exercise 3:

import re
csv_lines = [
"Alice,Smith,25,Engineer,alice@corp.com",
"Bob,Jones,30,Designer,bob@corp.com",
"Carol,White,28,Manager,carol@corp.com",
]
for line in csv_lines:
# TODO 1: Use re.match with groups to extract all 5 fields
# Pattern should match: word,word,digits,word,email
    match = re.match(
r"(\w+),(\w+),(\d+),(\w+),([\w\.-]+@[\w\.-]+)", line
)
    if match:
        first, last, age, role, email = match.groups()
# TODO 2: Validate that age is between 18 and 65
        age_num = int(age)
        valid_age = 18 <= age_num <= 65
# TODO 3: Print formatted output
        status = "✅" if valid_age else "⚠ age"
        print(f"{status} {first} {last} ({age}), {role}, {email}")

print("="*50)

#Unit 2 Exercise 1:
import re
text = "The cat sat on the mat near the bat"
# TODO 1: Replace all 3-letter words ending in "at" with "___"
result = re.sub(r"\b\w{1}at\b", "___", text)
print(result)
# TODO 2: Replace only the first occurrence
result2 = re.sub(r"\b\w{1}at\b", "___", text, count=1)
print(result2)

print("="*50)

#Unit 2 Exercise 2:
import re
# Reformat phone numbers from various formats to (XXX) XXX-XXXX
phones = [
"555-123-4567",
"555.123.4567",
"5551234567",
]
for phone in phones:
# TODO 1: First normalize — remove all non-digits
    digits = re.sub(r"\D", "", phone)
# TODO 2: Use re.sub with groups to reformat
    formatted = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", digits)
    print(f"{phone:<15} → {formatted}")

print("="*50)

#Unit 2 Exercise 3:

import re
text = "Python was created in 1991. Version 3.0 came in 2008. Now it's 2026."
# TODO 1: Use finditer to find all 4-digit years
# For each year, print the year and its context (10 chars before and after)
for match in re.finditer(r"\d{4}", text):
    start, end = match.span()
    ctx_start = max(0, start - 10)
    ctx_end = min(len(text), end + 10)
    context = text[ctx_start:ctx_end]
# TODO: Print the year, position, and context
    print(f"Year: {match.group()}, Position: {start}-{end}, Context: '{context}'")
# TODO 2: Use re.sub with a function to add 100 to every number in the text
def add_100(match):
    return str(int(match.group()) + 100)

result = re.sub(r"\d+", add_100, text)
print(f"\nAfter adding 100: {result}")

print("="*50)

#Unit 3 Exercise 1:
import re
# TODO 1: Compile a pattern to find words starting with a capital letter
cap_word = re.compile(r"\b[A-Z][a-z]*\b")
texts = [
"Alice met Bob in Paris",
"the quick brown Fox",
"No Capitals at the End except Here",
]
for text in texts:
# TODO 2: Use the compiled pattern's findall method
    matches = cap_word.findall(text) if cap_word else []
    print(f"Capitalized words: {matches}")

print("="*50)

#Unit 3 Exercise 2:

import re
# TODO: Rewrite this pattern using re.VERBOSE with comments
# Original: r"^(\d{2})/(\d{2})/(\d{4})$"
date_pattern = re.compile(r"""
^              # Start of string
(\d{2})        # Two digits for month
/              # Literal slash
(\d{2})        # Two digits for day
/              # Literal slash
(\d{4})        # Four digits for year
$              # End of string
""", re.VERBOSE)
tests = ["03/15/2026", "3/15/2026", "03-15-2026", "12/25/2025"]
for t in tests:
    match = date_pattern.match(t)
    if match:
        print(f"✅ {t} → month={match.group(1)}, day={match.group(2)}, year={match.group(3)}")
    else:
        print(f"❌ {t}")

print("="*50)

#Unit 3 Exercise 3:
#Do this one now 
import re
class Validator:
# TODO 1: Compile patterns as class attributes
    _email = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$", re.IGNORECASE)
    _phone = re.compile(r"^\d{3}-\d{3}-\d{4}$", re.IGNORECASE)
    _zip = re.compile(r"^\d{5}(-\d{4})?$", re.IGNORECASE) # Compile pattern for 5-digit ZIP, optional -XXXX
    _date = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.IGNORECASE) # Compile pattern for YYYY-MM-DD
    @classmethod
    def is_email(cls, text):
        return cls._email.match(text) is not None
    @classmethod
    def is_phone(cls, text):
    # TODO 2: Implement using _phone
        return cls._phone.match(text) is not None
    @classmethod
    def is_zip(cls, text):
    # TODO 3: Implement using _zip
        return cls._zip.match(text) is not None
    @classmethod
    def is_date(cls, text):
# TODO 4: Implement using _date
        return cls._date.match(text) is not None
# Test suite
tests = {
"is_email": ["alice@example.com", "not-an-email", "bob@site.org"],
"is_phone": ["555-123-4567", "5551234567", "55-123-4567"],
"is_zip": ["46802", "46802-1234", "4680", "ABCDE"],
"is_date": ["2026-03-15", "03/15/2026", "2026-13-01"],
}
for method_name, cases in tests.items():
    method = getattr(Validator, method_name) 
    print(f"\n{method_name}:")
    for case in cases:
        result = method(case)
        icon = "✅" if result else "❌"
        print(f" {icon} {case}")