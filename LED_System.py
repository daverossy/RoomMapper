__author__ = 'David Rossiter'

import Image
import ImageDraw
import BicolorMatrix8x8
import time


# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()


def led(status):
    # Set green forward arrow
    if status == "Forward":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a forwards arrow
        draw.line((7, 4, 0, 4), fill=(0, 255, 0))
        draw.line((7, 3, 0, 3), fill=(0, 255, 0))
        draw.line((3, 0, 0, 3), fill=(0, 255, 0))
        draw.line((3, 7, 0, 4), fill=(0, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    # Set green right arrow
    elif status == "Right":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a right arrow
        draw.line((4, 7, 4, 0), fill=(0, 255, 0))
        draw.line((3, 7, 3, 0), fill=(0, 255, 0))
        draw.line((3, 0, 0, 3), fill=(0, 255, 0))
        draw.line((4, 0, 7, 3), fill=(0, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    # Set green left arrow
    elif status == "Left":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a left arrow
        draw.line((4, 7, 4, 0), fill=(0, 255, 0))
        draw.line((3, 7, 3, 0), fill=(0, 255, 0))
        draw.line((3, 7, 0, 4), fill=(0, 255, 0))
        draw.line((4, 7, 7, 4), fill=(0, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    # Set green reverse arrow
    elif status == "Reverse":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a reverse arrow
        draw.line((7, 4, 0, 4), fill=(0, 255, 0))
        draw.line((7, 3, 0, 3), fill=(0, 255, 0))
        draw.line((4, 7, 7, 4), fill=(0, 255, 0))
        draw.line((4, 0, 7, 4), fill=(0, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    # Set green tick to represent mapping complete
    elif status == "Complete":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a forwards arrow
        draw.line((6, 5, 1, 0), fill=(0, 255, 0))
        draw.line((6, 5, 4, 7), fill=(0, 255, 0))
        draw.line((7, 5, 2, 0), fill=(0, 255, 0))
        draw.line((7, 5, 5, 7), fill=(0, 255, 0))
        draw.line((5, 5, 0, 0), fill=(0, 255, 0))
        draw.line((5, 5, 3, 7), fill=(0, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    # Set orange exclaimation mark
    elif status == "Halt":
        # Clear the display buffer.
        display.clear()

        # First create an 8x8 RGB image.
        image = Image.new('RGB', (8, 8))

        # Then create a draw instance.
        draw = ImageDraw.Draw(image)

        # Draw a forwards arrow
        draw.line((4, 4, 0, 4), fill=(255, 255, 0))
        draw.line((4, 3, 0, 3), fill=(255, 255, 0))
        draw.line((7, 4, 6, 4), fill=(255, 255, 0))
        draw.line((7, 3, 6, 3), fill=(255, 255, 0))

        # Draw the image on the display buffer.
        display.set_image(image)

        # Draw the buffer to the display hardware.
        display.write_display()

    elif status == "Clear":
        # Clear the display buffer.
        display.clear()
        # Write blank buffer to display to clear
        display.write_display()

    else:
        # Print error
        print "LED System status does not exist!"