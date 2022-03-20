import math as math


class points:
    
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z 

    def get_point_desc(self,txt):
        print("Point %s coordinates: x = %f, y = %f, z = %f" % (txt,self.x, self.y, self.z))
    
    def get_point_x(self):
        return self.x
 
    def get_point_y(self):
        return self.y
 
    def get_point_z(self):
        return self.z    
    
    def set_point(self,desc):
        txt="insert " + desc + " x= "
        self.x=float(input(txt))
        txt="insert " + desc + " y= "
        self.y=float(input(txt))
        txt="insert " + desc + " z= "
        self.z=float(input(txt))
    
    def dist(self,p2):
        ret=math.sqrt((p2.x-self.x)**2 + (p2.y-self.y)**2 + (p2.z-self.z)**2 ) 
        return(ret) 
    
        
        
p1=points(3.0, 7.3, 19.5)
p2=points(4.0, 84.2, 13.9)

p1.get_point_desc("p1")  
p2.get_point_desc("p2")
print ("distance (p1,p2) = ",p1.dist(p2))
print ("distance (p2,p1) = ",p2.dist(p1))

p1.set_point("p1")
p2.set_point("p2")
print("After data update")
p1.get_point_desc("p1")
p2.get_point_desc("p2")
print ("distance (p1,p2) = ",p1.dist(p2))

