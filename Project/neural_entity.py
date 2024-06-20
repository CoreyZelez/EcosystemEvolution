from abc import ABC, abstractmethod
from entity import Entity
import torch
import torch.nn as nn


class NeuralDecisionMaker(ABC):
    def __init__(self, neural_network: nn.Module):
        self.neural_network = neural_network

    @abstractmethod
    def decide_action(self, input: torch.tensor):
        """
        Uses neural network to decide on an action for a NeuralEntity object.

        :param input: The input the neural network generates a prediction from.
        :return: The decision made on what action to take.
        """
        pass

class EntityScorer(ABC):
    """
    Handles the scoring of a game entity.
    """
    def __init__(self):
        self.score = 0

    @abstractmethod
    def update(self, entity):
        """
        Updates
        """
        pass

        
class NeuralEntity(ABC, Entity):
    def __init__(self, decision_maker: NeuralDecisionMaker):
        """
        :param decision_maker: Responsible for determining actions entity makes.
        """
        self.decision_maker = decision_maker
        self.score = 0

    def adjust_score(self, delta: float):
        """
        :param delta: Change applied to score.
        """
        self.score += delta
