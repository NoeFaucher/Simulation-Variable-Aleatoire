# Exo 4

uniform <- function(x) runif(x)

exponentielle <- function(l) -log(1-uniform(1))/l

loi3 <- function(x) sqrt(uniform(x))


S <- function(n,expr,p) {
  sum <- sum(replicate(n,expr(p)))
  return(sum)
}

# m la moyenne
# s l'écart type
Z <- function(n,expr,p,m,s) {
  Sn <- S(n,expr,p)
  return(sqrt(n)*((Sn/n)-m)/s)
}

do_graph <- function(max,expr,p,m,s){
  tab <- replicate(max,Z(max,expr,p,m,s))
  hist(tab,prob=TRUE,plot=TRUE)
}
x<- seq(-3,3,length.out = 1000)
y<- dnorm(x)


do_graph(1000,uniform,1,0.5,sqrt(1/12))
lines(x,y,lwd=2,col="red")
do_graph(1000,exponentielle,0.5,2,2)
lines(x,y,lwd=2,col="red")
do_graph(1000,loi3,1,2/3,sqrt(1/18))
lines(x,y,lwd=2,col="red")

