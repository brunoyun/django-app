# Impact for Gradual semantics

This repository provides the code to implement a django application that can take as input an argumentation graph (in ASPARTIX) format and:

1. Draw the graph 
2. Compute the degrees of the arguments (using a specific semantics)
3. Infer attack intensity for each attack 
4. Calculate the impact of a set of arguments on a particular argument (using a specific semantics)

## Demo

https://django-app-eta.vercel.app/

## Gradual semantics implemented

We implemented the following four semantics:

- H-categoriser semantics
- The cardinality-basec semantics
- The max-based semantics
- The counting semantics

## The impact semantics implemented

We implemented the following two semantics:

- Shapley-based semantics
- Delobelle and Villata's semantics

## Bibliography

