# VisionGray - RGB to Grayscale Conversion

## Student Name
**Mihir Panchal**

## Index
1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Technologies Used](#technologies-used)
4. [Project Workflow](#project-workflow)
5. [Testing and Results](#testing-and-results)
6. [Conclusion](#conclusion)
7. [Future Enhancements](#future-enhancements)

---

## Introduction
This project is a Flask-based web application that allows users to upload an image, convert it to a grayscale image, and download the processed image without manual intervention. The application utilizes OpenCV for image processing and Flask for backend functionality.

## Objective
The primary objectives of this project are:
- To create a simple web interface for image processing.
- To convert RGB images to grayscale using OpenCV.
- To provide a download option by directly saving the output to a local folder.

## Technologies Used
| Technology  | Purpose |
|------------|---------|
| Python (Flask) | Backend server & handling image processing |
| HTML/CSS | Frontend user interface |
| OpenCV | Image processing (RGB to grayscale conversion) |

## Project Workflow
1. The user visits the webpage.
2. The user uploads an image via an HTML form.
3. The image is converted to grayscale using OpenCV.
4. The original and grayscale images are saved in a local folder directly.

## Testing and Results
### Test Cases
| Test Scenario | Expected Output |
|--------------|----------------|
| Upload an RGB image | Upload file name is displayed |
| Upload a non-image file | Shows error (handled by browser) |
| Convert image | Image is saved to grayscale folder |

### Result
The application successfully converts images to grayscale and saves them to a desired folder.

## Conclusion
This project demonstrates the integration of Flask and OpenCV for web-based image processing. The use of saving images directly to a local folder makes the user interface more convenient.

## Future Enhancements
- Apply filters like Sepia, Blur, and Edge Detection.
- Allow batch processing for multiple images.
- Improve UI/UX with JavaScript-based real-time previews.

