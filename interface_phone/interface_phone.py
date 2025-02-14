from tkinter import Frame,Text

class InterfacePhone(Frame):
	def __init__(self,boss):
		self.boss=boss
		Frame.__init__(self,master=boss)
		self.text=Text(self,width=80,height=20,font=("Arial",5))
		self.text.grid(row=0,column=0)
		
	def afficher_all(self,text_decode):
		self.index_line=0
		self.text.delete(0.0,"end")
		for line in text_decode:
			line_number=self.create_numbers_line(self.index_line)
			self.text.insert("end",line_number+" "+str(line)+"\n")
			
			self.index_line+=16
			
	def create_numbers_line(self,number):
		txt=str(hex(self.index_line))[2:]
		n=8-len(txt)
		for x in range(n):
			txt="0"+txt
		return txt