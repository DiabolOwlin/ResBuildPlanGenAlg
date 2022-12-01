import copy
import random
import requests
from PIL import Image as img
import notion_database



# Vitalik
# token = 'secret_IvTAjHlkOiQT2YGm4ZmzNOsmnVeVxtzLg4vR4FYck9U'
# databaseID = 'e4d10988ab964c22a62a2a6baf745b8a'

token = 'secret_T45iO2TZOukJtJQLW5vSf7POJa2W9v7RLQSeLFeMVxb'
databaseID = 'b2cb393e7412464cb51ad5f5d9360bae'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


class FlatDNA:
    Gens = {
        '''Apartment type: E - End apartment, S - standard apartment '''
        '''Layout: S - studio apartment, 1k - 1 room, 2k - 2 rooms, 3k - 3 rooms'''

        'Type': [['E', 'S'], 0.5],
        'Layout': [['S', '1k', '2k', '3k'], 0.5],
    }

    def __init__(self, DNA=None):

        self.DNA = {
            'Type': random.choice(FlatDNA.Gens['Type'][0]),
            'Layout': random.choice(FlatDNA.Gens['Layout'][0])
        }

        if DNA is not None:
            for i in DNA.keys():
                self.DNA[i] = DNA[i]

    def __repr__(self):
        return str(self.DNA)




def define_params(apart_type):

    PARAMS = {
        "filter": {
            "property": "Type",
            "multi_select": {
                "contains": f"{apart_type}"
            }
        }
    }
    return PARAMS

def query_database(databaseId, headers, apart_type):
    PARAMS = define_params(apart_type)
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    res = requests.request("POST", readUrl, json=PARAMS, headers=headers)
    data = res.json()
    return data



def retrieve_database(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}"
    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()
    return data





class Floor:

    def __init__(self, N):
        self.N = N
        self.Plan = []
        for i in range(N):
            self.Plan.append([FlatDNA({'Type': 'S'}), []])
        self.Plan[0][0].DNA['Type'] = 'E'
        self.Plan[-1][0].DNA['Type'] = 'E'

    # Filling the DNA of the floor with specific variants of apartments from the database (random enumeration)
    def fill_floor(self):
        for i in range(len(self.Plan)):
            if self.Plan[i][0].DNA['Type'] == 'E':
                flat = random.choice(query_database(databaseID, headers, 'End'))
                self.Plan[i][1].append(flat)
                # print(flat)
            if self.Plan[i][0].DNA['Type'] == 'S':
                flat = random.choice(query_database(databaseID, headers, 'Row'))
                self.Plan[i][1].append(flat)
                # print(flat)

    # Determining the actual floor geometry and area
    def floor_square(self):
        self.Width = 0
        self.Depth = 0
        for i in range(len(self.Plan)):
            self.Width += self.Plan[i][1][0]['properties']['Width']['number']
            self.Depth += self.Plan[i][1][0]['properties']['Depth']['number']
        self.Square = self.Width * self.Depth

    # Dictionary generation function with the percentage of apartments on the floor
    def floor_percent(self):
        self.FloorPercent_Dict = {}
        for g in FlatDNA.Gens['Layout'][0]:
            if g not in self.FloorPercent_Dict.keys():
                self.FloorPercent_Dict[g] = 0
            for i in range(len(self.Plan)):
                if self.Plan[i][0].DNA['Layout'] == g:
                    self.FloorPercent_Dict[g] += 1
        for i in self.FloorPercent_Dict.keys():
            self.FloorPercent_Dict[i] = self.FloorPercent_Dict[i] * 100 / self.N

    def get_png(self):
        floor_img = img.new('RGB', (6000, 3000), color='white')
        w = 0
        for i in range(len(self.Plan)):
            url = self.Plan[i][1][0]['properties']['Foto']['files'][0]['file']['url']
            im = img.open(requests.get(url, stream=True).raw)
            floor_img.paste(im, (int(w / 10), 0))
            w += self.Plan[i][1][0]['properties']['Width']['number']
        floor_img.save(f'./floor_img.png')


class GeneticFloor:
    FLOOR_SIZE = 10
    NEWBORN = 20
    MUTATED = 100
    SURVIVORS = 1

    # [Floors, Angle, Floor_width, Floor_deep, Room_S, Room_1k, Room_2k, Room_3k]
    def __init__(self, data):
        self.data = data
        self.Generation = {}

    def run_generations(self, N):
        for i in range(N):
            # print(f'--- Generation №{(i+1)} ---')
            if hasattr(self, 'BestFloor'):
                # Creating a generation and pass on the best version of the previous generation
                self.build_new_generation([self.BestFloor[0]])
            else:
                # Creating first generation
                self.build_new_generation()
            # Determining the best option in the current generation
            self.find_best_floor(GeneticFloor.SURVIVORS)
            # print(f'First generation option: {self.Generation[0].Width}')
            # print(f'Generation`s options quantity: {len(self.Generation)}')
        print(
            f'Final distribution of apartments: {self.BestFloor[0].FloorPercent_Dict}, deviations: {self.BestDeltaP}/{self.BestDeltaS}/{self.BestDelta}, width: {self.BestFloor[0].Width}')
        # print(f'Apartment quantity : {self.BestFloor[0].N}')

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
                        if random.randint(1, 20) == 5:
                            flat = random.choice(db_flat_type_dict['Cornet'])
                            i.Plan[p][1][0] = flat
                            # print(f'Mutation of the corner apartment')
                    if i.Plan[p][0].DNA['Type'] == 'S':
                        if random.randint(1, 20) == 5:
                            flat = random.choice(db_flat_type_dict['Row'])
                            i.Plan[p][1][0] = flat
                            # print(f'Mutation of the row apartment')
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
                {'S': self.data[4], '1k': self.data[5], '2k': self.data[6], '3k': self.data[7]}, g.FloorPercent_Dict)
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


# if __name__ == "__main__":

