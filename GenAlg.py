import copy
import random
import requests
from PIL import Image as Img


class FlatDNA:
    Gens = {
        'Type': [['E', 'R'], 0.5],
        'Rooms': [['1room', '2rooms'], 0.5],
    }

    def __init__(self, DNA=None):

        self.DNA = {
            'Type': random.choice(FlatDNA.Gens['Type'][0]),
            'Rooms': random.choice(FlatDNA.Gens['Rooms'][0])
        }

        if DNA is not None:
            for i in DNA.keys():
                self.DNA[i] = DNA[i]

    def __repr__(self):
        return str(self.DNA)


class Floor:

    def __init__(self, N):
        self.Depth = None
        self.Width = None
        self.Area = None

        self.Floor_Percentage_Dict = None

        self.N = N
        self.Plan = []

        for i in range(N):
            self.Plan.append([FlatDNA({'Type': 'R'}), []])
        self.Plan[0][0].DNA['Type'] = 'E'
        self.Plan[-1][0].DNA['Type'] = 'E'

    def fill_floor(self, i, label, array):
        while True:
            flat = random.choice(array)
            lab = flat[0]['Rooms']

            if lab == label:
                self.Plan[i][1].append(flat[1][0])
                self.Plan[i].append(flat[2])
                break

    def add_data(self, end_apartments, row_apartments):

        for i in range(len(self.Plan)):
            if self.Plan[i][0].DNA['Type'] == 'E':
                label = self.Plan[i][0].DNA['Rooms']
                self.fill_floor(i, label, end_apartments)

            else:
                label = self.Plan[i][0].DNA['Rooms']
                self.fill_floor(i, label, row_apartments)

    def calculate_floor_area(self):
        self.Width = 0
        self.Length = 0
        for i in range(len(self.Plan)):
            self.Width += self.Plan[i][2]['Width']
            self.Length += self.Plan[i][2]['Depth']

        self.Area = self.Width * self.Length

    def calculate_floor_percentage(self):
        self.Floor_Percentage_Dict = {}
        for g in FlatDNA.Gens['Rooms'][0]:

            if g not in self.Floor_Percentage_Dict.keys():
                self.Floor_Percentage_Dict[g] = 0
            for i in range(len(self.Plan)):

                if self.Plan[i][0].DNA['Rooms'] == g:
                    self.Floor_Percentage_Dict[g] += 1

        for i in self.Floor_Percentage_Dict.keys():
            self.Floor_Percentage_Dict[i] = self.Floor_Percentage_Dict[i] * 100 / self.N

    def get_png(self):
        urls = []

        for i in range(len(self.Plan)):
            urls.append(self.Plan[i][1][0])

        images = [Img.open(requests.get(x, stream=True).raw) for x in urls]

        widths, lengths = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_length = max(lengths)

        floor_img = Img.new('RGB', (total_width, max_length), color='white')
        x_offset = 0
        for im in images:
            floor_img.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        floor_img.save(f'./floor_img.png')


class GenerationFloor:
    Floor_Size = 10
    Survivors = 1
    Chances = 20
    Were_Mutated = 100

    def __init__(self, data):
        self.data = data
        self.Generation = {}

        self.Best_Floor = None
        self.Best_Delta = None
        self.Best_Delta_P = None
        self.Best_Delta_A = None

    def build_new_generation(self, end_apartments, row_apartments, survivors_array=None):

        if survivors_array is None:
            survivors_array = []
        generation_new = {}
        self.Generation = {}
        index = 0

        for i in survivors_array:
            generation_new[index] = copy.deepcopy(i)
            index += 1

        for i in survivors_array:
            for k in range(GenerationFloor.Were_Mutated):
                for p in range(len(i.Plan)):
                    if i.Plan[p][0].DNA['Type'] == 'E':
                        self.mutation(i, p, end_apartments)

                    else:
                        self.mutation(i, p, row_apartments)

                generation_new[index] = i
                index += 1

        for i in range(GenerationFloor.Chances):
            new_floor_prototype = GenerationFloor.Floor_Size + random.randint(-3, 4)

            if new_floor_prototype <= 0:
                new_floor_prototype = 1

            new_floor = Floor(new_floor_prototype)
            new_floor.add_data(end_apartments, row_apartments)
            generation_new[index] = new_floor
            index += 1

        self.Generation = copy.deepcopy(generation_new)

    def run_alg(self, N, end_apartments, row_apartments):
        for i in range(N):
            print(f'--- Generation №{(i + 1)} ---')
            print('==============================================')
            if hasattr(self, 'BestFloor'):
                self.build_new_generation(end_apartments, row_apartments, [self.Best_Floor[0]])
            else:
                self.build_new_generation(end_apartments, row_apartments)

            self.best_floor(GenerationFloor.Survivors)
            print(f'First generation width: {self.Generation[0].Width}')
            print(f'Generation`s quantity: {len(self.Generation)}')

        print(
            f'Final percentage of apartments: {self.Best_Floor[0].Floor_Percentage_Dict}, '
            f'deviations: {self.Best_Delta_P}/{self.Best_Delta_A}/{self.Best_Delta}, width: {self.Best_Floor[0].Width}')
        print(f'Apartment quantity : {self.Best_Floor[0].N}')
        return self.Best_Floor[0]

    def mutation(self, i, p, array):
        while True:
            label = i.Plan[p][0].DNA['Rooms']
            if random.randint(1, 20) == 5:
                flat = random.choice(array)
                lab = flat[0]['Rooms']

                if lab == label:
                    i.Plan[p][1][0] = flat
                    i.Plan[p].append(flat[2])
                    break

    def best_floor(self, N=1):
        delta_p = 1000000
        delta_a = 1000000
        delta = 1000000

        best_floor = []
        for i in self.Generation.keys():
            g = self.Generation[i]
            g.calculate_floor_percentage()
            g.calculate_floor_area()

            delta_p_tmp = self.compare_floor_percentage(
                {
                    '1room': self.data[5],
                    '2rooms': self.data[6],
                },
                g.Floor_Percentage_Dict)

            delta_s_tmp = abs(g.Width - self.data[2])
            delta_tmp = delta_p_tmp + delta_s_tmp / 1500
            if delta_tmp < delta:

                best_floor.insert(0, g)
                delta_p = delta_p_tmp
                delta_a = delta_s_tmp
                delta = delta_tmp

        self.Best_Floor = best_floor
        self.Best_Delta = delta
        self.Best_Delta_P = delta_p
        self.Best_Delta_A = delta_a

        GenerationFloor.Floor_Size = self.Best_Floor[0].N

    def compare_floor_percentage(self, d1, d2):
        delta = 0
        for i in d1.keys():
            delta += abs(d1[i] - d2[i])
        return delta
