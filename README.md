# Impact for Gradual semantics

This repository provides the code to implement a django application that can take as input an argumentation graph (in ASPARTIX) format and:

1. Draw the graph 
2. Compute the degrees of the arguments (using a specific semantics)
3. Infer attack intensity for each attack 
4. Calculate the impact of a set of arguments on a particular argument (using a specific semantics)

## Demo

A demo of the application is deployed on [Vercel](https://impact-gradual-semantics.vercel.app/).

![image of the interface](https://bruno-yun.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F57e14b1b-ce77-483b-a9ed-537a76c86282%2F594f0392-5dbc-4463-bd53-419656ec7ed3%2FCapture_decran_2023-10-12_a_13.07.14.png?table=block&id=45d27bc7-5e0b-44a8-aa9c-716f5fb22af0&spaceId=57e14b1b-ce77-483b-a9ed-537a76c86282&width=1420&userId=&cache=v2)


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

