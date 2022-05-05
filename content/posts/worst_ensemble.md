---
title: "Worst-case scenario for a model ensemble"
date: 2022-05-03
---

# Formalizing the problem

Let us consider $2n+1$ models performing a classification task on a test set consisting of $N$ data points. The models all have the exact same accuracy $a$, which we will conveniently choose so that $Na=A$, the number of correctly predicted instances, is an integer. For convenience, let us also define $E=N-A$, the number of incorrectly predicted instance for each model.

We want to define a model ensemble by majority voting, which will predict correctly a data point if $n+1$ models at least predict it correctly.

What is the worse possible accuracy that this model ensemble can reach?

## Result

The worst number $E^*_\text{ens}$ of data points incorrectly predicted by such a model ensemble verifies

$$ (2n+1) \left(1+\left\lfloor\frac{E}{n+1}\right\rfloor\right) \geq E^*_\text{ens} \geq (2n+1) \left\lfloor\frac{E}{n+1}\right\rfloor.$$

The lower bound is actually $\min\left(N,(2n+1) \left\lfloor\dfrac{E}{n+1}\right\rfloor\right)$, because of course the number of errors cannot be larger than the total number of data points, but we will assume that this is never the case.

## Setting up notation
The important information we need to keep track of is the "error budget" that each model has. We can reframe the problem as follow:

Given an error budget for each model encoded as the $(2n+1)-$vector
$B=(E,\dots,E),$
find the maximal size for a collection of vectors $(v_1, \dots, v_k)$ such that
* Each vector $v_i$ contains only $0$ or $1$
* Each vector $v_i$ contains at least $n+1$ entries equal to $1$
* $B-\displaystyle\sum_{i=1}^k v_i$ only has non-negative entries

Each of the $v_i$ represents a datapoint which the ensemble predicts incorrectly, and the $1$-entries correspond to individual models which predicted it incorrectly. We will call them error assignments. 
The last two constraints mean respectively that the majority of individual models must be wrong about a data point in order for the ensemble to be wrong too, and that each model can only be wrong on at most $E$ data points.

## Proof
First of all let us establish something: the best solution has to use the error budget to the best possible efficiency. This means that necessarily, each $v_i$ will have exactly $n+1$ entries equal to $1$.

We will prove the following steps:
1. $E^*_\text{ens}$ is an increasing function of $E$
2. If $E=p(n+1)$, $E^*_\text{ens}=(2n+1)k$ 

Which leads to the framing inequality we claimed above because 
$$(n+1)\left(1+\left\lfloor\frac{E}{n+1}\right\rfloor\right) \geq E\geq (n+1)\left\lfloor\frac{E}{n+1}\right\rfloor $$  

### $E^*_\text{ens}$ is a strictly increasing function of $E$  
This is easy to prove: if a collection of error assignments $(v_1,...,v_k)$ verifies the constraints for an error budget of $E$, it verifies them for $E+1$ as well. 
Furthermore it also verifies them for a budget of $B=(E,\dots,E,E+1,\dots,E+1)$, with $n+1$ entries with value $E$, which is obtained starting from $E+1$ and subtracting $v_0=(1,\dots,1,0,\dots,0)$.

### If $E=p(n+1)$, $E^*_\text{ens}=(2n+1)k$
We will prove this by exhibiting a suitable collection of error assignments.
Let us start by subtracting $v_1=(1,\dots,1,0,\dots,0)$ with $n+1$ nonzero entries.
We then build $v_{i+1}$ from $v_i$ by applying a circular permutation to its entries (*i.e.* $v_2=(0,1,\dots,1,0,\dots,0)$ and so on).

If we subtract the first vector, the budget will look like
$$B_1 = B-v_1 = (E-1,\dots,E-1,E,\dots,E).$$
After one more step, we get
$$B_2 = (E-1, E-2, \dots, E-2, E-1,\dots,E).$$
After $n+1$ total steps, we get this nice valley pattern:
$$B_{n+1} = (E-1,\, E-2,\, E-3,\,\dots,\,E-n,\,E-(n+1),\, E-n,\, \dots,\, E-3,\, E-2,\, E-1),$$
which should be clear because for the first $n$ entries, their position is the number of vectors they get subtracted before the "window of $1$s" leaves them, and the reverse happens for the last $n$ entries. The middle entries is subtracted for every single of these first $n+1$ steps.

Now if we apply one more step, we see that the window applies to the last $n$ entries and the first one. Each one of the last $n$ entries will be covered by the window exactly the number of times needed to reach $E-(n+1), and the same will happen for the first $n$, while the middle entry will be left untouched.

So after $2n+1$ steps, we reach a symmetric situation gain with
$$B_{2n+1}=(E-(n+1),\dots,E-(n+1)),$$

Which means that if $E=p(n+1)$, we can repeat these $2n+1$ steps $p$ times, and thus that we did a total of $p(2n+1)$ steps, which is the number of mistakes our ensemble made.

Why is this the worst-case scenario? After these $p(2n+1)$ steps, the error budget of all models is completely exhausted since 
$$B_{p(2n+1)} = (0,\dots 0).$$

## Putting it all together

For any error budget $E$, we have the framing inequality

$$(n+1)\left(1+\left\lfloor\frac{E}{n+1}\right\rfloor\right) \geq E\geq (n+1)\left\lfloor\frac{E}{n+1}\right\rfloor.$$  

(Which is just the statement that $E$ is framed bt two multiples of $n+1$)

For the two values framing $E$, we have an exact value for $E^*_\text{ens}$, because they are of the form $p(n+1)$ with

$$p=1+\left\lfloor\frac{E}{n+1}\right\rfloor\text{ and } p=\left\lfloor\frac{E}{n+1}\right\rfloor\text{ respectively.}$$

Therefore, the desired framing inequality is true:
$$ (2n+1) \left(1+\left\lfloor\frac{E}{n+1}\right\rfloor\right) \geq E^*_\text{ens} \geq (2n+1) \left\lfloor\frac{E}{n+1}\right\rfloor.$$