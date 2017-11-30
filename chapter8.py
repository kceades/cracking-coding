def wayCounter(steps):
	""" Problem 8.1 """
	return wayCounterHelper(steps,{})

def wayCounterHelper(steps,memos):
	""" Helper for Problem 8.1 """
	if steps<0:
		return 0
	elif steps==0:
		return 1
	else:
		if steps in memos:
			return memos[steps]
		else:
			memos[steps] = wayCounterHelper(steps-1,memos)\
				+wayCounterHelper(steps-2,memos)+wayCounterHelper(steps-3,memos)
			return memos[steps]



def parens(n):
	""" Problem 8.9 """
	strings = parensHelper(n,[''])
	for string in strings:
		print(string)

def parensHelper(n,strings):
	if n==0:
		return strings
	else:
		new_strings = []
		for string in strings:
			new = '()' + string
			new2 = string + '()'
			if new==new2:
				new_strings.append(new)
			else:
				new_strings.append(new)
				new_strings.append(new2)
			new3 = '(' + string + ')'
			if new3!=new2 and new3!=new:
				new_strings.append(new3)
		return parensHelper(n-1,new_strings)