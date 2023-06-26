# Canny edge detector
This is my university project to implement Canny edge detector, which uses a multi-stage algorithm to detect a wide range of edges in images.

[Information from the wiki: https://en.wikipedia.org/wiki/Canny_edge_detector]

The process of Canny edge detection algorithm can be broken down to five different steps:
  1. Apply Gaussian filter to smooth the image in order to remove the noise
  2. Find the intensity gradients of the image
  3. Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
  4. Apply double threshold to determine potential edges
  5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

# Gaussian filter
Since all edge detection results are easily affected by the noise in the image, it is essential to filter out the noise to prevent false detection caused by it. To smooth the image, a Gaussian filter kernel is convolved with the image. This step will slightly smooth the image to reduce the effects of obvious noise on the edge detector. The equation for a Gaussian filter kernel of size (2k+1)×(2k+1) is given by:

![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/29a306ba-e1a2-4d54-9047-bbcc1494750b)


![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/24a21915-7e47-4418-adaf-3c296da00278)

Here is an example of a 5×5 Gaussian filter, used to create the adjacent image, with sigma  = 1. (The asterisk denotes a convolution operation.)

![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/63d47556-5124-41dc-bb69-57e8f12b7457)

# Finding the intensity gradient of the image
An edge in an image may point in a variety of directions, so the Canny algorithm uses four filters to detect horizontal, vertical and diagonal edges in the blurred image. The edge detection operator (such as Roberts, Prewitt, or Sobel) returns a value for the first derivative in the horizontal direction (Gx) and the vertical direction (Gy). From this the edge gradient and direction can be determined:

![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/9cb980df-36c5-4ec8-bfab-90f6ca0c843f)

![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/0419bd74-0499-401b-b021-5c28e8caed74)

# Gradient magnitude thresholding or lower bound cut-off suppression
Minimum cut-off suppression of gradient magnitudes, or lower bound thresholding, is an edge thinning technique. Lower bound cut-off suppression is applied to find the locations with the sharpest change of intensity value. The algorithm for each pixel in the gradient image is:
  1. Compare the edge strength of the current pixel with the edge strength of the pixel in the positive and negative gradient directions.
  2. If the edge strength of the current pixel is the largest compared to the other pixels in the mask with the same direction (e.g., a pixel that is pointing in the y-direction will be compared to the pixel above and          below it in the vertical axis), the value will be preserved. Otherwise, the value will be suppressed.
In some implementations, the algorithm categorizes the continuous gradient directions into a small set of discrete directions, and then moves a 3x3 filter over the output of the previous step (that is, the edge strength and gradient directions). At every pixel, it suppresses the edge strength of the center pixel (by setting its value to 0) if its magnitude is not greater than the magnitude of the two neighbors in the gradient direction. For example,
  if the rounded gradient angle is 0° (i.e. the edge is in the north–south direction) the point will be considered to be on the edge if its gradient magnitude is greater than the magnitudes at pixels in the east and west    directions,
  if the rounded gradient angle is 90° (i.e. the edge is in the east–west direction) the point will be considered to be on the edge if its gradient magnitude is greater than the magnitudes at pixels in the north and south   directions,
  if the rounded gradient angle is 135° (i.e. the edge is in the northeast–southwest direction) the point will be considered to be on the edge if its gradient magnitude is greater than the magnitudes at pixels in the        north-west and south-east directions,
  if the rounded gradient angle is 45° (i.e. the edge is in the northwest–southeast direction) the point will be considered to be on the edge if its gradient magnitude is greater than the magnitudes at pixels in the         north-east and south-west directions.
In more accurate implementations, linear interpolation is used between the two neighbouring pixels that straddle the gradient direction. For example, if the gradient angle is between 89° and 180°, interpolation between gradients at the north and north-east pixels will give one interpolated value, and interpolation between the south and south-west pixels will give the other (using the conventions of the last paragraph). The gradient magnitude at the central pixel must be greater than both of these for it to be marked as an edge.
Note that the sign of the direction is irrelevant, i.e. north–south is the same as south–north and so on.

# Double threshold
After application of non-maximum suppression, remaining edge pixels provide a more accurate representation of real edges in an image. However, some edge pixels remain that are caused by noise and color variation. To account for these spurious responses, it is essential to filter out edge pixels with a weak gradient value and preserve edge pixels with a high gradient value. This is accomplished by selecting high and low threshold values. If an edge pixel’s gradient value is higher than the high threshold value, it is marked as a strong edge pixel. If an edge pixel’s gradient value is smaller than the high threshold value and larger than the low threshold value, it is marked as a weak edge pixel. If an edge pixel's gradient value is smaller than the low threshold value, it will be suppressed. The two threshold values are empirically determined and their definition will depend on the content of a given input image.

# Edge tracking by hysteresis
The strong edge pixels should certainly be involved in the final edge image; they are deemed to come from true edges in the image. However, there will be some debate on the weak edge pixels. We want to determine whether these pixels come from a true edge, or noise/color variations. Weak edge pixels should be dropped from consideration if it is the latter. This algorithm uses the idea that weak edge pixels from true edges will (usually) be connected to a strong edge pixel while noise responses are unconnected. To track the edge connection, blob analysis is applied by looking at a weak edge pixel and its 8-connected neighborhood pixels. As long as there is one strong edge pixel that is involved in the blob, that weak edge point can be identified as one that should be preserved. These weak edge pixels become strong edges that can then cause their neighboring weak edge pixels to be preserved.

![image](https://github.com/LineGM/canny_edge_detector/assets/28562738/2384597c-fbb4-4258-bef8-450070a6c246)

