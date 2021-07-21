import numpy as np


def load_data(filename):
	"""Utility funciton to load data from files.
	
	Parameters
	----------
	filename :  str
		The path to the data source file.
	
	Returns
	-------
	data : ndarray
		A list containing all the data from the source.
	"""
	
	with open(filename) as f:
		data = f.read()
	
	data = data.split('\n')[:-1]
	data = [float(item.split('B')[0][1:]) for item in data]
	data = np.array(data)
		
	return data


def save_data(filename, data):
	"""Utility funciton to read data files.
	
	Parameters
	----------
	filename :  str
		The path to the file where data will be saved.
	data : ndarray
		A NumPy array containing all the data to be saved.
	"""

	text_data = [str(item) for item in data]
	text_data = '\n'.join(text_data)
	with open(filename, 'wt') as f:
		f.write(text_data)
		
	return


def apply_filter(data, filter_name='high-pass'):
	"""Applies a specified filter to the input data.
	
	Parameters
	----------
	data : ndarray
		The array with data to be filtered in  NumPy format.
	filter_name : str
		The name of the filter to be applied. By default it is set to 
		`'high-pass'` The options are:
		
		- `'high-pass'`. Applies a high-pass filter.
		- `'low-pass'`. Applies a low-pass filter.
		- `'notch-60'`. Applies a Notch filter (60Hz).
		- `'notch-120'`. Applies a Notch filter (120Hz).
		- `'notch-180'`. Applies a Notch filter (180Hz).
		
	Returns
	-------
	a_filtered : ndarray
		The filtered array in NumPy format.
	"""
	
	filter_values = {
		'high-pass': {
			'num': np.array([
				0.967979116586355,
				-3.87191637080971,
				5.8078745084467,
				-3.87191637080971,
				0.967979116586353
			]),
			'den': np.array([
				1.0,
				-3.9349131586298,
				5.80684935782903,
				-3.80891939663271,
				0.9369835701473
			])
		},
		'low-pass': {
			'num': np.array([
				0.029961623669272,
				0.067130684368247,
				0.08891650138874,
				0.067130684368247,
				0.029961623669272
			]),
			'den': np.array([
				1.0,
				-1.64108261333786,
				1.36267875398924,
				-0.522411096246205,
				0.0839160730586
			])
		},
		'notch-60': {
			'num': np.array([
				0.894632477430353,
				-3.32723296345856,
				4.88283835542764,
				-3.32723296345857,
				0.894632477430356
			]),
			'den': np.array([
				1.0,
				-3.51282144991274,
				4.87170485529735,
				-3.14164447700439,
				0.800398454990987
			])
		},
		'notch-120': {
			'num': np.array([
				0.89463247731328,
				-2.60863603651524,
				3.69084568507969,
				-2.60863603651524,
				0.89463247731328
			]),
			'den': np.array([
				1.0,
				-2.7541421726346,
				3.67971218377352,
				-2.46312990039587,
				0.800398454070091
			])
		},
		'notch-180': {
			'num': np.array([
				0.89463247743035179,
				-1.5236639295087626,
				2.4379516714510858,
				-1.5236639295087626,
				0.89463247743035179
			]),
			'den': np.array([
				1.0,
				-1.6086518115260233,
				2.4268181713208063,
				-1.4386760474915006,
				0.80039845499098439
			])
		}
	}
	
	num = filter_values[filter_name]['num']
	den = filter_values[filter_name]['den']
	a_filtered = data
	
	xn_n = np.zeros(5)
	yn_n = np.zeros(5)
	
	for i in range(len(a_filtered)):
		xn = a_filtered[i]
		
		ec1 = [xn * num[0]] + [num[k] * xn_n[k] for k in range(1, 5)]
		ec1 = sum(ec1)
		
		ec2 = [den[k] * yn_n[k] for k in range(1, 5)]
		ec2 = sum(ec2)
		
		yn = ec1 - ec2
		a_filtered[i] = yn
		
		for j in range(4, 1, -1):
			yn_n[j] = yn_n[j - 1]
			xn_n[j] = xn_n[j - 1]
		yn_n[1] = yn
		xn_n[1] = xn
		
		
	return a_filtered
