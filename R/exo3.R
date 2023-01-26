# Exo 3

uniform <- function(x) runif(x)

exponentielle <- function(l) -log(1-uniform(1))/l

loi3 <- function(x) sqrt(uniform(x))

estimateur <- function(n,expr,p) {
  sum <- sum(replicate(n,expr(p)))
  return(sum/n)
}

do_graph <- function(max,expr,p,moy){
  tab <- c()
  for (i in 1:max){
    tab <- c(tab,estimateur(i,expr,p))
  }
  
  plot(tab,type="l",)
  abline(h=moy,col="red") 
  
}


# 1 
do_graph(1000,uniform,1,0.5)
# 2 
do_graph(1000,exponentielle,0.5,2)
# 3 
do_graph(1000,loi3,1,0.666666666666)



           