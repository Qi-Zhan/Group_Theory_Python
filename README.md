# Group_Theory_Python
This project provides simple *finite* group instances such as cyclic group, symmetric group and corresponding operation in Python. 

This project may be useful in teaching and learning group theory.

## Usage
see `examples` folder for some basic usage

## Feature
* support general group representation and some built-in groups
* support construction group by quotient and product
* support homomorphism, group action ... TODO

## Core 
`group.py`
This file provides abstract group, consists of element defined in `group_element.py` and operation
defined in `binaryop.py`.

`group_element.py`
This file provides some concrete group elements, e.g. Integer, Permutation.

`binaryop.py`
This file provides some concrete operations, e.g. Modulo, Permute.

You can define any group, element, operation you want.

`homomorphism.py` 
This file provides abstract homomorphism and corresponding property such as kernel, image ...  

