


class Hexa:
	def __init__(self,boss):
		self.boss=boss
		
	def decode(self,text):
		index_element_per_line=0
		txt_decode=[]
		line_temp=[]
		print(text)
		for element in text:
			if index_element_per_line>=15:
				index_element_per_line=0
				txt_decode.append(line_temp)
				line_temp=[]
			line_temp.append(element)
			index_element_per_line+=1
		if index_element_per_line!=0:
			txt_decode.append(line_temp)
		
		return txt_decode		
		