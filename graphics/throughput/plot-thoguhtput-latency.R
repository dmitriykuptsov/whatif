data<-read.csv("ping.txt", header=T)

mean(data$Latency)
sd(data$Latency)
median(data$Latency)
min(data$Latency)
max(data$Latency)

require(ggplot2)

pdf("ping.pdf")
options(repr.plot.width = 5, repr.plot.height = 2)
ggplot(data, aes(x=Latency, y = after_stat(density))) + 
  geom_histogram(aes(y = after_stat(density)), bins = 10, fill = "blue") +
  xlab("Latency, ms") +
  ylab("Probability") +
  geom_density(color = "black", size = 1.5, alpha = 0.5) +
  theme_minimal()
dev.off()
