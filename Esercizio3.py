
mylist=[]                       # emply list to be filled with 2D objs

    
class points:                   # the single 2D obj
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show_point (self):
        # show single point data
        #
        print("x=%f, y=%f" % (self.x,self.y))
    
    def get_point_x(self):
        return self.x
 
    def get_point_y(self):
        return self.y


class Baricentro:          
    # init get an array of lines, for each one a poin obj is instantiate and appended in the list
    # 
    def __init__(self, line_list):
        for i in range(len(line_list)):
            if (len(line_list[i]) > 0) and (line_list[i].count(",")==1):
                line_list[i] = line_list[i].strip()             # take out CR LF
                line_list[i] = line_list[i].replace(" ","")     # take out all spaces
                tmp=line_list[i].rsplit(",")                    #split elem via comma and put the x y value in tmp
                #print (tmp)
                mylist.append(points(float(tmp[0]),float(tmp[1])))     # convert element in float and store in point obj
                #print (point_elem[i])

    def show_b_points(self):
        # show all the objs of the list        
        #
        for i in range(len(mylist)):
            print("line #%d -> x=%f, y=%f" % (1,mylist[i].get_point_x(),mylist[i].get_point_y()) )
            
    def get_valid(self):
        return(len(mylist))
 
    def show_b_center(self):
        # compute ente f gravity and show it       
        #
        mean_x=0
        mean_y=0
        idx=len(mylist);
        for i in range(idx):
            mean_x=mean_x+mylist[i].get_point_x()
            mean_y=mean_y+mylist[i].get_point_y()
        mean_x=mean_x/idx;
        mean_y=mean_y/idx;
        print("centre of gravity for %d points = (%f,%f)" %(idx,mean_x,mean_y))




def load_file():
    try:
        filename = input('Insert filename: ')
        #filename="myfile2D.txt"
        myfile = open(filename,'r')
        mylines = myfile.readlines()
        myfile.close()
        
    except BaseException as err:        # in case of any error
        mylines = list()                # clean the lines list and show error
        print("Error = %s " % (err))
        
    return mylines




# main program

lines=load_file()               # open file and fill the lines_list with all the read ones
idx=len(lines);                 # get tota lines read

if (idx):
    MyObj=Baricentro(lines)     # create the main obj with the lines_list 
                                # one point_obj is created for each entry line
    MyObj.show_b_points()       # show all the points of the main obj
    print("Total valid lines read = ",MyObj.get_valid())
    print()
    MyObj.show_b_center()       # compute and show the Center of Gravity

