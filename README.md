This application can download images from the mailbox and read it which can be useful if the user is blind. It just takes the command from the user recognizes it and then downloads 
the image sent to user from the mail. 

The API used for OCR(Optical Character Reader) is Google Vision API. This is a powerful API which is trained on billions of characters in multiple languages and can detect texts inside
the images. 

In order to use this application you need to create an account in Google Vision through Google Cloud Platform. After creating the account, an API key(json file) needs to be generated which will
be used inside the code to initialize the API from local. Place the api key into the resources folder.

To use this application, create a new project in Pycharm. Initialize git in that project. Pull the files from the repo. Install the requirements. 
There are few PyAudio wheel files in the resources folder for windows 64bit and python 3.7/3.8
If your specs match with the above one then you can directly install PyAudio using pip install 'PyAudioWheelName' otherwise you can download the appropriate wheel file for your
specs from  www.lfd.uci.edu/~gohlke/pythonlibs .

Put the api key(json file) into resources folder.

Put all your credentials into the credentials file.

Run main.py file.

Once it runs, it will prompt the user to speak.. 

If user say download image in english, then it downloades the image from most recent mail and reads in English.
If user say download image in hindi, then it downloades the images and reads in hindi.
