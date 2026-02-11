#!/usr/bin/env python
# coding: utf-8

# In[1]:


7**4


# In[4]:


s = "Hi there Sam!"
s.split()


# In[7]:


planet = "Earth"
diameter = 12742


print('My diameter of {one}  is: {two}'.format(one=planet,two=diameter))


# In[16]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])


# In[25]:



d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
s=d['k1']
a=


# In[31]:



def domainGet(email):
    
    return email.split('@')

domainGet('user@gmail.com')


# In[36]:


def dawg(st):
    return 'dog'in st.lower().split()

def cdawg(st):
    count=0
    for i in st.lower().split():
        if i=='dog':
            count=count+1
            
    print(count)
dawg("the dog is dog ")
cdawg("what the dog doing in the dishwasherrrr")


# In[39]:


def cs(speed,bday):
    if bday:
        speed=speed-5
    else:
        speed=speed
    if speed>80:
        return 'high fine'
    elif speed>60:
        return 'small ticket'
    else:
        return 'you are fineee'

    
cs(81,True)
cs(81,False)


# In[40]:


my=[1,3,4,5]
my


# In[41]:


type(my)


# In[42]:


import numpy as np


# In[43]:


ar=np.array(my)


# In[44]:


ar


# In[45]:


type(ar)


# In[47]:


mym=[[1,2,3],[4,5,6],[2,2,2]]
np.array(mym)


# In[48]:


np.arange(1,15)


# In[50]:


np.arange(1,15,4)


# In[51]:


np.zeros(5)


# In[53]:


np.zeros((5,5))


# In[54]:


# same goes for np.ones
# linespace function equal part ma divide kari ne ans appe


# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[3]:


np.ones(10)


# In[4]:


np.ones(10)*5


# In[6]:


np.arange(10,51)


# In[7]:


np.arange(10,51,2)


# In[8]:


arr=np.arange(0,9)


# In[9]:


arr


# In[11]:


np.array(arr(3,3))


# In[12]:


marr=[[0,1,2],[3,4,5],[6,7,8]]
np.array(marr)


# In[13]:


np.eye(3)


# In[14]:


np.random.rand(1)


# In[16]:


np.random.randn(25)


# In[18]:


np.linspace(0,1,20)


# In[19]:


np.linspace(0,1,100).reshape(10,10)


# In[21]:


np.arange(0,9).reshape(3,3)


# In[25]:


num=100
for i in range(0,100):
    arr=i
    np.reshape(10,10)


# In[33]:



np.arange(1,101).reshape(10,10)/100


# In[36]:


mat=np.arange(1,26).reshape(5,5)
mat


# In[37]:


mat[2:,1:]


# In[39]:


mat[3:4,4:]


# In[40]:


mat[0:3,1:2]


# In[41]:


mat[4:,:]


# In[42]:


mat[3:,:]


# In[45]:


s =0
for i in mat:
    s=s+i
    
print(s)


# In[46]:





# In[48]:


mat.min()


# In[50]:


mat.min(axis=1)


# In[51]:


mat


# In[52]:


mat.min(axis=0)


# In[53]:


mat.sum(axis=0)


# In[55]:


mat.sum()


# In[2]:


import numpy as np


# In[7]:


iris=np.genfromtxt('iris_numpy.txt',skip_header=1,delimiter=',',dtype=float)







# In[8]:


iris


# In[9]:


iris.shape


# In[10]:


iris.ndim


# In[11]:


iris.size


# In[12]:


sample=iris[0:30,[0,1,2,3,5]]


# In[13]:


sample


# In[14]:


iris1,iris2,iris3=np.split(iris,[50,100],axis=0)


# In[15]:


iris1


# In[16]:


iris2


# In[23]:


header=np.array(['sepal length','sepal width','petal length','petal width','Species No'])
header


# In[24]:


iris


# In[30]:


sample


# In[39]:


nsample=iris[0:150,[0,1,2,3,5]]


# In[40]:


nsample


# In[35]:


mean=nsample.mean(axis=0).round(2)


# In[41]:


mean


# In[45]:


m=nsample.min(axis=0).round(2)


# In[46]:


m


# In[50]:


a=nsample.max(axis=0).round(2)
a


# In[56]:


