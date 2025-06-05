Metal Surface Defect Detection

1. Edge Detection & Dilation: Applied edge detection followed by dilation to highlight defect boundaries, assuming defects have distinct edges with sufficient contrast.
2. Adaptive Thresholding: Utilized adaptive thresholding to create a binary image, enhancing defect detection by adapting to local intensity variations.
3. Morphological Operations: Employed morphological transformations (e.g., closing) to refine defect shapes and minimize noise, ensuring accurate contour detection.
4. Contour Detection & Filtering: Identified contours with areas >50 pixels using OpenCV, computing their centers, bounding boxes, and sizes, filtering out small noise artifacts, and counting total defects.
5. DBSCAN Clustering: Grouped defect centers using DBSCAN (eps=50, min_samples=1) to cluster nearby defects, 
   drawing black bounding boxes around clusters, counting clusters, and reporting defect and 
   cluster areas in pixels, with output saved as 'output_clustered_boxes.jpg'.

