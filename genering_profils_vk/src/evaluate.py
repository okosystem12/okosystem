from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image

import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

def detect_photo(model, image_path):
    image = read_image_bgr(image_path)
    image = preprocess_image(image)
    image, scale = resize_image(image)
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    boxes /= scale

    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # scores are sorted so we can break
        if score < 0.4:
            return False
        else:
            plt.figure(figsize=(15, 15))
            plt.axis('off')
            return True