x=iris1.min(axis=0).round(2)
y=iris2.min(axis=0).round(2)
z=iris3.min(axis=0).round(2)

x[0]>m[0]


# In[57]:


y[0]>m[0]


# In[58]:


z[0]>m[0]


# In[59]:


x


# In[60]:


y


# In[61]:


z


# In[1]:


np.savetxt('iris.txt',nsample,delimiter=',')


# In[2]:


install pandas as pd


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


s1=pd.Series([1,2,3,4,54,5])


# In[6]:


s1


# In[7]:


data=np.arange(1,11)
index=np.arange(101,111)
s2=pd.Series(data,index)


# In[8]:


s2


# In[9]:


s1.iloc[[1,2]]


# In[10]:


s1.[[1,2]]


# In[11]:


s1[[1,2]]


# In[12]:


data2='p','m','k','j','k','s','p','c'
index2=np.arange(1,9)

s2=pd.Series(data2,index2)
s2


# In[13]:


s2[3]


# In[14]:


s2[2,3]


# In[15]:


s2[[2,3]]


# In[16]:


s2[['p']]


# In[17]:


s2


# In[18]:


s3=pd.Series(data,index)


# In[19]:


s3


# In[20]:


s3[[101,102]]


# In[21]:


s6=pd.Series(['New Delhi','WashingtonDC', 'London','Paris'],index=['India','USA','UK','France'])


# In[22]:


s6


# In[23]:


s6[1:]


# In[24]:


s6[-1:]


# In[25]:


s6[:-1]


# In[26]:


s6[-1]


# In[27]:


s6['usa']


# In[28]:


s6['USA']


# In[29]:


S6.index.name='con'


# In[30]:


s6.index.name='con'


# In[31]:


s6


# In[32]:


s6.data.name='sta'


# In[34]:


s6


# In[35]:


s6.values


# In[36]:


s6.size


# In[46]:


import numpy as np
import pandas as pd
s9=pd.Series(np.arange(10,19,1),index=[1,2,3,4,5,6,7,8,9])


# In[40]:


import numpy as np
import pandas as pd


# In[47]:


s9


# In[48]:


s9.head()


# In[49]:


s9.tail()


# In[50]:


s9.count()


# In[51]:


s10=pd.Series(np.arange(101,110),np.arange(1,10))


# In[52]:


s10


# In[53]:


s9


# In[54]:


s10-s9


# In[56]:


ch=[chr(i) for i in range(65,91)]
ch


# In[57]:


EngAlph=pd.Series(ch)


# In[58]:


EngAlph


# In[61]:


Vowels=pd.Series([0,0,0,0,0],['A','E','I','O','U'])


# In[62]:


Vowels


# In[63]:


d={1:'a',2:'b',3:'c',4:'d',5:'e'}


# In[64]:


d


# In[65]:


Friends=pd.Series(d)


# In[66]:


Friends


# In[67]:


MTseries=pd.Series()


# In[68]:


MTseries


# In[69]:


MTseries.empty


# In[1]:



np


# In[2]:


import numpy as np
import pandas as pd


# # data frame

# In[3]:


np


# In[12]:


data=[1,2,3,4]
data2=[2,3,4,2]
index=[101,102,103,104]

a=pd.DataFrame([data2,data],columns=index)
a


# In[15]:


d2={'state':['bla','bla','bla'],'area':[1,3,4],'pop':[4,5,6]}


# In[16]:


df3=pd.DataFrame(d2)


# In[17]:


df3


# In[40]:


sa=pd.Series([100,200,4,5,3],index=['a x d f s'.split()])


# In[41]:


sa


# In[42]:


sb=pd.Series([10,0,4,5,883],index=['a x d f s'.split()])


# In[43]:


sb


# In[24]:


df99=pd.DataFrame(sa)


# In[30]:


df99


# In[28]:


df98=pd.DataFrame(sb)


# In[31]:


df98


# In[44]:


df78=pd.DataFrame([sa,sb])


# In[45]:


df78


# In[46]:


np.random.randn(101)


# In[48]:


from numpy.random import randn
np.random.seed(102)

df8=pd.DataFrame(randn(5,4),index='a b c d e',split(),columns='w x y z'.split())
df8


