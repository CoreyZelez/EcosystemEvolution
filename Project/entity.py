from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass