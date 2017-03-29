import string
from string import ascii_uppercase as up_case
from string import ascii_lowercase as lo_case


def ceaser(s, k, decode = False):
	if decode:
		k = 26 - k
	return s.translate(
		str.maketrnas(
			up_case + lo_case,
			up_case[k:] + up_case[:k]
			lo_case[k:] + lo_case[:k]
			)
		)

while True:
	encrypt_key = int(input("decide the magic number: "))
	msg = input("enter the message: ")
	print("encrypted message: ", ceaser(msg, encrypt_key))
	print("   
