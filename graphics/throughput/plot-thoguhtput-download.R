data<-read.csv("download.txt", header=T)

require(ggplot2)

pdf("download.pdf")
options(repr.plot.width = 5, repr.plot.height = 2)
ggplot(data, aes(x=Throughput / 1024, y = after_stat(density))) + 
  geom_histogram(aes(y = after_stat(density)), bins = 10, fill = "blue") +
  xlab("Throughput, Mbits/s") +
  ylab("Probability") +
  geom_density(color = "black", size = 1.5, alpha = 0.5) +
  theme_minimal()
dev.off()
