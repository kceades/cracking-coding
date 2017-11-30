class linkedList(object):
	""" General Linked List Creator """
	def __init__(self,value=None):
		self.value = value
		self.next = None

def removeDuplicatesBuffer(input_list):
	""" Problem 2.1 """
	elements = {}
	return_list = linkedList(input_list.value)
	x = return_list

	while input_list.next is not None:
		input_list = input_list.next
		if input_list.value is not in elements:
			elements[input_list.value] = 1
			x.next = linkedList(input_list.value)
			x = x.next
	return return_list

def removeDuplicates(input_list):
	""" Problem 2.1 without any additional data structures """
	return_list = input_list
	x = return_list
	while input_list.value is not None:
		temp = input_list.value
		hold = input_list
		while hold.value is not None:
			prev = hold
			hold = hold.next
			if hold.value==temp:
				prev.next = hold.next
			hold = hold.next
		x.next = hold.next
		x = x.next
		input_list = input_list.next
	return return_list