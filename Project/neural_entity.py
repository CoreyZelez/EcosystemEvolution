from abc import ABC, abstractmethod
from entity import Entity
import torch
import torch.nn as nn
        
class NeuralEntity(ABC, Entity):
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

    def __init__(self, decision_maker: NeuralDecisionMaker):
        self.decision_maker = decision_maker