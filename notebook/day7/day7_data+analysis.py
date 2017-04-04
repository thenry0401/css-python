
# coding: utf-8

# In[4]:

from functools import reduce
import math #sqrt 함수 쓰기위해
import pickle


def average(scores): #score = [95, 23, 46, 25]
    return reduce(lambda a, b: a + b, scores)/len(scores)

def variance(scores, arvg): #scores = [95, 23, 25, 62] avrg = 50, #sum((각 점수 - 평균)**2) / 데이터의 개수
     return reduce(lambda a, b: a + b, map(lambda s:(s-avrg)**2, scores))/len(scores)                   



# In[53]:

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")



# In[29]:

f = open("class_A.bin", "rb")


# In[30]:

items = []
while True:
    try:
        data = pickle.load(f)
    except EOFError:
        break
    items.append(data)
print(items)    


# In[31]:

dic = dict(one=1, two=2, three=3)
dic


# In[32]:

dic.values()


# In[33]:

scores = []

for item in items:
    for value in item.values():
        scores.append(value)
        
scores


# In[34]:

avrg = average(scores)
avrg


# In[35]:

vari = round(variance(scores, avrg),1)
vari


# In[36]:

std_dev = round(math.sqrt(vari),1)
std_dev


# In[54]:


evaluateClass(avrg, std_dev)


# In[51]:

a= 12 
b = "abc"
print("{}는 재밌어, {}는 싫어".format(a,b))
age = 18
name = "greg"
print("내 이름은 {n}이고 나이는 {a}인데 그 나이 {a}는 사실 거짓말이야".format(n = name, a = age))

print(age, end = "   ")
print(name)
print(age,name)

print("내 이름은 {0}이고 나이는 {1}인데 그 나이 {1}는 사실 거짓말이야".format(name, age))



# In[ ]:



