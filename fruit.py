"""This file holds everything responsible for representing a fruit."""
import pygame
from resources import fruit_images, slice_frames
from constants import *
import random

class Fruit:
    """
    Class representing the fruit in the Fruit Ninja game.
    """
    def __init__(self, fruit_type: str, x: int, y: int, trajectory: tuple[int, int]):
        """
        Initialize the Fruit object with provided values.

        :param fruit_type: The name of an image file from assets/fruits without the file extension
        :param x: The x-coordinate of the fruit's position
        :param y: The y-coordinate of the fruit's position
        :param trajectory: The x and y velocity of the fruit
        """
        self.type = fruit_type
        
        self.x = x
        self.y = y
        self.trajectory = trajectory

        self.angle = 0
        self.rotate_direction = random.choice(range(-25, 25))

        self.frames = fruit_images[fruit_type]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
        self.sliced = False
        self.last_frame_time = pygame.time.get_ticks()
        self.slice_frames = slice_frames
        self.slice_frame_count = 0

    def move(self):
        """
        This method makes the fruit move.

        This method runs once every frame.
        """
        if not self.sliced:
            # TODO: Add the first element (with index 0) of the trajectory to the fruit's
            #       X-coordinate (self.x) and the second element of the trajectory
            #       to the fruit's Y-coordinate (self.y).
            #       Also, replace the trajectory with an updated one, where the first
            #       element remains unchanged, but GRAVITY gets added to the second one.

            # TODO: Add self.rotate_direction to self.angle to make the fruits spin!

            self.hitbox.topleft = (self.x, self.y)
            if pygame.time.get_ticks() - self.last_frame_time > 50:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]
                self.last_frame_time = pygame.time.get_ticks()
        elif self.slice_frames:
            if pygame.time.get_ticks() - self.last_frame_time > 50:
                if self.slice_frame_count < len(self.slice_frames) - 1:
                    self.slice_frame_count += 1
                    self.image = self.slice_frames[self.slice_frame_count]
                    self.last_frame_time = pygame.time.get_ticks()
                else:
                    return False  # Mark for removal
        return True

    def draw(self, surface):
        """
        This method draws the fruit on the screen.
        :param surface: to draw the fruit on
        """
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(topleft = (self.x, self.y)).center)

        surface.blit(rotated_image, new_rect)

    def slice(self):
        self.angle = 0
        self.sliced = True
        self.image = self.slice_frames[0]
        self.slice_frame_count = 0
        self.last_frame_time = pygame.time.get_ticks()
