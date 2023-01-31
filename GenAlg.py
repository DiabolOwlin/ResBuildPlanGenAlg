import copy
import random
import requests
from PIL import Image as img


class FlatDNA:
    Gens = {
        # '''Apartment type: E - End apartment, S - standard apartment '''
        # '''Layout: S - studio apartment, 1k - 1 room, 2k - 2 rooms, 3k - 3 rooms'''

        'Type': [['E', 'R'], 0.5],
        'Rooms': [['1room', '2rooms'], 0.5],
    }

    def __init__(self, DNA=None):

        self.DNA = {
            'Type': random.choice(FlatDNA.Gens['Type'][0]),
            'Rooms': random.choice(FlatDNA.Gens['Rooms'][0])
        }

        # self.DNA = {
        #     'Type': random.choice(FlatDNA.Gens['Type'][0])}
        # if self.DNA['Type'] == 'E':
        #     choice_list = ['1room', '2rooms']
        #     self.DNA['Rooms'] = random.choice(choice_list)
        #
        # else:
        #     self.DNA['Rooms'] = random.choice(FlatDNA.Gens['Rooms'][0])
        # print(f' current DNA: {self.DNA}')

        if DNA is not None:
            for i in DNA.keys():
                self.DNA[i] = DNA[i]

    def __repr__(self):
        return str(self.DNA)


class Floor:

    def __init__(self, N):
        self.Depth = None
        self.Width = None
        self.Square = None
        self.FloorPercent_Dict = None

        self.N = N
        self.Plan = []
        for i in range(N):
            self.Plan.append([FlatDNA({'Type': 'R'}), []])
        self.Plan[0][0].DNA['Type'] = 'E'
        self.Plan[-1][0].DNA['Type'] = 'E'
        # print(f"Length of floor: {len(self.Plan)}")

    # Filling the DNA of the floor with specific variants of apartments from the database (random enumeration)

    def fill_floor(self, end_apartments, row_apartments):

        for i in range(len(self.Plan)):
            if self.Plan[i][0].DNA['Type'] == 'E':
                label = self.Plan[i][0].DNA['Rooms']
                while True:
                    flat = random.choice(end_apartments)
                    lab = flat[0]['Rooms']
                    if lab == label:
                        self.Plan[i][1].append(flat[1][0])
                        self.Plan[i].append(flat[2])
                        break

            else:
                # if self.Plan[i][0].DNA['Type'] == 'R':
                label = self.Plan[i][0].DNA['Rooms']
                while True:
                    flat = random.choice(row_apartments)
                    lab = flat[0]['Rooms']

                    if lab == label:
                        self.Plan[i][1].append(flat[1][0])
                        self.Plan[i].append(flat[2])
                        break

    # Determining the actual floor geometry and area
    def floor_square(self):
        self.Width = 0
        self.Depth = 0
        for i in range(len(self.Plan)):
            self.Width += self.Plan[i][2]['Width']
            self.Depth += self.Plan[i][2]['Depth']

        self.Square = self.Width * self.Depth

    # Dictionary generation function with the percentage of apartments on the floor
    def floor_percent(self):
        self.FloorPercent_Dict = {}
        for g in FlatDNA.Gens['Rooms'][0]:
            if g not in self.FloorPercent_Dict.keys():
                self.FloorPercent_Dict[g] = 0
            for i in range(len(self.Plan)):
                if self.Plan[i][0].DNA['Rooms'] == g:
                    self.FloorPercent_Dict[g] += 1
        for i in self.FloorPercent_Dict.keys():
            self.FloorPercent_Dict[i] = self.FloorPercent_Dict[i] * 100 / self.N

    def get_png(self):
        urls = []
        for i in range(len(self.Plan)):
            urls.append(self.Plan[i][1][0])

        images = [img.open(requests.get(x, stream=True).raw) for x in urls]

        widths, depths = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(depths)

        floor_img = img.new('RGB', (total_width, max_height), color='white')
        x_offset = 0
        for im in images:
            floor_img.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        floor_img.save(f'./floor_img.png')


class GeneticFloor:
    FLOOR_SIZE = 10
    NEWBORN = 20
    MUTATED = 100
    SURVIVORS = 1

    # [Floors, Angle, Floor_width, Floor_depth, Room_S, Room_1k, Room_2k, Room_3k]
    def __init__(self, data):
        self.data = data
        self.Generation = {}

    def run_generations(self, N, end_apartments, row_apartments):
        for i in range(N):
            print(f'--- Generation №{(i + 1)} ---')
            print('===========================================')
            if hasattr(self, 'BestFloor'):

                # Creating a generation and pass on the best version of the previous generation
                self.build_new_generation(end_apartments, row_apartments, [self.BestFloor[0]])
            else:

                # Creating first generation
                self.build_new_generation(end_apartments, row_apartments)

            # Determining the best option in the current generation
            self.find_best_floor(GeneticFloor.SURVIVORS)
            print(f'First generation option: {self.Generation[0].Width}')
            print(f'Generation`s options quantity: {len(self.Generation)}')

        print(
            f'Final distribution of apartments: {self.BestFloor[0].FloorPercent_Dict}, '
            f'deviations: {self.BestDeltaP}/{self.BestDeltaS}/{self.BestDelta}, width: {self.BestFloor[0].Width}')
        print(f'Apartment quantity : {self.BestFloor[0].N}')
        return self.BestFloor[0]

    def build_new_generation(self, end_apartments, row_apartments, survivors_array=None):
        if survivors_array is None:
            survivors_array = []
        new_generation = {}
        self.Generation = {}
        index = 0

        # Adding the best floors from the previous generation to the new generation
        for i in survivors_array:
            new_generation[index] = copy.deepcopy(i)
            index += 1

        # Changing the layout in the best options from the previous generation
        for i in survivors_array:
            for k in range(GeneticFloor.MUTATED):
                for p in range(len(i.Plan)):
                    if i.Plan[p][0].DNA['Type'] == 'E':

                        while True:
                            label = i.Plan[p][0].DNA['Rooms']
                            if random.randint(1, 20) == 5:
                                flat = random.choice(end_apartments)
                                lab = flat[0]['Rooms']

                                if lab == label:
                                    i.Plan[p][1][0] = flat
                                    break
                        i.Plan[p].append(flat[2])
                        print(f'Mutation of the corner apartment')

                    if i.Plan[p][0].DNA['Type'] == 'R':

                        while True:
                            label = i.Plan[p][0].DNA['Rooms']
                            if random.randint(1, 20) == 5:
                                flat = random.choice(row_apartments)
                                lab = flat[0]['Rooms']

                                if lab == label:
                                    i.Plan[p][1][0] = flat
                                    break
                        i.Plan[p].append(flat[2])
                        print(f'Mutation of the row apartment')

                new_generation[index] = i
                index += 1

        # Adding new options to the new generation
        for i in range(GeneticFloor.NEWBORN):
            n_new = GeneticFloor.FLOOR_SIZE + random.randint(-3, 4)

            if n_new <= 0:
                n_new = 1
            floor1 = Floor(n_new)
            floor1.fill_floor(end_apartments, row_apartments)
            new_generation[index] = floor1
            index += 1

        self.Generation = copy.deepcopy(new_generation)

    def find_best_floor(self, N=1):
        delta_p = 1000000  # Percentage deviation
        delta_s = 1000000  # Area deviation
        delta = 1000000  # Deviation summary
        # Delta_array = []
        best_floor = []
        for i in self.Generation.keys():
            g = self.Generation[i]
            # Determined percentages
            g.floor_percent()
            # Defined geometry
            g.floor_square()
            # Calculate the deviations from the specified percentage
            delta_p_tmp = self.compare_floor_percentage(
                {  # 'S': self.data[4],
                    '1room': self.data[5],
                    '2rooms': self.data[6],
                    # '3k': self.data[7]
                },
                g.FloorPercent_Dict)
            # Calculate the deviation from the width of the floor
            delta_s_tmp = abs(g.Width - self.data[2])
            # Output the combined deviation
            delta_tmp = delta_p_tmp + delta_s_tmp / 1500
            if delta_tmp < delta:
                best_floor.insert(0, g)
                delta_p = delta_p_tmp
                delta_s = delta_s_tmp
                delta = delta_tmp
                # Delta_array.append(delta_tmp)
        self.BestFloor = best_floor
        self.BestDelta = delta
        self.BestDeltaP = delta_p
        self.BestDeltaS = delta_s
        GeneticFloor.FLOOR_SIZE = self.BestFloor[0].N

    def compare_floor_percentage(self, d1, d2):
        delta = 0
        for i in d1.keys():
            delta += abs(d1[i] - d2[i])
        return delta