# In[1]:


import numpy as np
import pandas as pd


# In[4]:


from numpy.random import randn
df=pd.DataFrame(randn(5,5),index=['a b c d e'.split()])


# In[5]:


df


# In[6]:


new=[1,2,3,4,5]
df['WIN']=new


# In[7]:


df


# In[16]:


df.set_index('WIN',inplace=True)


# In[17]:


df


# In[19]:


outer=['P1','P1','P1','P2','P2','P2']
inner=[1,2,3,1,2,3]
findex=list(zip(outer,inner))
findex=pd.MultiIndex.from_tuples(findex)


# In[20]:


df=pd.DataFrame(np.random.randn(6,3),index=findex,columns=['A','B','C'])


# In[21]:


df


# In[22]:


df.loc['P1']


# In[23]:


df.loc['P1'].loc[2]


# In[24]:


df.index.names=['haha','HAHA']


# In[25]:


df


# In[26]:


df.xs('P1')


# In[27]:


df.xs(('P1',1))


# In[28]:


df.mean()


# In[34]:


df2=pd.DataFrame({'A':[1,2,3,4],'B':[np.nan,np.nan,700,66],'C':[34,np.nan,44,322],'D':[4,5,np.nan,89]})
df2


# In[35]:


df2.describe()


# In[36]:


df2.describe().transpose()


# In[37]:


df2.dropna()


# In[39]:


df2.dropna(axis=0)


# In[40]:


df2.dropna(axis=1)


# In[41]:


df2.fillna(value="hehe")


# In[49]:


data = {'Company':['MST','GOOG','MST','GOOG','FB','FB'],
'Person':['Sam','Raj','Amy','Ria','Kia','Sarah'],
'Sales':[200,120,340,124,243,350]}
df3=pd.DataFrame(data)


# In[50]:


df3


# In[57]:


a=df3.groupby(by="Company")


# In[58]:


df3


# In[60]:


print(a)


# In[61]:


a.min()


# In[62]:


a.max()


# In[63]:


a.count()


# In[65]:


df3['Company'].unique()


# In[66]:


def dumb(x):
    return x+100


# In[67]:


df3['Sales'].apply(dumb)


# In[68]:


df3


# In[69]:


del df3['Person']


# In[70]:


df3


# In[72]:


print(df3.columns)
print(df3.index)


# In[73]:


df3.sort_values(by='Sales')


# In[146]:


df = pd.read_csv('Salaries.csv')


# In[75]:


df


# In[76]:


df.info()


# In[78]:


df['BasePay'].mean()


# In[80]:


df['OvertimePay'].max()


# In[98]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# In[99]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# In[106]:


maxx=df['TotalPay'].max()
df[df['TotalPay']==maxx]


# In[107]:


minn=df['TotalPay'].min()
df[df['TotalPay']==minn]


# In[110]:


df.groupby('Year')


# In[111]:


a=df.groupby('Year')


# In[114]:


a.mean("BasePay")['BasePay']


# In[117]:


df['JobTitle'].nunique()


# In[120]:


df['JobTitle'].value_counts().head()


# In[131]:


sum(df[df['Year']==2013]['JobTitle'].value_counts()==1) 


# In[142]:


cc=0
def check(q):
    if 'cheif' in q.lower:
        
        return True
    else:
        return False


sum(df[df['JobTitle'].apply(check)].value_counts()==True)


# In[ ]:


sum(df[df['JobTitle'].apply(check)].value_counts()==True)


# In[144]:


df2= pd.read_csv('Ecommerce Purchases')


# In[147]:


df2


# In[148]:


df2.info()


# In[149]:


df2['Purchase Price'].mean()


# In[150]:


df2['Purchase Price'].max()


# In[151]:


df2['Purchase Price'].min()


# In[157]:


df2[df2['Language']=='en'].apply(len)['Language']


# In[161]:


df2[df2['Job']=='Lawyer'].apply(len)


# In[164]:


df2[df2['AM or PM']=='AM'].apply(len)['AM or PM']


# In[165]:


df2[df2['AM or PM']=='PM'].apply(len)['AM or PM']


# In[169]:


df2.groupby('Job')
aa=df2.groupby('Job')


# In[ ]:




