# Add the functions in this file
import math
import json
def load_journal(filename):
  f=open(filename)
  s=f.read()
  d=json.loads(s)
  return d
  
  


def compute_phi(filename,event):
   m=load_journal(filename)
   a=b=c=e=n1=n0=n_1=n_0=0
   
   
   for i in m:
      if event in i['events']:
           n1=n1+1
           if i['squirrel']== True:
             a=a+1
           else:
             c=c+1
      else:
         n0=n0+1
         if i['squirrel']:
            e=e+1
         else:
            b=b+1
      if i['squirrel']:
         n_1=n_1+1
      if not i['squirrel']:
         n_0=n_0+1
       
   phi=(a*b-c*e)/math.sqrt(n1*n0*n_1*n_0)
   return phi
   
def compute_correlations(filename):
   d=load_journal(filename)
   event_list=[]
   for i in d:
     for j in i['events']:
       if j not in event_list:
          event_list.append(j)
   #print(event_list)
   k={}
   for event in event_list:
     k[event]=compute_phi(filename,event)
   return k
   
def diagnose(filename):
   k=compute_correlations(filename)
   max=-1
   key_list=list(k.keys())
   value_list=list(k.values())
   min=1
   
   for i in k.keys():
     if k[i]>max:
       
       max=k[i]
       
       
     if k[i]<min:
       min=k[i]
   pos=value_list.index(max)
   pos1=value_list.index(min)
   max_key=key_list[pos]
   min_key=key_list[pos1]
   return max_key,min_key
#diagnose("journal.json")
