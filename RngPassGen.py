import random
import pyperclip

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
#symbols = "`~!@#$%^&*()-_=+" no symbols as requested, left incase for future use
length = 12

#add + symbols  after numbers to include symbols in the password
string = lower + upper + numbers

password = "".join(random.sample(string, length))
pyperclip.copy(password)
print("Your rng password is:" + password)
print("Password copied to clipboard!")
