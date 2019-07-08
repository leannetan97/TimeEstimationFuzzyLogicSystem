#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
#Author : TAN LAY YAN WIF160058


# In[2]:


#     System name : Patient waiting time estimation system
#     length_of_queue = queue
#     availability_of_doctor = availability
#     estimation_time = time (in min)

# New Antecedent
queue = ctrl.Antecedent(np.arange(0,11,1),'queue')
availability = ctrl.Antecedent(np.arange(0,11,1),'availability')
time = ctrl.Consequent(np.arange(0,60,1),'time')


# In[3]:


# Auto-membership function
queue_name = ['short','moderate', 'long']
availability_name = ['busy','moderate', 'free']
time_name = ['short','moderate', 'long']
queue.automf(names = queue_name)
availability.automf(names = availability_name)
time.automf(names = time_name)


# In[4]:


# show Graph
# get_ipython().run_line_magic('matplotlib', 'inline')
queue.view()
availability.view()
time.view()
plt.show()


# In[5]:


# Generate rules
rule1 = ctrl.Rule(queue['short'], time['short'])
rule2 = ctrl.Rule(queue['moderate'] & availability['free'], time['short'])
rule3 = ctrl.Rule(queue['moderate'] & availability['moderate'], time['moderate'])
rule4 = ctrl.Rule(queue['moderate'] & availability['busy'], time['long'])
rule5 = ctrl.Rule(queue['long'] & availability['free'], time['moderate'])
rule6 = ctrl.Rule(queue['long'] & availability['moderate'], time['long'])
rule7 = ctrl.Rule(queue['long'] & availability['busy'], time['long'])


# In[6]:


# Set up controler
time_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7])
time_estimate = ctrl.ControlSystemSimulation(time_ctrl)


# In[8]:


# taking input
time_estimate.input['queue'] = 8
time_estimate.input['availability'] = 3 

# mom = mean of max
queue.defuzzify_method = 'mom' 
availability.defuzzify_method = 'mom'
time.defuzzify_method = 'mom'

# Compute output
time_estimate.compute()

# display output
print(time_estimate.output['time'])

# view graph
# time.view(sim=time_estimate)




