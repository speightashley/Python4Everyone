import re

text = "This is a string and I am going to play with 885 regular expressions to try to extract things from it"

pattern = re.compile(r'\w+.?')
x = pattern.findall(text)
z = pattern.match(text, 0)
a = pattern.search(text, 4)

newpattern = re.compile(r'(\w+) (\w+) (\w+)')

anotherpattern = re.compile(r'a')
b = anotherpattern.sub("?", text)

y = newpattern.findall(text)

print(x)
print(z)
print(a)
print(y)

print()
print(b)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)