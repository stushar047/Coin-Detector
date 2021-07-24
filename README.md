# Coin Detector, Diameter Estimation and Coin Counting

Coin detection and diameter recognition is a
good way to determine the value of the coin and counting
the coin along with this can help to determine the bill.
Currently, most of the coin detection method follow
Hough circle transformation. In Hough circle
transformation, minimum radius, maximum radius, and
minimum distance between the center point of the circles
are used to suppress redundant circle and find optimum
circle for the coin. Minimum distance parameter will give
inaccurate circle when none of the circles are perfect.
Therefore, when multiple circles are detected for a single
coin in the range of the defined radius, instead one
keeping one and removing others, all the circles’ centers
and radius have been averaged since it is difficult to say
which circle is close to the coin. This method has provided
good results for the coin detection, diameter prediction
and coin counting. Lastly, a graphical user interface has
been developed to tune the minimum radius and
maximum radius parameter.
