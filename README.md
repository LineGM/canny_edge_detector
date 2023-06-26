# canny_edge_detector
This is my university project to implement Canny edge detector, which uses a multi-stage algorithm to detect a wide range of edges in images.
The process of Canny edge detection algorithm can be broken down to five different steps:
  1. Apply Gaussian filter to smooth the image in order to remove the noise
  2. Find the intensity gradients of the image
  3. Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
  4. Apply double threshold to determine potential edges
  5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.
