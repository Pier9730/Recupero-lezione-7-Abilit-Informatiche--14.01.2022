
def mean(a,b):
    sum=0
    for i in range(b):
        sum=sum+a[i]
    sum=sum/b
    return(sum)


x = []              # emply list to be filled with X value for each entry
y = []              # emply list to be filled with Y value for each entry

idx=0
with open("myfile2D.txt", 'r') as myfile:
    for currline in myfile:                     # read a line including CR+LF for each line till end of file
        #print("Getline   ->",currline)    
        currline = currline.strip()             # take out CR LF
        #print("StripCRLF ->",currline)    
        currline = currline.replace(" ","")     # take out all spaces
        #print("StripSPC  ->",currline)    
        if (len(currline) > 0) and (currline.count(",")==1):  #chek for valid lines
            tmp=currline.rsplit(",")            #split elem via comma and put the x y value in tmp
            #print (tmp)
            x.append(float(tmp[0]))             #convert element in float and store in the x and y list
            y.append(float(tmp[1]))
            print("line #%d ->x=%f, y=%f" % (idx,x[idx],y[idx]))
            idx=idx+1
myfile.close()
print("Total valid lines read = ",idx)
print()

mean_x=mean(x,idx)
mean_y=mean(y,idx)
print("centre of gravity for %d points = (%f,%f)" %(idx,mean_x,mean_y))


      
