def is_a_int(a):
	"""Checks if a number is an Integer or not
	Input: Any String std Input
	Output: Type Bool
	True: If Integer
	False: If Not Integer
	"""
    try:
        int(str(a))
    except:
        bool_a = False
    else:
        bool_a = True
    return bool_a


def is_a_float(a):
	"""
		Checks if a number is an Float or not
		Input: Any String std Input
		Output: Type Bool
		True: If Integer
		False: If Not Integer
	"""
    try:
        float(str(a))
    except:
        bool_a = False
    else:
        bool_a = True
    return bool_a
