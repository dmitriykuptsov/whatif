data<-read.csv("upload.txt", header=T)

mean(data$Throughput / 1024)
sd(data$Throughput / 1024)
median(data$Throughput / 1024)
min(data$Throughput / 1024)
max(data$Throughput / 1024)

require(ggplot2)

pdf("upload.pdf")
options(repr.plot.width = 5, repr.plot.height = 2)
ggplot(data, aes(x=Throughput / 1024, y = after_stat(density))) + 
  geom_histogram(aes(y = after_stat(density)), bins = 10, fill = "blue") +
  xlab("Throughput, Mbits/s") +
  ylab("Probability") +
  geom_density(color = "black", size = 1.5, alpha = 0.5) +
  theme_minimal()
dev.off()
