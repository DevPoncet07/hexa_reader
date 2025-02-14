from tkinter import Tk
from interface_phone.interface_phone import InterfacePhone
from src.hexa import Hexa


class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.interface=InterfacePhone(self)
        self.interface.grid()
        self.hexa=Hexa(self)
        txt=self.open_file("file1.txt")
        txt_decode=self.hexa.decode(txt)
        self.interface.afficher_all(txt_decode)
        
    def open_file(self,filename):
    	file=open("files/"+filename)
    	content=[]
    	for line in file.readlines():
    		content.append(line)
    	return "".join(content)



if __name__=='__main__':
    root=Root()
    root.mainloop()

