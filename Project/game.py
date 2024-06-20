from entity_manager import EntityManager
import pygame

class Game:
    """
    
    """

    def __init__(self):
        self.entity_manager = EntityManager()

    def draw(self, screen: pygame.Surface):
        self.entity_manager.draw(surface)