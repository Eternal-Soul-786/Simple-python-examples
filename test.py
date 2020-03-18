import time
class TechLearners:
    interest_list=[]
    
    
    learners={'rosy':'l1','ramu':'l2','damu':'l3','sony':'l4','bichu':'l5','jack':'l6'}
    mentors={'jack':'m1','johnson':'m2','caty':'m3','miley':'m4'}
    python={'jack':'10:30','johnson':'11:22','caty':'2:30','miley':'4:30'}
    java={'jack':'12:45','johnson':'10:30','caty':'4:30','miley':'2:30'}
    def __init__(self, interest):
        
        self.interest_list.append(interest)
   
    def SetMentorOrLearner(self,pa,id):
         t = id
         count =0
         for i,j in self.mentors.items():
             if j == t:
                 print("participant is a mentor")
                 self.SetAvailableTime()
                 break
             count =count+1
         if(count == len(self.mentors)):
             print("participant is a learner ")
        
    def SetAvailableTime(self):
          named_tuple = time.localtime() # get struct_time
          time_string = time.strftime("%H:%M", named_tuple)
          print("so the available time is",time_string)
          self.GetMentor(time_string,self.interest_list)
          
    def GetMentor(self,tt,uu):
         time = tt
         count =0
         if(self.interest_list == ['python']):
            for k,i in self.python.items():
                if (i == time):
                    print("so the available mentor is",k)
                    break
                count =count+1
            if(count == len(self.python)):
               print("no mentor is available")
                
        
        
        
        
        
g = input("Enter the area of interest or domain")
e=TechLearners(g)
k=input("enter the name of the participant")
i=input("enter the id of the participant")
e.SetMentorOrLearner(k,i)
