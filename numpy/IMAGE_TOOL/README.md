# Image Processing Tool

A command-line image processing tool built with Python and NumPy that provides various image manipulation and filtering capabilities.

## Features

The tool supports the following image operations:

- **Color Inversion**: Invert image colors
- **Grayscale Conversion**: Convert color images to grayscale
- **Brightness Adjustment**: Increase or decrease image brightness
- **Image Flipping**: Flip images horizontally or vertically
- **Blur Filter**: Apply a blur effect to images
- **Edge Detection**: Detect edges using Sobel operators
- **Image Resizing**: Resize images by percentage (1-100%)

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install numpy pillow matplotlib scipy
```

### Dependencies
- `numpy` - For array operations and image manipulation
- `pillow` (PIL) - For image loading and saving
- `matplotlib` - For image display
- `scipy` - For convolution operations in filters

## Usage

Basic syntax:
```bash
python main.py <input_image> <output_image> [options]
```

### Command Line Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `input` | Required | Path to the input image file |
| `output` | Required | Path where the processed image will be saved |
| `--invert` | Flag | Invert the colors of the image |
| `--grayscale` | Flag | Convert the image to grayscale |
| `--brightness` | Integer | Adjust brightness (+/- value) |
| `--flip` | Choice | Flip image (`horizontal` or `vertical`) |
| `--blur` | Flag | Apply blur filter |
| `--edges` | Flag | Apply edge detection |
| `--resize` | Integer | Resize image (scale percent: 1-100) |

### Examples

1. **Convert to grayscale:**
   ```bash
   python main.py input.jpg output.jpg --grayscale
   ```

2. **Invert colors and apply blur:**
   ```bash
   python main.py input.jpg output.jpg --invert --blur
   ```

3. **Adjust brightness and flip horizontally:**
   ```bash
   python main.py input.jpg output.jpg --brightness 30 --flip horizontal
   ```

4. **Apply edge detection:**
   ```bash
   python main.py input.jpg output.jpg --edges
   ```

5. **Resize image to 50% of original size:**
   ```bash
   python main.py input.jpg output.jpg --resize 50
   ```

6. **Combine multiple operations:**
   ```bash
   python main.py input.jpg output.jpg --grayscale --brightness -20 --blur --flip vertical
   ```

## File Structure

```
IMAGE_TOOL/
├── main.py              # Main application entry point
├── utils.py             # Utility functions for loading, saving, and displaying images
├── image_operations.py  # Core image processing operations
├── filters.py           # Image filtering operations
├── test_images/         # Sample images for testing
│   ├── sample.jpg
│   └── sample2.png
└── README.md           # This file
```

## Modules

### `utils.py`
Contains utility functions:
- `load_image(path)` - Load image from file path
- `save_image(path, array)` - Save numpy array as image
- `show_image(array)` - Display image using matplotlib

### `image_operations.py`
Core image processing functions:
- `invert(image)` - Invert image colors
- `grayscale(image)` - Convert to grayscale
- `adjust_brightness(image, value)` - Adjust brightness
- `flip(image, direction)` - Flip image horizontally or vertically
- `resize_image(image, scale_percent)` - Resize image by percentage

### `filters.py`
Advanced filtering operations:
- `apply_blur(image)` - Apply 3x3 blur kernel
- `apply_edge_detection(image)` - Sobel edge detection

## Supported Image Formats

The tool supports all image formats supported by PIL/Pillow, including:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- GIF (.gif)

## Notes

- Operations are applied in the order they appear in the command line
- The tool automatically displays the processed image after saving
- Brightness values can be positive (brighter) or negative (darker)
- Edge detection automatically converts the image to grayscale
- Resize operation uses LANCZOS resampling for better quality

## Sample Images

The `test_images/` directory contains sample images (`sample.jpg` and `sample2.png`) that you can use to test the tool's functionality.

## Error Handling

- Invalid file paths will raise appropriate errors
- Resize scale must be between 1-100%
- Brightness values are automatically clipped to valid range (0-255)

## License

This project is open source and available under the MIT License.
