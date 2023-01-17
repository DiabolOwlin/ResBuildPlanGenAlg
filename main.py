import copy
import random
import requests
from PIL import Image as img

# TO DO: get max width available for building (reduces all if`s that might come along in the way)
# TO DO 03.12: get 'Type' and 'Layout'

# can generate one side of apartments and then flip it and get the opposite side. which will make a complete layout
# adjust all flats to one level from the window site
#     similar thing  ↑↑↑ ↓↓↓
# corridor (required all flats to be turned to corridor with the doors wall)
token = 'secret_T45iO2TZOukJtJQLW5vSf7POJa2W9v7RLQSeLFeMVxb'
databaseID = 'b2cb393e7412464cb51ad5f5d9360bae'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}



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
        # print(f'current DNA: {self.DNA}')

        if DNA is not None:
            for i in DNA.keys():
                self.DNA[i] = DNA[i]

    def __repr__(self):
        return str(self.DNA)


def define_params(apart_type):
    params = {
        "filter": {
            "property": "Type",
            "multi_select": {
                "contains": f"{apart_type}"
            }
        }
    }
    return params


def query_database(databaseId, header, apart_type):
    params = define_params(apart_type)
    read_url = f"https://api.notion.com/v1/databases/{databaseId}/query"
    res = requests.request("POST", read_url, json=params, headers=header)
    data = res.json()
    return data


def retrieve_database(databaseId, header):
    read_url = f"https://api.notion.com/v1/databases/{databaseId}"
    res = requests.request("GET", read_url, headers=header)
    data = res.json()
    return data


text_e = query_database(databaseID, headers, 'End')
text_e = text_e.get('results')
# print(text_e[0].get('properties').get('Width'))

end_apartments = []
for _ in range(len(text_e)):
    type_name = text_e[_].get('properties').get('Type').get('multi_select')[0].get('name')[0]
    rooms_count = text_e[_].get('properties').get('Rooms').get('multi_select')[0].get('name')
    layout = text_e[_].get('properties').get('Layout').get('files')[0].get('file').get('url')
    width = text_e[_].get('properties').get('Width').get('number')
    depth = text_e[_].get('properties').get('Depth').get('number')
    end_apartments.append([{'Type': type_name, 'Rooms': rooms_count}, [layout], {'Width': width, 'Depth': depth}])

# print(f'end: {end_apartments}')
text_r = query_database(databaseID, headers, 'Row')
text_r = text_r.get('results')

row_apartments = []
for _ in range(len(text_r)):
    type_name = text_r[_].get('properties').get('Type').get('multi_select')[0].get('name')[0]
    rooms_count = text_r[_].get('properties').get('Rooms').get('multi_select')[0].get('name')
    layout = text_r[_].get('properties').get('Layout').get('files')[0].get('file').get('url')
    width = text_r[_].get('properties').get('Width').get('number')
    depth = text_r[_].get('properties').get('Depth').get('number')
    row_apartments.append([{'Type': type_name, 'Rooms': rooms_count}, [layout], {'Width': width, 'Depth': depth}])


# print(f'end: {row_apartments}')


class Floor:

    def __init__(self, N):
        self.N = N
        self.Plan = []
        for i in range(N):
            self.Plan.append([FlatDNA({'Type': 'R'}), []])
        self.Plan[0][0].DNA['Type'] = 'E'
        self.Plan[-1][0].DNA['Type'] = 'E'
        # print(f"Length of floor: {len(self.Plan)}")
    # Filling the DNA of the floor with specific variants of apartments from the database (random enumeration)

    def fill_floor(self):

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
        # floor_img = img.new('RGB', (6000, 3000), color='white')
        # w = 0
        # for i in range(len(self.Plan)):
        #     print(i)
        #     url = self.Plan[i][1][0]
        #     print(url)
        #     im = img.open(requests.get(url, stream=True).raw)
        #     floor_img.paste(im, (int(w / 10), 0))
        #     w += self.Plan[i][2]['Width']
        # print(f"Width from get_png: {w}")
        # floor_img.save(f'./floor_img.png')
        urls = []
        for i in range(len(self.Plan)):
            urls.append(self.Plan[i][1][0])

        images = [img.open(requests.get(x, stream=True).raw) for x in urls]
        widths, depths = zip(*(i.size for i in images))
        total_width = sum(widths)
        print(f'total_width: {total_width}')
        max_height = max(depths)
        print(f'max_height: {max_height}')

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

    def run_generations(self, N):
        for i in range(N):
            print(f'--- Generation №{(i + 1)} ---')
            print('===========================================')
            if hasattr(self, 'BestFloor'):
                # Creating a generation and pass on the best version of the previous generation
                self.build_new_generation([self.BestFloor[0]])
            else:
                # Creating first generation
                self.build_new_generation()
            # Determining the best option in the current generation
            self.find_best_floor(GeneticFloor.SURVIVORS)
            print(f'First generation option: {self.Generation[0].Width}')
            print(f'Generation`s options quantity: {len(self.Generation)}')
        print(
            f'Final distribution of apartments: {self.BestFloor[0].FloorPercent_Dict}, '
            f'deviations: {self.BestDeltaP}/{self.BestDeltaS}/{self.BestDelta}, width: {self.BestFloor[0].Width}')
        print(f'Apartment quantity : {self.BestFloor[0].N}')
        print('###########################################\nBest floor:')
        return self.BestFloor[0]







    def build_new_generation(self, survivors_array=None):
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
            floor1.fill_floor()
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
                {#'S': self.data[4],
                 '1room': self.data[5],
                 '2rooms': self.data[6],
                 #'3k': self.data[7]
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


if __name__ == "__main__":

    gen_floor = GeneticFloor([1, 0, 60000, 10000, 50, 30, 10, 10])

    best_floor = gen_floor.run_generations(20)
    best_floor.get_png()

    # for i in range(len(best_floor)):
    #     print(best_floor[i][1])


