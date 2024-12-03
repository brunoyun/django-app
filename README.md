# Impact for Gradual semantics

This repository provides the code to implement a django application that can take as input an argumentation graph (in ASPARTIX) format and:

1. Draw the graph 
2. Compute the degrees of the arguments (using a specific semantics, see below)
3. Infer attack intensity for each attack (using an extension of the Shapley measure, see [Amgoud et al. 2017](https://www.ijcai.org/Proceedings/2017/10))
4. Calculate the impact of a set of arguments on a particular argument (w.r.t. a specific semantics)

## The ASPARTIX format

The ASPARTIX format is used to define Dung argumentation graphs.

```
arg(a).   ... a is an argument
arg(a).   ... b is an argument
att(a,b). ... a attacks b
```
The code above creates a simple graph with two arguments ($a$ and $b$) with one attack from $a$ to $b$.

For a full description, we refer to the corresponding [TU WIEN webpage](https://www.dbai.tuwien.ac.at/proj/argumentation/systempage/dung.html).

## Demo

A demo of the application is deployed on [Vercel](https://impact-gradual-semantics.vercel.app/).

![image of the interface](https://bruno-yun.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F57e14b1b-ce77-483b-a9ed-537a76c86282%2F594f0392-5dbc-4463-bd53-419656ec7ed3%2FCapture_decran_2023-10-12_a_13.07.14.png?table=block&id=45d27bc7-5e0b-44a8-aa9c-716f5fb22af0&spaceId=57e14b1b-ce77-483b-a9ed-537a76c86282&width=1420&userId=&cache=v2)


## Gradual semantics implemented

We implemented the following four semantics:

- H-categoriser semantics.
- The cardinality-based semantics
- The max-based semantics
- The counting semantics

We refer to the corresponding papers by [[Amgoud et al. 2017](Acceptability Semantics for Weighted Argumentation Frameworks)](https://www.ijcai.org/proceedings/2017/0009.pdf), [[Amgoud et al. 2022](Evaluation of argument
strength in attack graphs: Foundations and semantics)](https://www.sciencedirect.com/science/article/abs/pii/S0004370221001582), and [[Borg and Floris 2021]( A basic framework for explanations in argumentation)](https://ieeexplore.ieee.org/document/9329042).

## The impact semantics implemented

We implemented the following two semantics:

- Shapley-based semantics
- Delobelle and Villata's semantics
