import PIL
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def get_class(image_path, model_path, labels_paths):
    # Disabling scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Loading the model
    model = load_model(mode, compile=False)
    # Loading the labels
    class_names = open("labels.txt", "r").readlines()
    # Creating the array of the right shape to feed into the keras model
    # The 'length', or number of images you can put into the array is
    # determined by the first position in the shape tuple (in this case, 1)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(image_path).convert("RGB")
    # Resizing the image to be at least 224x224px and then cropping it from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    # Turning the image into a NumPy array
    image_array = np.asarray(image)
    # Normalizing the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # Loading the image into the array
    data[0] = normalized_image_array
    # Predicting the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    # Print prediction and confidence score
    return (class_name[2:], confidence_score)