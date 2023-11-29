# ExplorationActivity2
## Question 1: What library
For the second exploration activity, I chose a library called Pillow, a fork of the Python Imaging Library (PIL). Pillow is the front-runner for digital image processing in the Python programming language and was created by Jeffrey A. Clark.
## Question 2: How to run
The first step in running Pillow is to ensure that either Pillow is already downloaded or to install it. To check if Pillow is indeed downloaded on your machine (as is the case with the ITC lab computers), you can run a simple command: _pip show pillow_. In the case that you need to install it, run the command: _pip install pillow_ and you will be good to go. Once installed it is like any other Python program that you would run through the terminal.
## Question 3: Purpose
"As mentioned above, Pillow is a fork of PIL, but PIL has not been updated since 2011 and is discontinued. That is where Pillow comes in—it provides robust image processing, and its tools are used for all facets of imaging. My program demonstrates the key functions of the library. I took two images of Porsches and began testing the functions of the library. As there is a part of the Library Overview that requires me to go in-depth with parts of the code, I will explain some functions and delve deeper into them in the overview.

Every part of my code has functions with try-catch blocks to ensure that any errors with the images are contained. Firstly, and most commonly used, is the function _Image.open()_, which is utilized to open any of the file formats that Pillow supports—BMP, PNG, JPEG, and TIFF. I then began testing the ability of the image manipulation provided by Pillow, which gives you the ability to resize, rotate, flip, and even merge the images that have been previously opened. All of these functions are valuable in image editing and other aspects of preprocessing.

Another function that I demonstrate in my program is the ability to write/draw on the image. This is very useful when it comes to relaying information with the use of images and annotations. Some other functions of the library include the saving function, where all images we have previously improved and edited can be saved as any of the supported file types and can be saved to our personal folder, where we can then implement them in our work.

To finalize the purpose of this, I combined most of the functions I created into a JPEG that prompts the viewer to choose a Porsche model using resize, open, merge, and writing functions. Additionally, there is a built-in function that runs like _ImageName.show()_ and pops up a PNG of the image
## Insert Image here
## Question 4: Sample Input/Output
My program mostly works with output and a lot less with input, I believe that makes sense as the library is an image based thing. In terms of possibilty for some input it would be plausible to ask the user for the name of the jpeg they want opened or the colour of font they want to be written on the image. But as it is my task to display the library in an informative way I did not believe this way to be the best as well as being fairly unnecessary. Some sample output on the other hand, I already provided the final product and output of combining a lot of the functionality but I will also show the car flipped as well as it being merged with no text.
## Add car pics

