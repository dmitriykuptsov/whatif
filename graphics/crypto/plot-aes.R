data<-read.csv("clean-data-aes.txt", header=T)
data<-data[data$Op=="Enc", ]
require(ggplot2)

pdf("aes.pdf")
options(repr.plot.width = 5, repr.plot.height = 2)
ggplot(data, aes(x = Block, y = Mean, colour = factor(Type))) +
  geom_line() + 
  geom_errorbar(aes(ymax = CIP, ymin = CIN)) +
  xlab("Message size, Bytes") +
  ylab("Time, us") +
  guides(colour=guide_legend(title="Implementations")) +
  scale_fill_manual(values = c("blue", "pink", "red")) +
  theme_minimal()
dev.off()
