def uniqueStringAdditional(in_str):
	""" Problem 1.1 """
	elements = {}
	for letter in in_str:
		if letter in elements:
			return False
		else:
			elements[letter] = 1
	return True

def uniqueString(in_str):
	""" Problem 1.1 without additional data structures """
	for i in range(len(in_str)):
		looking_for = in_str[i]
		for j in range(i+1,len(in_str)):
			if in_str[j]==looking_for:
				return False
	return True

def compress(in_str):
	""" Problem 1.5 """
	r_string = ""
	in_length = len(in_str)
	current = in_str[0]
	count = 1
	for i in range(1,in_length):
		if in_str[i]==current:
			count = count + 1
			if i==(in_length-1):
				r_string = r_string + current + str(count)
		else:
			r_string = r_string + current + str(count)
			count = 1
			current = in_str[i]
	
	if len(r_string)>=in_length:
		return in_str
	else:
		return r_string