# Television 2.0
import TV_module,games

class Watch(TV_module.TV):
    def __init__(self,number,serial):
        super(Watch,self).__init__(number)
        self.serial = serial
        self.names = name       
        print(self.names,"screen time =120 min")
        
    @property
    def name(self):
        if self.number == 0:
            name = "TV is Off"
            
        elif self.number == 1:
            name = "Star Plus"
        elif self.number == 2:
            name = "B4U Music"
        elif self.number == 3:
            name = "ESPN"
        elif self.number == 4:
            name = "Max"
        else:
            None            
        return name

class Viewer(Watch):
    def __init__(self,names):
        super(Viewer,self).__init__(n,s)
        self.viewers = []
        for name in names:
            viewer = Watch.name
            self.viewers.append(viewer)                 
        
    def __str__(self):
        if self.viewers:
            rep = ""
            for viewer in self.viewers:
                rep =+ viewer + "\t"
        else:
            rep ="<NO Viewers>"
        return rep
    
    def screen_time(self,names,time_allowed=120):
        time = 0
        for name in names:
            if time > time_allowed:
                print("you are not allowed to watch more TV")
            elif time < time_allowed:
                self()
                    
    
                    
class Housemates(object):
    def add_housemate(self,viewer):
        self.viewers.append(viewer)
    def remove_housemate(self,viewer):
        self.viewers.remove(self,viewer)
    

    
# main   
names = []   
        
h = games.ask_number("How many people watching TV today (1-5) ? ", 1, 6)
for i in range(h):
    name = input("Enter Viewer name:  ")
    names.append(name)
n = int(input("Enter the number of the channel you want to watch:"))
s = input("Enter name of the serial you want to watch: ")
viewer = Viewer(names)

print (viewer.viewers)
n = int(input("Enter the number of the channel you want to watch:"))
s = input("Enter name of the serial you want to watch: ")
viewer.screen_time(names)
    
print()




    
"""


print(v1)
channel = TV_Serial(n,s)
channel.start()
channel.watching()
n = int(input("Enter the number of the channel you want to watch:"))
s = input("Enter name of the serial you want to watch: ")

"""
