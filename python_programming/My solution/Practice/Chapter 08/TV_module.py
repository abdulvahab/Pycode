# Television

class TV(object):
    
    def __init__(self,number,volume=5):
        self.__volume=volume
        self.number=number

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self,new_volume):
        if new_volume > 10:
            print("\nMaximum Volume is 10")
            self.__volume = 10
            self.watching()
        else:
            self.__volume = new_volume
            print("\nvolume changed to:", self.__volume)
            self.watching()                                
        
    def channel_name(self):
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
        
               
        
    def watching(self):
        
        print("\nyou are watching",self.channel_name(),"\nat channle:",self.number, "\nat volume",self.volume)
        print("\nEnjoy your time:")
        input("\nPress enter when you want to change Channel or Volume")
        action = input("""\n
                            Press 'c' to change the channel
                                        or
                                  'v'  to change the volume:
                      """)
        if action == 'c':
            self.start()
        elif action == 'v':
            self.change_volume()
        else:
            print("\nKeep watching:"),
            self.watching()
            
    def change_volume(self):
        consent = input("\nwant to change the volume ? :")                                
        if consent == 'n':
            self.watching()
        elif consent == 'y':
            self.volume = int(input("\nEnter new volume(between 1 & 10):  "))                                                     

    def start(self):
        choice = None
        while choice != 0:
            print("""\n\n           TV menu

                          0 - Switch Off
                          1 - Drama
                          2 - Music
                          3 - Sport
                          4 - Movie

                     """)

            choice = int(input("\nChoose your channel number:"))

            if choice == 0:
                print ("\ngood.bye")
            elif choice > 4:
                print("\nInvalid Choice:")
                input("\nPress enter to choose another channel")
            else:
                c = choice
                channel = TV(c)
                TV.watching(channel)

                     




if __name__ == "__main__":
    print("This is a TV module need to be used in other programme")    
 

    input("\n\nPress enter key to exit:")


