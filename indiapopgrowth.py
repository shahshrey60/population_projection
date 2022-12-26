
   
import pandas as pd
import csv
import matplotlib.pyplot as plt
import random
import time
with open("population_data.csv", "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    a = list(reader)
x_india=[]
y_india=[]
birth_rates=[]
death_rates=[]
fertility_rates=[]
popul=[]
year_list=[]
for i in a:
        print(i)
        if(i["\ufeffname"]=="India"):
            birth_rates.append(i['birth_rate'])
            year_list.append(int(i['year']))
            fertility_rates.append(float(i['fertility_rate']))
            death_rates.append(float(i['death_rate']))
            popul.append(float(i['population']))

b=0.0095
d=7.31
f=2.184
c=0

b1=15
b2=20
d1=5
d2=10
f2=7
f1=3
year=year_list[-1]
p=popul[-1]
final_p=[]
for i in range(0,80):
    year+=1
    if(i==40):
        b1-=5
        b2-=8
        d1-=3
        d2-=3
        f2-=2
    if(i==20):
        d1=d1+1
        d2=d2+1
        b1-=3
        b2-=3
        f2-=1
    b=b-((random.randrange(b1,b2))/100000)
    d=d+((random.randrange(d1,d2))/1000)
    f=f-((random.randrange(f1,f2))/1000)
    birth_rates.append(b)
    death_rates.append(d)
    year_list.append(year)
    p1=p*b
    p2=p1*f
    p3=(p/1000)*d
    p4=p2+p-p3
    p=p4
    final_p.append([b,f,d,p,year])
    popul.append(p)
    
a_india=[]
b_india=[]
#print(popul)

x=popul
y=year_list
#print(x)



                
                
    
  
#China
import pandas as pd
import csv
import matplotlib.pyplot as plt
import random
import time
with open("population_data.csv", "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    a = list(reader)
x_china=[]
y_china=[]
birth_rates=[]
death_rates=[]
fertility_rates=[]
popul2=[]
year_list2=[]
for i in a:
        print(i)
        if(i["\ufeffname"]=="China"):
            birth_rates.append(i['birth_rate'])
            year_list2.append(int(i['year']))
            fertility_rates.append(float(i['fertility_rate']))
            death_rates.append(float(i['death_rate']))
            popul2.append(float(i['population']))

b=0.005
d=7.07
f=1.7
c=0
b1=10
b2=15
d1=30
d2=40
f2=3
f1=1
year2=year_list2[-1]
p=popul2[-1]
final_p=[]
for i in range(0,80):
    year2+=1
    if(i==10):
        b1-=5
        b2-=5
        d1+=5
        d2+=5
        f2+=2
    b=b-((random.randrange(b1,b2))/100000)
    d=d+((random.randrange(d1,d2))/1000)
    f=f+((random.randrange(f1,f2))/1000)
    birth_rates.append(b)
    death_rates.append(d)
    year_list2.append(year2)
    p1=p*b
    p2=p1*f
    p3=(p/1000)*d
    p4=p2+p-p3
    p=p4
    final_p.append([b,f,d,p,year2])
    popul2.append(p)
    
a_china=[]
b_china=[]
#print(popul)

x2=popul2
y2=year_list2
#print(x)
#print(len(x))


#Japan
import pandas as pd
import csv
import matplotlib.pyplot as plt
import random
import time
with open("population_data.csv", "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    a = list(reader)
x_japan=[]
y_japan=[]
birth_rates=[]
death_rates=[]
fertility_rates=[]
popul3=[]
year_list3=[]
for i in a:
        print(i)
        if(i["\ufeffname"]=="Japan"):
            birth_rates.append(i['birth_rate'])
            year_list3.append(int(i['year']))
            fertility_rates.append(float(i['fertility_rate']))
            death_rates.append(float(i['death_rate']))
            popul3.append(float(i['population']))

b=0.007
d=11.1
f=1.34
c=0
b1=10
b2=15
d1=30
d2=40
f2=3
f1=1
year3=year_list3[-1]
p=popul3[-1]
final_p=[]
for i in range(0,80):
    year3+=1
    if(i==10):
        b1-=5
        b2-=5
        d1+=5
        d2+=5
        f2+=2
    b=b-((random.randrange(b1,b2))/100000)
    d=d+((random.randrange(d1,d2))/1000)
    f=f+((random.randrange(f1,f2))/1000)
    birth_rates.append(b)
    death_rates.append(d)
    year_list3.append(year3)
    p1=p*b
    p2=p1*f
    p3=(p/1000)*d
    p4=p2+p-p3
    p=p4
    final_p.append([b,f,d,p,year3])
    popul3.append(p)
    
a_japan=[]
b_japan=[]
#print(popul)

x3=popul3
y3=year_list3
#print(x)
#print(len(x))
for i in range(0,len(x3)):
    #print(x[i],y[i])
    if(y3[i]%10==0):
        a_japan.append(y3[i])
        b_japan.append(x3[i]/10000000)
        a_china.append(y2[i])
        b_china.append(x2[i]/10000000)
        a_india.append(y[i])
        b_india.append(x[i]/10000000)
        plt.plot(a_japan,b_japan,label =  " Japan")
        plt.plot(a_china,b_china,label =  " China")
        plt.plot(a_india,b_india,label =  " India")
        plt.plot([2020,2020],[0,170])
        plt.xlabel('Year')
        # naming the y axis
        plt.ylabel('Population Growth (in billions) ')
          
        # giving a title to my graph
        plt.title('Population Projection Curve (I058,I063,I065) ')
        plt.legend()
        # function to show the plot
        plt.show()
        time.sleep(1)
print(min(popul3))