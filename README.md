### Single Channel Queue
The implementation of python projects deals with one problem of single-channel queuing problems. It shows that a single-channel queuing model without losses can be used to solve queuing problems. It is composed of the queue and service center and uses the FIFO system.A single-channel queue can be used for a bank system /ticket counter service/any delivery service.

### Requirements
* Python 3.8
* Pandas
* Spyder
* Numpy
* Matplotlib

### Introduction
To describe queuing problems through mathematical formulation, some assumptions are made by considering arrivals and services as patterned by known function. Equations representing the distribution of the time between arrivals are used with other equations depicting other features such as the distribution of the service time. The relationship existing between these equations is the matter studied in waiting line theory. Arrivals of people or entry requirements (events) are customarily Poisson distributed. The duration of the service provided by people is usually exponentially distributed. For generating interarrival and service times, gamma and Weibull distributions are also utilized depending on the model as the exponential distribution is said to be a special case of both of the gamma and Weibull distributions.

### Random Variable
A random variable is a variable whose possible values are numerical outcomes of a random phenomenon. There are two types of random variables, discrete and continuous.

A discrete random variable may take on only a countable number of distinct values and thus can be quantified. For example, you can define a random variable X to be the number that comes up when you roll a fair dice. X can take values : [1,2,3,4,5,6] and therefore is a discrete random variable.

Some examples of discrete probability distributions are Bernoulli distribution, Binomial distribution, Poisson distribution, etc.

A continuous random variable takes an infinite number of possible values. For example, you can define a random variable X to be the height of students in a class. Since the continuous random variable is defined for values, it is represented by the area under a curve (or the integral).

A curve meeting needed requirements is often known as a density curve. Some examples of continuous probability distributions are normal distribution, exponential distribution, beta distribution, etc.

There’s another type of distribution that often pops up in literature which you should know about called cumulative distribution function. All random variables (discrete and continuous) have a cumulative distribution function. It is a function giving the probability that the random variable X is less than or equal to x, for every value x. For a discrete random variable, the cumulative distribution function is found by summing up the probabilities.


### Poison Distribution fot Inter Arrival time 
The Poisson is a discrete probability distribution and yields the number of arrivals in a given time. The exponential distribution is a continuous function and yields the distribution of the time intervals between arrivals. The Poisson distribution considers the behavior of arrivals as occurring at random and postulates the presence of a constant “λ” which is independent of the time. The constant λ represents the mean arrival rate or the number of arrivals per unit of time, and λ 1 is the length of the time interval between two consecutive arrivals.


### Exponential Distribution for Service Time
In Exponential Distribution, we can generate an exponentially distributed random variable using scipy.stats module's expon.rvs() method which takes shape parameter scale as its argument which is nothing but 1/lambda in the equation. To shift distribution use the loc argument, size decides the number of random variates in the distribution.


### Problem We Have Faced
There was a problem in our first submission. In a floating point value we had used a long number after point. By the direction of our supervisor we have overcome this problem in our final release.


### Contributors
1. Sujoy Saha 
2. Sajib Debnath
3. [Tutul Roy](https://github.com/TUTULROY)
4. Md. Ali Mortuja
5. Ridoy


### Supervisor
Honourable [Muhtadir Shihab](https://github.com/Muhtadir) Sir.


