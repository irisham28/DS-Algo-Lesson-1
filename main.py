#class is - blueprint of object 

class fruit:
    #attributes /properties of the class
    #constructor for attributes 

    def __init__(self,color,taste,seed,shape,preference):
        #initalizing the functions
        self.color=color
        self.taste=taste
        self.seed = seed
        self.shape=shape
        self.preference = preference

    #methods->getter,setter,custom method
        
        #getter 
    def get_shape(self):
            return self.shape
        
        #setter
    def set_shape(self,new_shape):
            self.shape = new_shape

        #custom method
    def increase_preference(self):
            self.preference=self.preferance+1

    def show_fruit(self):
            print("hi there I am a fruit with {},i am {},i am very {},my shape is a {},I love it {}%".format(self.seed, self.color, self.taste, self.shape,self.preference))

#objects
mango=fruit("yellow","sweet","mango seed","oval",100)

mango.get_shape()

print(mango.get_shape())

mango.set_shape("heart")
print(mango.get_shape())

mango.show_fruit()

strawberry = fruit("red","sweet but sour","small seeds","heart",75)

strawberry.show_fruit()





    








