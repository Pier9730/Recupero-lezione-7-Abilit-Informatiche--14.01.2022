import random

class Campionato:
 
    def __init__(self):
        self.mydict = dict()
 
    def exist(self, name):
        if(self.mydict.get(name)):
            return(1)
        else:
            return(0)
        
    def insert(self, name, points):
        self.mydict[name] = points
 

    def get(self, name):
        return self.mydict.get(name)
    
    def delete(self, name):
        self.mydict.pop(name)
    
    def get_position(self,rank):
        if len(self.mydict)>0:
            points=sorted(self.mydict.values(),reverse=True)
            #print (points)
            for namekey in self.mydict:
                if self.mydict.get(namekey)==points[rank]:
                    #print("find=",namekey," points= ",points[rank])
                    return(namekey)
                    break
 
    def count(self):
        return len(self.mydict)
 
    def __str__(self):
        return str(self.mydict)
    


 
c = Campionato()
n = int(input("Quante squadre da inserire? "))


for i in range(0,n):
    """ 
    # manual mode entry    
    team = input("Inserire nome squadra : ")
    score = int(input("Inserire punti per la squadra : " + team + " : "))
    if( not c.exist(team)):
         c.insert(team, score)
    else :
        print("Team already present")
        i=i-1
        continue
    # end manual mode
    """

#    """ 
    # automatic mode entry    
    team = "Team name #"+str(i+1)
    score = random.randint(14,72)
    c.insert(team, score)
    # end automatic mode
#    """


# test delete, so insert a dummy one ad delete it
c.insert("tobedeleted", 123)
#print(c)
c.delete("tobedeleted")
#print(c)


n_teams=c.count()
print("Nel campionato ci sono ",n_teams," squadre")
print("Classifica finale")
print("<pos>       <squadra>      <punti>    <note>")
for i in range(0,n_teams):
    currteam=c.get_position(i)
    if(i==0):
        remark="Campione"
    elif (i>=(n_teams-3)):
        remark="Retrocessa"
    else:
        remark=""
    print("%3d    %-18s    %3d     %s" %(i+1,currteam,c.get(currteam),remark))
