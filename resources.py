"""This file holds all images and sounds for the Fruit Ninja game."""
from constants import *
import pygame
import os
from PIL import Image


# Load sound effects
# Here's an example how sounds can be loaded using PyGame.
flute_sound = pygame.mixer.Sound("assets/sounds/flute.wav")

# But our game needs more sounds! Load your sounds here.
# We have provided sound effects for the gameplay ambience (ambience.wav),
# fruits and bombs being thrown (throw.wav and bomb_throw.wav),
# bomb explosion (kaboom.wav), missing a fruit (miss.wav),
# slicing a fruit (slice.wav), and the main game soundtrack (soundtrack.wav).
# You can also use your own sounds, any MP3 or WAV file should work fine!

big_font = pygame.font.Font('assets/fonts/gamecamper.ttf', 36)
font = pygame.font.Font('assets/fonts/gamecamper-lite.ttf', 24)

# Load fruit images
def load_fruit_images(directory):
    fruit_images = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if filename.endswith(".gif"):
            fruit_name = os.path.splitext(filename)[0]  # Get the name without extension
            fruit_images[fruit_name] = load_gif_frames(file_path)  # Load as GIF
        elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
            fruit_name = os.path.splitext(filename)[0]  # Get the name without extension
            image = pygame.image.load(file_path).convert_alpha()  # Load static image
            # Resize the image to be at most 120x120 while keeping the aspect ratio
            fruit_images[fruit_name] = [resize_image(image)]  # Store resized image
    return fruit_images

# Load fruit images as frame sequences for GIFs
def load_gif_frames(path):
    pil_img = Image.open(path)
    frames = []
    try:
        while True:
            frame = pil_img.convert("RGBA")
            frames.append(pygame.image.fromstring(frame.tobytes(), frame.size, "RGBA"))
            pil_img.seek(len(frames))
    except EOFError:
        pass
    return frames

# Load background images dynamically
def load_background_images(directory):
    backgrounds = {}
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            background_name = os.path.splitext(filename)[0]  # Get the name without extension
            image = pygame.image.load(os.path.join(directory, filename))
            image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            backgrounds[background_name] = image
    return backgrounds

# Resize an image to be at most 120x120, keeping the aspect ratio
def resize_image(image, max_size=120):
    width, height = image.get_size()
    
    # Calculate the scaling factor
    if width > height:
        new_width = min(width, max_size)
        new_height = int((new_width / width) * height)
    else:
        new_height = min(height, max_size)
        new_width = int((new_height / height) * width)

    # Perform the resizing
    return pygame.transform.scale(image, (new_width, new_height))

# Load fruit and slice images
fruit_images = load_fruit_images("assets/fruits")
slice_frames = load_gif_frames("assets/effects/slice.gif")

# Load background images
backgrounds = load_background_images("assets/backgrounds")
