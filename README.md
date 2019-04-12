# Analysis of data computed using Feret's diameter

Shape description is a field of image analysis that deals with the quantification of shape properties of an object. A shape property that is quantified by a number is named descriptor. For instance, area, perimeter, diameter are some descriptors.

Feature selection is an important and complex problem in data analysis and machine learning tasks. Having at disposal a large number of features, it is of crucial importance to select those that are the most suitable. Some benefits are reducing the computational time and avoiding overfitting and learning based on irrelevant features. An explanatory example is that it is important for problems of prediction that we use features which are correlated as much as possible with the value we want to predict, but at the same time uncorrelated to each other.

Many shape descriptors are generic, i.e. they are used for somputing other descroiptors using mathematical operations. In such a manner features are transformed to another features. In this manner, a geometrical property represented by a generic feature frequently gets another geometrical meaning and it is very itricate to make clear, complete and general conclusions abouts the relationship of the geometrical properites. 

Many different descriptors are used simultanelusly in shape analysis to provide a set of numbers that determines the shape of an object as best as possible. Naturally arrises an interesting question, how would descriptors (frequenlty having clear geometrical meaning such as area, perimeter, diameter) behave in data analysis and machine learning tasks. One of generic descriptors is Feret's diameter and this is a small study on it.

### Feret's diameter
Feret's diameter of an object is the distance between its two furthest points measured in a given direction. For an illustration, we give the following image:
<p align="center">
  <img src="images/feretDiam.png" width="150">
</p>


When computed for multiple directions, Feret's diameter enables a number of other shape descriptors. For this study we choose the following:
1. *Maximal Feret's diameter* - equal to the classic diameter, i.e. the distance between two futhest points of an object. We compute it as the maximal Feret's diameter over all the directions.
2. *Minimal Feret's diameter* - minimal Feret's diameter over all the directions.
3. *Aspect ratio* - ratio between maximal and minimal Feret's diameter.
4. *Average Feret's diameter* - average Feret's diameter over all the directions.
5. *Feret's diameter perpendicular to the maximal*.
6. *Feret's diameter perpendicular to the minimal*.
7. *Area of the minimal encasing rectangle* - the area of the rectangle with minimal area among all the rectangles that encase the object.
8. *Larger side of the minimal encasing rectangle*.
9. *Shorter side of the minimal encasing rectangle*.
10. *The radius of the ball with equal volume as the cylinder with radius equal to minimal Feret's diameter and height equal to maximal Feret's diameter*.
11. *Perimeter* - computed as the average Feret's diameter over all directions multiplied by $\pi$. This can be applied only if the observed are conves, which is true in our case.
### Input data

Pixel coverage representation is the representation of a shape in which image intensities express to which extent every pixel is covered by the shape. There are different methods for computing pixel coverage representation from real images. We use the algorithm proposed in https://doi.org/10.1016/j.patrec.2011.12.014. The input data base consistsof 368 pixel coverage representations of microscopic images of cell nuclei. The following image illustrates some cell nuclei from the data base and their pixel coverage representations:

<p align="center">
  <img src="images/cell1.png" width="100">
  <img src="images/cell1Cov.png" width="100">
  <img src="images/cell2.png" width="100">
  <img src="images/cell2Cov.png" width="100">
</p>

### Computing Feret's diameter over angles and cells

[](FerDiamCellImArranged/cellMain.m) iterates over angles {0,1,2...,180} degrees and computes Feret's diameter for every cell using the algorithm proposed in https://doi.org/10.1016/j.patrec.2016.04.021. Some cells and the computed Feret's diameter are illustrated by the following figure:

<p align="center">
  <img src="images/cell1Rot.png" width="150">
  <img src="images/feret1.png" width="210">
  <img src="images/cell2Rot.png" width="150">
  <img src="images/feret2.png" width="210">
</p>

[](pythonCode/feretVisualization.m) visualizes the result over all cells and angles: 
<p align="center">
  <img src="images/feretOverAll.png" width="400">
</p>

### Computing other descriptors

Using the obtained matrix of Feret's diameter over all cells and angles [](FerDiamCellImArranged/cellMain.m) computes and visualizes values of the descriptors we listed in the section **Feret's diameter**.

We illustrate some of the descriptors over all the cells in the data base:
<p align="center">
  <img src="images/someDesc.png" width="600">
</p>

### Computing correlation matrix

[](FerDiamCellImArranged/cellMain.m) computes the correlation matrix and displays the heat map for the 11 descriptors:

<p align="center">
  <img src="images/corrMat.png" width="400">
</p>

### Conclusion

A general conclusion is that there is a strong positive correlation between descriptors computed on the data set. Would that be the same if the shapes in the data set are not all convex, such that the perimeter can encrase without increasing the shape size?  

It is interesting to notuice that the perimeter is more strongly correlated to the area of the bounding rectangle than to the maximal diameter. This can be explained by the fact that the increment of the maximal diameter does not neccesarily leads to increment of the perimeter since a shape can be elongated. On this data base both, the bounding rectangle and the perimeter are measures of the size of a shape.

Also, increasing of maximal or minimal ratio both lead to the increment of the shape under considertion. This is not true for the aspect ratio measure.

My general impression is that the computed measures with exceptance of the aspect ratio have strong positive correlation to the size of shapes in the data set. If we wolud observe more diverse objects which change theie convexity, elongation, compactness and other properties, the results would differ. One more impression is that a deep understanding of the features at disposal and the data under consideration is of great importance for selecting the right features and making generalizaions to larger data.  

Any more conclusions :) ?








