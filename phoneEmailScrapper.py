import re
import pyperclip

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 
(
((\d\d\d) | (\(\d\d\d\)))?       #area code (optional)
(\s|-)        #first separator
\d\d\d        # first 3 digits
-        # separator
\d\d\d\d        # last 3 digits
(((ext(\.)?\s)|x)        # extension word-pad (optional)
(\d{2,5}))?
)              # the number-part of the extension (optional)
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name part
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)




