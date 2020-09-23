#!/usr/bin/env python
# coding: utf-8

# Let's read the data using the open 

# In[15]:


f = open("data.txt", "r")
print(f.read())


# Let's define the top_list which is the first two rows of the list.

# In[16]:


top2_list=[]


# In[17]:


def topNlines(fname, N): 
	# opening file using with() method 
	# so that file get closed 
	# after completing work 
	with open(fname) as file: 
		
		# loop to read iterate 
		# last n lines and print it 
		for line in (file.readlines() [0:N]):
			top2_list.append(line)
			print(line, end ='') 


# Driver Code: 
if __name__ == '__main__': 
	fname = 'data.txt'
	N = 3
	try: 
		topNlines(fname, N) 
	except: 
		print('File not found')


# Printing the top list

# In[18]:


print(top2_list)


# In order to store the rest of the data, let's define the data_list and print the last rows
# 

# In[19]:


data_list=[]


# In[21]:


def lastNlines(fname, N): 
	# opening file using with() method 
	# so that file get closed 
	# after completing work 
	with open(fname) as file: 
		
		# loop to read iterate 
		# last n lines and print it 
		for line in (file.readlines() [N:25]):
			data_list.append(line)
			print(line, end ='') 


# Driver Code: 
if __name__ == '__main__': 
	fname = 'data.txt'
	N = 3
	try: 
		lastNlines(fname, N) 
	except: 
		print('File not found')


# In[22]:


data_list


# In order to extract and remove the "*" we are making a temp list and then putting the final report in year_list

# In[27]:


year_list = []
for i in range(0,len(data_list)):
    temp = data_list[i].split('\t')
    if '*' in temp[0]:
        year_list.append(temp[0].replace('*',''))
    else:
        year_list.append(temp[0])
    #print(temp)
print(year_list)    


# In order to extract and remove the "," we are making a temp list and then putting the final report in pop_list

# In[28]:


pop_list = []
for i in range(0,len(data_list)):
    temp = data_list[i].split('\t')
    pop_list.append(temp[1].replace(',',''))
print(pop_list)


# In order to Remove the ",", and "$", and "Billion" we are making a temp list and then putting the final report in cost_list

# In[32]:


cost_list = []
for i in range(0,len(data_list)):
    temp = data_list[i].split('\t')
    dummy = temp[2].replace('$','')
    dummy = dummy.replace(',','')
    if 'Billion' in dummy:
        dummy = dummy.replace('Billion','')
        dummy = float(dummy)*(10^9)
    cost_list.append(dummy)

print(cost_list)


# In order to Remove the "cents", and "$" we are making a temp list and then putting the final report in avg_list

# In[39]:


avg_list = []
for i in range(0,len(data_list)):
    temp = data_list[i].split('\t')
    dummy1 = temp[3].replace('$','')
    dummy1 = dummy1.replace('cents','')
    dummy1 = float(dummy1)/100
    avg_list.append(dummy1)
print(avg_list)


# putting everything in csv

# In[46]:


import csv

with open('census_cost.csv', 'r', newline='') as f:
    fieldnames = ['year_list','pop_list','cost_list','avg_list']
    thewriter = csv.DictWriter(f, fieldnames= fieldnames)


# In[47]:


print(thewriter)


# In[56]:


with open('census_cost.csv') as file1:
    for i in range(0, len(fieldnames)):
        file1.write(str(fieldnames[i])
    for i in range(0,len(year_list)):
                    file1.write(str(year_list[i]))
                    file1.write(str(pop_list[i]))
                    file1.write(str(cost_list[i]))
                    file1.write(str(avg_list[i]))        


# In[ ]:




