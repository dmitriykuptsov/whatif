data<-scan("throughput.txt")
m<-mean(data)
s<-sd(data)
n<-length(data)
df=n-1
cl<-0.95
print(m)
print(qt(cl, df)*s/sqrt(n))
