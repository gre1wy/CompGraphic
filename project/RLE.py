import numpy as np


def rle_compress(img):

    compressed_data = []

    # Make 1d array from image
    flattened_channel = img.flatten()

    # Save width of image to decompress
    width = img.shape[1]
    compressed_data.append(width)

    # Get a pointer on first pixel
    current_pixel = flattened_channel[0]
    run_length = 1

    # Run through image channel
    for pixel in flattened_channel[1:]:
        if pixel == current_pixel:
            run_length += 1
        else:
            compressed_data.extend([current_pixel, run_length])
            # Change a pointer
            current_pixel = pixel
            run_length = 1

    compressed_data.extend([current_pixel, run_length]) 

    return np.array(compressed_data)

def rle_decompress(compressed_data):
    # Extract width of the image
    width = compressed_data[0]

    # Initialize an empty list to store decompressed pixels
    decompressed_channel = []

    # Iterate through the compressed data starting from index 1
    i = 1
    while i < len(compressed_data):
        pixel = compressed_data[i]
        run_length = compressed_data[i + 1]

        # Repeat the pixel run_length times
        decompressed_channel.extend([pixel] * run_length)

        # Move the index to the next pixel
        i += 2

    # Reshape the decompressed 1D array to the original image shape
    decompressed_img = np.array(decompressed_channel).reshape(-1, width)

    return np.array(decompressed_img)

def rle_compress_rgb(img):
    compressed_data_rgb = []
    for i in range(3):
        data = rle_compress(img[:, :, i])
        compressed_data_rgb.append(data)
    return compressed_data_rgb

def rle_decompress_rgb(img):
    data_red = rle_decompress(img[0])
    data_green = rle_decompress(img[1])
    data_blue = rle_decompress(img[2])
    decompressed_data_rgb = np.dstack((data_red, data_green, data_blue))
    return decompressed_data_rgb


