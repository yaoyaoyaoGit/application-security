import numpy as np
from PIL import Image

def squarify_image(img):
    if img.shape[0] == img.shape[1]:
        return img
    max_side = max(img.shape[0], img.shape[1])
    # Assume image is RGB and pad with white
    squared_img = np.ones((max_side, max_side, 3), dtype=np.uint8) * 255
    padding = abs((img.shape[0] - img.shape[1]) // 2)
    if img.shape[0] > img.shape[1]:
        squared_img[:, padding:img.shape[0] - padding] = img
    else:
        squared_img[padding:img.shape[1] - padding, :] = img
    return squared_img

if __name__ == "__main__":
    fn = "sample.jpeg"
    img = np.asarray(Image.open(fn))
    squared_img = squarify_image(img)
    squared_img = Image.fromarray(squared_img, 'RGB')
    squared_img.save("squared_%s" % fn)