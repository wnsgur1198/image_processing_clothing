# -*- coding: UTF-8 -*-
# main.py : Fashion MNIST Clothing Classification - make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from matplotlib import pyplot
import PIL.ImageOps
from color_recog import ColorRecog


# Image Path
IMAGE_PATH = 'images/0.jpg'
# class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
           # 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
class_names = ['티셔츠', '바지', '긴팔티', '드레스', '코트',
           '샌들', '셔츠', '스니커즈', '가방', '구두']
                   
class Analyze:
    def __init__(self):
        #print('analyze')
        pass

    # load and prepare the image
    def load_image(self, filename):
        # load the image
        img = load_img(filename, grayscale=True, target_size=(28, 28))
        
        # invert img
        img2 = PIL.ImageOps.invert(img)

        # convert to array
        img2 = img_to_array(img2)

        # reshape into a single sample with 1 channel
        img2 = img2.reshape(1, 28, 28, 1)

        # prepare pixel data
        img2 = img2.astype('float32')
        img2 = img2 / 255.0

        return img, img2

    # load an image and predict the class
    def run_example(self):
    
        anl = Analyze()
        # load the image
        img, img2 = anl.load_image(IMAGE_PATH)

        # load model
        model = load_model('models/final_model.h5')

        # predict the class
        result = model.predict_classes(img2)
        # print(class_names[result[0]])
        
        # show img
        #pyplot.imshow(img)
        #pyplot.show()
        
        return class_names[result[0]]

    def analyze(self):
    
        anl = Analyze()
        # entry point, run the example
        clothing = anl.run_example()

        clrRecog = ColorRecog()
        # classify color
        color = clrRecog.image_color_cluster(IMAGE_PATH)
        
        print(color+' '+clothing)
        
        #return clothing+','+color
        return color+' '+clothing
