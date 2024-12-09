# What is Drake?
[Drake](https://drake.mit.edu/) is a C++ library with Python bindings that advertises
itself as
> "a collection of tools for analyzing the dynamics of our robots and building control
> systems for them, with a heavy emphasis on optimization-based design/analysis."


While it aligns well with the [vision for Drake](https://medium.com/toyotaresearch/drake-model-based-design-in-the-age-of-robotics-and-machine-learning-59938c985515),
this quoted summary places unnecessary restrictions on the scope of Drake's
applicability. That is, the  summary **understates** the capabilities of Drake.

To understand why the summary is an understatement, we need to look at the three major
components of Drake (see article linked as "vision for Drake" above).
1. A multibody dynamics engine with state-of-the-art contact modeling
2. A framework for modeling, composing, combining, and simulating general dynamical
   systems
3. An optimization framework for writing and solving mathematical programs


