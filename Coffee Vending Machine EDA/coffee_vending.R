library(tidyverse)
library(lubridate)
library(psych)
library(patchwork)

setwd("C:/Users/Kath/Desktop")
sales <- read.csv("index.csv")

colnames(sales)
dim(sales)

table(sales$cash_type) # most users pay by card
describeBy(sales, group = sales$DOTW)
describeBy(sales, group = sales$coffee_name)



length(unique(sales$card))

sales$DOTW <- wday(sales$date)

table(sales$DOTW)

# Most common hour of purchase
hist(sales$DOTW)
hour(sales$datetime) %>% table

# Most profitable DOTW and hour
dotw <- pivot_wider(sales, names_from = DOTW, values_from = )
ggplot(sales, aes(x=DOTW, y=money, group=DOTW)) +geom_boxplot()


# Exploring DOTW ----------------------------------------------------------

table(sales$DOTW)

# most busy DOTW
busy_DOTW <- ggplot(sales, aes(x=DOTW)) + geom_histogram() +
  xlab("Day of the Week") + ylab("Daily Transactions")

# most profitable DOTW
profit_DOTW <- sales %>% group_by(DOTW) %>% summarize(profit=sum(money)) %>%
  ggplot(aes(x=DOTW, y=profit)) + geom_point()

busy_DOTW + profit_DOTW

# Exploring coffee type ---------------------------------------------------

table(sales$coffee_name)

n_drinks <- sales %>% count(coffee_name) %>%
  ggplot(aes(x=coffee_name, y=n)) +
  geom_bar(stat = 'identity') + xlab("Type of Drink") + ylab("Total Sales") +
  ggtitle("Number of Sales for Each Type of Drink") +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))


drink_profits <- sales %>% group_by(coffee_name) %>%
  summarise(profit=sum(money)) %>%
  ggplot(aes(x=coffee_name, y=profit)) +
  geom_bar(stat = 'identity') + xlab("Type of Drink") + ylab("Total Profit") +
  ggtitle("Profit By Type of Drink") +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))

n_drinks + drink_profits

write.csv(sales, "coffee_sales.csv")
