setwd("~/Desktop/Fall 2018/SYS 6018/Kaggle/Bloggers")

train.original <- read.csv("train.csv")
test.original <- read.csv("test.csv")

traindata <- read.csv("trainupdated.csv")
testdata <- read.csv("testupdated.csv")

train.original <- train.original[,1:5]
traindata <- cbind(traindata, train.original)
y <- train.original[,8]

test.original <- test.original[,1:5]
testdata <- cbind(testdata, test.original)


#load("hw2simdatatrain.Rdata")
#load("hw2simdatatest.Rdata")

#traindata <- data.frame(traindata)
#testdata <- data.frame(testdata)
train.y <- cbind(traindata, y)

#Split train.y into 80% training data and 20% test data
test.set <- function(data, size)
{
  a <- sample(1:nrow(data), round(size*nrow(data)))
  b <- setdiff(1:nrow(data), a)
  list(test =data[a,], train = data[b,])
}
train.y_subsection <- test.set(train.y, 0.2)

# Create OLS
train.ols <- lm(y ~ ., data = train.y_subsection$train)
#summary(train.ols)
AIC(train.ols)
BIC(train.ols)

# # Step for OLS
# train.ols.step <- step(train.ols)
# summary(train.ols.step)
# AIC(train.ols.step)
# BIC(train.ols.step)
# # The stepped ols was implemented because it had higher AIC/BIC and less predictors

install.packages('glmnet')
library(glmnet)

training.x <- as.matrix(train.y_subsection$train[-c(2007)])
training.y <- as.matrix(train.y_subsection$train[c(2007)])
testdata.x <- as.matrix(train.y_subsection$test[-c(2007)])
testdata.y <- as.matrix(train.y_subsection$test[c(2007)])

# Do ridge regression
train.ridge <- glmnet(training.x, training.y, alpha=0)

# Do lasso regression
train.lasso <- glmnet(training.x, training.y, alpha=1)

# Predict with OLS and get root mean square error
train.ols.step.predict <- predict(train.ols, data.frame(testdata.x), type = "response")
rmse.ols.step <- sqrt(mean((train.ols.step.predict - data.frame(testdata.y))^2))
rmse.ols.step

# Cross validation for ridge to get min lambda
cv.train.ridge <- cv.glmnet(training.x, training.y, alpha=0)
cv.train.ridge$lambda.min

# Predict with the best lambda for ridge
train.ridge.predict <- predict(train.ridge, s = cv.train.ridge$lambda.min, newx = testdata.x)

# Rmse of ridge
rmse.ridge <- sqrt(mean((train.ridge.predict - testdata.y)^2))
rmse.ridge

# Cross validation for lasso
cv.train.lasso <- cv.glmnet(training.x, training.y, alpha=1)
cv.train.lasso$lambda.min

# Predict with the best lambda
traindata.lasso.predict <- predict(train.lasso, s = cv.train.lasso$lambda.min, newx = testdata.x)

# Rmse of lasso
rmse.lasso <- sqrt(mean((traindata.lasso.predict - testdata.y)^2))
rmse.lasso

#Pick model with the lowest absolute error of any of the models