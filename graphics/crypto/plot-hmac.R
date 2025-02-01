data<-read.csv("clean-data-hmac.txt", header=T)
data<-data[data$Op=="Enc", ]
require(ggplot2)

pdf("hmac.pdf")
options(repr.plot.width = 4, repr.plot.height = 2)
ggplot(data, aes(x = Block, y = Mean, colour = factor(Type))) +
  theme(
    panel.background = element_rect(fill = "lightblue",
                                colour = "lightblue",
                                size = 0.5, linetype = "solid"),
    panel.grid.major = element_line(size = 0.5, linetype = 'solid',
                                colour = "white"), 
    panel.grid.minor = element_line(size = 0.25, linetype = 'solid',
                                colour = "white")
  ) +
  geom_line() + 
  geom_errorbar(aes(ymax = CIP, ymin = CIN)) +
  xlab("Message size, Bytes") +
  ylab("Time, us") +
  guides(colour=guide_legend(title="Implementations"))
dev.off()
