
class WorldCell:
    """
    A square shaped region of the game world.
    """
    def __init__(self, width: float, x: float, y: float):
        """
        :param width: Width in world coordinates of square shaped cell.
        :param x: x coordinate of top left position of cell.
        :param y: y coordinate of top left position of cell.
        """
        self.width = width
        self.x = x
        self.y = y
        # consider between storing just entities or differentiating the
        # kind of entities.


class WorldGrid:
    """
    Division of game world into a grid. 
    """

    def __init__(self, x_dim: int, y_dim: int, cell_width: float):
        """
        :param x_dim: Number of cells in x axis.
        :param y_dim: Number of cells in y axis.
        :param cell_size: Width of each game world cell.
        """
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.cell_width = cell_width
        self.cells = [] 
        self.init_cells(cell_width)

    def init_cells(self):
        """
        Initialise the 2d list of grid coordinates.
        """
        for x in range(self.x_dim):
            row = []
            for y in range(self.x_dim):
                x_coord = x * self.cell_width  # x coord of cell.
                y_coord = y * self.cell_width  # y coord of cell.
                row.append(WorldCell(self.cell_width, x_coord,  y_coord))
            self.cells.append(row)

    def get_cell(self, x: float, y: float):
        """
        Gets world cell which contains a specific position. 
        
        :param x: Position's x coordinate.
        :param y: Position's y coordinate.
        :return: World cell containing specified position.
        """
        # Convert position's world coordinates to grid coordinates.
        # When position on border of two cells we tie break by choosing the cell which is
        # to the left or above.
        x = x // self.cell_width  
        y = y // self.cell_width
        if(x == self.x_dim):
            x -= 1
        if(y == self.y_dim):
            y -= 1
        return self.cells[x][y]


            
class GameWorld:
    """
    """

    def __init__(self):
        # self.grid = WorldGrid()
        pass
