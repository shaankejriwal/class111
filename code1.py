import random
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

p_mean = statistics.mean(data)
p_std_deviation = statistics.stdev(data)

print("population mean = ",p_mean)
print("population standard deviation = ",p_std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
print("the mean of sample is = ",mean)
std_deviation = statistics.stdev(mean_list)
print("the standard deviation of sample is = ",std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df1 = pd.read_csv("data1.csv")
data1 = df["Math_score"].tolist()
mean1 = statistics.mean(data1)
print("mean of dataset 1 is = ",mean1)

df2 = pd.read_csv("data2.csv")
data2 = df["Math_score"].tolist()
mean2 = statistics.mean(data2)
print("mean of dataset 2 is = ",mean2)

df3 = pd.read_csv("data3.csv")
data3 = df["Math_score"].tolist()
mean3 = statistics.mean(data3)
print("mean of dataset 3 is = ",mean3)

fig = ff.create_distplot([mean_list],["data"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.20],mode = "lines",name = "MEAN1"))
fig.add_trace(go.Scatter(x = [mean2,mean2],y = [0,0.20],mode = "lines",name = "MEAN2"))
fig.add_trace(go.Scatter(x = [mean3,mean3],y = [0,0.20],mode = "lines",name = "MEAN3"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0,0.20],mode = "lines",name = "FIRST STANDARD DEVIATION START"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0,0.20],mode = "lines",name = "FIRST STANDARD DEVIATION END"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start],y = [0,0.20],mode = "lines",name = "SECOND STANDARD DEVIATION START"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0,0.20],mode = "lines",name = "SECOND STANDARD DEVIATION END"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start],y = [0,0.20],mode = "lines",name = "THIRD STANDARD DEVIATION START"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end],y = [0,0.20],mode = "lines",name = "THIRD STANDARD DEVIATION END"))
fig.show()

