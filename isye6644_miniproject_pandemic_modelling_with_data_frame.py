#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Function to infect a student
def infect_student(ls,li):
    ls.pop()
    li.append([4])
    
# Function to reduce the number of days of infection possible for infected person, when a day is over.
def update_infected(li):
    for l in li:
        l[0]-=1
    return li    

# Function to reduce the number of infected student
def reduce_infected():
    global li
    olen=len(li)
    li =[l for l in li if l[0]>0]
    clen= olen - len(li)
    global ls
    if clen>0:
        for i in range(0,clen):
            r.append(1)
    return clen

# Function to recover the infected kids after 3 days of infection so that they not susceptible anymore
def recover_kids(clen,r):
    for i in range(0,clen):
        r.append(1)
    return r

# Function to track the count number of susceptible, infected and recovered student
def count_stats(ls,li,r):
    return print((len(ls),len(li),len(r)))


# In[6]:


# libaries used in Simulation
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt 
import pandas as pd
# Global Vairbles
# random.seed(100) # seed for replication
sim_length= 200 # simulation length
sim_trail= 1000 # trails

df=pd.DataFrame({'trial':[],'days':[],'infected':[],'susceptible':[],'recovered':[] })



for trail in range(1, sim_trail+1):
    
    ls=[1]*20 #list of susceptible
    li=[[3]] #list of infected
    r=[]#list of recovered
    n = 1 # number bernoulli trail
    prob_inf=0.02 # Probability of infection
    count=1
    print("\ntrail: ",trail)
     # Simulation:
    print("\nIntially Tommy was infected")
    print("Infection count {}".format(count))
    print("\n No. of infected person : {} with their potential infection periods {}\n".format(len(li),li))
    for t in range(1,sim_length+1):
        df.loc[len(df.index)] = [trail,t, len(li),len(ls),len(r)] 
        if(t>1):
            update_infected(li)
            reduce_infected()
            print("\n No. of infected person : {} with their potential infection periods {}\n".format(len(li),li))
        if(len(li)==0):
            print(t)
            break


        for istudent in range(0,len(li)):

            for sstudent in range(0,len(ls)):
                if np.random.binomial(n, prob_inf, 1) ==1:              
                    infect_student(ls,li)
                    count+=1
                    print("Infection count {}".format(count))
        print("Count of susceptible, infected and recovered students:" )
        count_stats(ls,li,r)




# In[7]:


df


# In[8]:


data_aggregate = df.groupby(df['days']).mean()


# In[9]:


plt.rcParams["figure.figsize"] = 16,8
new_df = df
del new_df['trial']
data_aggregate = new_df.groupby(df['days']).mean().plot()
plt.xlabel("Time(days)", fontsize = 12)
plt.ylabel("Proportion", fontsize = 12)


# In[10]:


mean_infected = df.groupby('days')['infected'].mean()
mean_infected


# In[11]:


# We changed the no of trials to 1 and then we ran this code to get the graph indicating till when the epidemic last
import numpy as np
import matplotlib.pyplot as plt 

df["inf"]=21
df['inf']=df['inf'] -(df['recovered']+df['susceptible'])
df

# creating the dataset
a =dict(zip(df['days'],df['inf']))
days = list(a.keys())
days.append(days[-1]+1)

values = list(a.values())
values.append(0)
fig = plt.figure(figsize = (10, 5))
x_ticks = np.arange(1, max(df['days'])+3, 1)
plt.xticks(x_ticks)
# creating the bar plot
plt.bar(days, values, color ='green', width = 0.4, label='values')

plt.xlabel("Days")
plt.ylabel("No. of students indfected")
plt.title("SIR ")


plt.show()
plt.show()


# In[ ]:




