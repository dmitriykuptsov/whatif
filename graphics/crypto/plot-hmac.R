data<-read.csv("clean-data-hmac.txt", header=T)
data<-data[data$Op=="Enc", ]
require(ggplot2)

pdf("hmac.pdf")
options(repr.plot.width = 4, repr.plot.height = 2)
ggplot(data, aes(x = Block, y = Mean, colour = factor(Type))) +
  geom_line(lwd=1.5) + 
  geom_errorbar(aes(ymax = CIP, ymin = CIN)) +
  xlab("Message size, Bytes") +
  ylab("Time, us") +
  guides(colour=guide_legend(title="Implementations")) +
  scale_colour_manual(values=c(Hybrid="blue",Native="pink",Python="black")) +
  theme_minimal() +
  theme(legend.position="bottom", legend.box = "horizontal")
dev.off()
