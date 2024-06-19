


class Generation:
    """
    A generation of a populace of some species.
    """
    def __init__(self, species_id: int, individuals: list, scores: list, seed: int):
        """
        :param individuals: The individuals in the generation.
        :param scores: The scores of the individuals.
        :param seed: The random seed used when the individuals were scored.
        """
        self.species_id = species_id
        self.individuals = individuals
        self.scores = scores
        self.seed = seed

class GeneticOptimiser:
    """
    A class for tracking and performing genetic optimisations of species.
    """
    def __init__(self, elitism: float, diversification: float, num_parents: int, 
                 minimal_parent_weight: float, maximal_random_mutation: float, ):
        """
        :param elitism: Percent of top performers to influence next generation.
        :param diversification: Percent of population randomly chosen to influence next generation.
        :param num_parents: Number of parents producing a single offspring.
        :param minimal_parent_weight: Minimal percentage each parent contributes to child attributes.
        :param maximal_random_mutation: Maximal percentage random mutation of childs traits following 
            combination of parental traits. 
        """
        assert(minimal_parent_weight <= 1 / num_parents)

        self.elitism = elitism
        self.diversification = diversification
        self.num_parents = num_parents
        self.minimal_parent_weight = minimal_parent_weight
        self.maximal_random_mutation = maximal_random_mutation

        self.generations = dict()  # Maps species id to list of generations.

    def perform_optimisation_step(self, generation: Generation):
        """
        Performs genetic optimisation on a generation of some species.

        :param generation: The generation the optimisation step is performed for.
        :return: The individuals in the next generation.
        """
        # Add diversification * N random individuals to the parents list.
        # Add the top elitism * N individuals to the parents list.
        # Shuffle the list so no priority is given.
        # Loop through each parent in the list.
        # Pick num_parents - 1 other parents at random (excluding current loop parent) to breed 
        # a single individual.
        # after this process there will be K entities in the next generation.
        # Repeat the above process terminating as soon as the number of entities in the next
        # generation equals the number in the previous generation.


