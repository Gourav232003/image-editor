import argparse
from utils import load_image, save_image, show_image
from image_operations import invert, grayscale, adjust_brightness, flip, resize_image
from filters import apply_blur, apply_edge_detection

def main():
    parser = argparse.ArgumentParser(description="Image Processing Tool using NumPy")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to save processed image")
    parser.add_argument("--invert", action="store_true", help="Invert colors")
    parser.add_argument("--grayscale", action="store_true", help="Convert to grayscale")
    parser.add_argument("--brightness", type=int, help="Adjust brightness (+/-)")
    parser.add_argument("--flip", choices=["horizontal", "vertical"], help="Flip the image")
    parser.add_argument("--blur", action="store_true", help="Apply blur filter")
    parser.add_argument("--edges", action="store_true", help="Apply edge detection")
    parser.add_argument("--resize", type=int, help="Resize image (scale percent: 1–100)")


    args = parser.parse_args()

    image = load_image(args.input)
    print("Loading:", args.input)


    if args.invert:
        image = invert(image)
    if args.grayscale:
        image = grayscale(image)
    if args.brightness is not None:
        image = adjust_brightness(image, args.brightness)
    if args.flip:
        image = flip(image, direction=args.flip)
    if args.blur:
        image = apply_blur(image)
    if args.edges:
        image = apply_edge_detection(image)
    if args.resize is not None:
        image = resize_image(image, args.resize)


    save_image(args.output, image)
    show_image(image)

if __name__ == "__main__":
    main()
