# Exo 5

uniform <- function(x) runif(x)



varX <- function() {
  U <- uniform(1)
  V <- uniform(1)
  
  return(sqrt(-2*log(U))*cos(2*pi*V))
}

varY <- function() {
  U <- uniform(1)
  V <- uniform(1)
  
  return(sqrt(-2*log(U))*sin(2*pi*V))
}

x<- seq(-3,3,length.out = 1000)
y<- dnorm(x)

# X 

sample <- replicate(1000,varX())
hist(sample,border="black",prob=TRUE,xlab="Valeur",ylab="Densité" ,main="Histogramme de la variable X",col="peachpuff")
lines(x,y,lwd=2,col="red")

# Y

sample <- replicate(1000,varY())
hist(sample,border="black",prob=TRUE,xlab="Valeur",ylab="Densité" ,main="Histogramme de la variable Y",col="peachpuff")
lines(x,y,lwd=2,col="red")