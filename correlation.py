# Add the functions in this file
import math
import json
def load_journal(file_name):
  
  
  f=open(file_name)
  s=f.read()
  d=json.loads(s)
  return d


def compute_phi(m,event):
   
   a=b=c=e=n1=n0=n_1=n_0=0
   
   
   for i in m:
       
      if event in i['events']:
           n1=n1+1
           if i['squirrel']:
             a=a+1
           if not i['squirrel']:
             c=c+1
      if event not in i['events']:
         n0=n0+1
         if i['squirrel']:
            e=e+1
         if not i['squirrel']:
            b=b+1
      if i['squirrel']:
         n_1=n_1+1
      if not i['squirrel']:
         n_0=n_0+1
       
   phi=(a*b-c*e)/math.sqrt(n1*n0*n_1*n_0)
   return phi
   
def compute_correlations(file_name):
   d=load_journal(file_name)
   event_list=[]
   for i in d:
     for j in i['events']:
       if j not in event_list:
          event_list.append(j)
   #print(event_list)
   k={}
   for i in event_list:
     k[i]=compute_phi(d,i)
   return k
   
def diagnose(file_name):
   k=compute_correlations(file_name)
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
