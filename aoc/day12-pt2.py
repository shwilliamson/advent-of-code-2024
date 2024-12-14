from dataclasses import dataclass, field
from typing import Tuple, List, Dict, Optional, TypeAlias, Set

Coordinate: TypeAlias = Tuple[int, int]


@dataclass(frozen = True)
class Corner:
    coordinate: Coordinate
    hash_bust: int = 0

    def external_count(self, region: 'Region') -> int:
        external_count = 0
        for c in self.adjacent_plots():
            if c not in region.plots:
                external_count += 1
        return external_count

    def is_internal_diagonal(self, region: 'Region') -> bool:
        plots = self.adjacent_plots()
        internal_diagonal = ((plots[0] in region.plots and plots[2] in region.plots) or
                             (plots[1] in region.plots and plots[3] in region.plots))
        return self.external_count(region) == 2 and internal_diagonal

    def is_external(self, region: 'Region') -> bool:
        # An odd number of adjacent external plots (1 or 3)
        # means this is an external corner of the region.
        return self.external_count(region) % 2 != 0

    def adjacent_plots(self) -> List[Coordinate]:
        (i, j) = self.coordinate
        return [
            (i - 1, j - 1), # NW
            (i - 1, j),     # NE
            (i, j),         # SE
            (i, j - 1)      # SW
        ]


@dataclass
class Plot:
    crop: str
    coordinate: Coordinate
    region: Optional['Region'] = None

    def neighbors(self) -> List[Coordinate]:
        (i, j) = self.coordinate
        return [
            (i, j - 1), # north
            (i + 1, j), # east
            (i, j + 1), # south
            (i - 1, j)  # west
        ]

    def corners(self) -> List[Corner]:
        (i, j) = self.coordinate
        return [
            # Use the plot's coordinate as the NW corner of the plot
            Corner((i, j)),         # NW
            Corner((i, j + 1)),     # NE
            Corner((i + 1, j)),     # SW
            Corner((i + 1, j + 1))  # SE
        ]


@dataclass
class Region:
    crop: str
    garden: 'Garden'
    plots: Dict[Coordinate, Plot] = field(default_factory=dict)

    def corners(self) -> Set[Corner]:
        regional_corners = set[Corner]()
        for plot in self.plots.values():
            for corner in plot.corners():
                if corner.is_external(region=self):
                    regional_corners.add(corner)
                elif corner.is_internal_diagonal(region=self):
                    # These internal corners should be counted twice
                    regional_corners.add(corner)
                    regional_corners.add(Corner(corner.coordinate, hash_bust=1))
        return regional_corners

    def cost(self) -> int:
        return len(self.plots.values()) * len(self.corners())

    def add(self, plot: Plot):
        if plot.crop != self.crop or plot.region:
            return
        plot.region = self
        self.plots[plot.coordinate] = plot
        for n in plot.neighbors():
            neighboring_plot = self.garden.plots.get(n, None)
            if neighboring_plot:
                self.add(neighboring_plot)


@dataclass
class Garden:
    regions: List[Region] = field(default_factory=list)
    plots: Dict[Coordinate, Plot] = field(default_factory=dict)

    def cost(self) -> int:
        return sum([r.cost() for r in self.regions])

    def assign_regions(self):
        for plot in self.plots.values():
            if not plot.region:
                region = Region(plot.crop, garden=self)
                region.add(plot)
                self.regions.append(region)


def main():
    with open('resources/day12.txt', 'r') as file:
        garden = Garden()
        matrix = [line.strip() for line in file]
        for i, row in enumerate(matrix):
            for j, crop in enumerate(row):
                garden.plots[(i,j)] = Plot(crop, (i,j))
        garden.assign_regions()
        print(f"answer is {garden.cost()}")


if __name__ == '__main__':
    main()