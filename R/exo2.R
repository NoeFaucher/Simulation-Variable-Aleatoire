
uniform <- function(x) runif(x)

# 1
bernoulli <- function(p) 1-p<=uniform(1)

barplot(table(replicate(100,bernoulli(0.5))),col=c("red","blue"),main="100 expériences de Bernoulli de paramètre 0.5")
bernoulli(0.5)


# 2
geometrique <- function(p) {
  u<-uniform(1)
  f <-0
  x <-0
  while(u>f){
    x <- x+1
    f <- 1-(1-p)^x
  }
  return(x)
}
geometrique(0.0005)


# 3
poisson <- function(l) {
  u<-uniform(1)
  f <-exp(-l)
  x <-0
  while(u>f){
    x <- x+1
    f <- f+ (exp(-l)*(l^x))/factorial(x)
  }
  return(x)
}

poisson(100)


# 4
exponentielle <- function(l) -log(1-uniform(1))/l

exponentielle(0.00000005)
