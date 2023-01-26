# Exo 1

uniform <- function(x) runif(x)


# 1
bernoulli <- function(p) p>uniform(1)


barplot(table(replicate(100,bernoulli(0.5))),col=c("red","blue"),main="100 expériences de Bernoulli de paramètre 0.5")
bernoulli(0.5)


# 2
binomiale <- function(n,p) sum(replicate(n,bernoulli(p)),na.rm=TRUE)

binomiale(1000,0.5)


# 3
geometrique <- function(p) {
  cpt=1
  while(!bernoulli(p)){ cpt<-cpt+1}
    
  return(cpt)
}

geometrique(0.001)

# 4
uniform2 <- function(k) floor(1+(k+1-1)*uniform(1))

replicate(10,uniform2(5))

# 5 
uniform3 <- function() 2*uniform(1)-1
test <-replicate(100000,uniform3())
hist(test,border="black",prob=TRUE,xlab="Valeur",ylab="Densité" ,main="Uniforme [-1,1]",col="peachpuff")
lines(density(test),lwd = 2,col="red")

