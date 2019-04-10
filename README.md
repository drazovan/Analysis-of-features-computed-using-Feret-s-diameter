# Analysis of descriptors computed using Feret's diameter

In this study we... 
What are descriptors. What is shape analysis. 
Shape image\\



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
11. *Perimeter* - computed as the average Feret's diameter over all directions multiplied by $\pi$.

### Input data

Pixel coverage representation is the representation of a shape in which image intensities express to which extent every pixel is covered by the shape. There are different methods for computing pixel coverage representation from real images. We use the algorithm proposed in https://doi.org/10.1016/j.patrec.2011.12.014. The input data base consistsof 368 pixel coverage representations of microscopic images of cell nuclei. The following image illustrates some cell nuclei from the data base and their pixel coverage representations:

<p align="center">
  <img src="images/cell1.png" width="100">
  <img src="images/cell1Cov.png" width="100">
  <img src="images/cell2.png" width="100">
  <img src="images/cell2Cov.png" width="100">
</p>

### Computing Feret's diameter over angles and cells

[](FerDiamCellImArranged/cellMain.m) iterates over angles {0,1,2...,180} degrees and computes Feret's diameter for every cell. Some cells and the computed Feret's diameter are illustrated by the following figure:

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









