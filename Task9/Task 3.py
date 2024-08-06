def remove_items(list, item): 

	n = list.count(item) 
	for i in range(n): 
		list.remove(item) 
	return list 
	
if __name__ == "__main__": 
	list = [1, 2, 3, 4, 2, 5, 2] 
	item = 2

	print("The list is :" + str(list)) 
	remove = remove_items(list, item) 
	print("Result :" + str(remove)) 
