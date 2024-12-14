from dataclasses import dataclass, field
from typing import Tuple, Set, List, Dict


@dataclass
class Plot:
    crop: str
    coordinate: Tuple[int, int]
    external_perimeter: int
    assigned_region: bool = False

    @staticmethod
    def neighbors(i: int, j: int) -> List[Tuple[int, int]]:
        return [
            (i, j - 1), # north
            (i + 1, j), # east
            (i, j + 1), # south
            (i - 1, j)  # west
        ]


@dataclass
class Region:
    crop: str
    plots: List[Plot] = field(default_factory=list)

    def perimeter(self) -> int:
        return sum([p.external_perimeter for p in self.plots])

    def cost(self) -> int:
        return len(self.plots) * self.perimeter()

    def add(self, plot: Plot, plots: Dict[Tuple[int,int], Plot]):
        if plot.crop != self.crop or plot.assigned_region:
            return
        plot.assigned_region = True
        self.plots.append(plot)
        for n in Plot.neighbors(plot.coordinate[0], plot.coordinate[1]):
            neighboring_plot = plots.get(n, None)
            if neighboring_plot:
                self.add(neighboring_plot, plots)


@dataclass
class Garden:
    regions: List[Region] = field(default_factory=list)
    plots: Dict[Tuple[int,int], Plot] = field(default_factory=dict)

    def cost(self) -> int:
        return sum([r.cost() for r in self.regions])

    def assign_regions(self):
        for plot in self.plots.values():
            if not plot.assigned_region:
                region = Region(plot.crop)
                region.add(plot, self.plots)
                self.regions.append(region)


def main():
    with open('resources/day12.txt', 'r') as file:
        crop_map: Dict[Tuple[int,int], str] = {}
        matrix = [line.strip() for line in file]
        for i, row in enumerate(matrix):
            for j, crop in enumerate(row):
                crop_map[(i, j)] = crop

        garden = Garden()
        for coordinate, crop in crop_map.items():
            perimeter = 0
            for n in Plot.neighbors(coordinate[0], coordinate[1]):
                if crop != crop_map.get(n, None):
                    perimeter += 1
            garden.plots[coordinate] = Plot(crop, coordinate, perimeter)

        garden.assign_regions()
        print(f"answer is {garden.cost()}")


if __name__ == '__main__':
    main()