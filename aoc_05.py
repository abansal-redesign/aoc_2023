import re
class SeedData:
    def __init__(self, seed, soil, fert, water, light, temp, humid, loc):
        self.seed = seed
        self.soil = soil
        self.fert = fert
        self.water = water
        self.light = light
        self.temp = temp
        self.humid = humid
        self.loc = loc

class SeedSoilMap:
    def __init__(self, seed_soil_data):
        self.data = seed_soil_data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class SoilFertilizerMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class FertilizerWaterMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class WaterLightMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class LightTempMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class TempHumidMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class HumidLocationMap:
    def __init__(self, data):
        self.data = data
        self.map = {}
        for each in self.data:
            self.find_map(each)
        
    def find_map(self, line_data):
        for each_line_data in self.data:
            des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
            for i in range(0, length):
                self.map[src + i] = des + i

class AnalyseData:
    def __init__(self, all_data):
        self.all_data = all_data
        self.seed_inst = []
        self.map_all_data()
        self.find_seed_data()
        
    def map_all_data(self):
        self.seed_to_soil = SeedSoilMap(self.all_data['seed-to-soil']).map
        self.soil_to_fert = SoilFertilizerMap(self.all_data['soil-to-fertilizer']).map
        self.fert_to_water = FertilizerWaterMap(self.all_data['fertilizer-to-water']).map
        self.water_to_light = WaterLightMap(self.all_data['water-to-light']).map
        self.light_to_temp = LightTempMap(self.all_data['light-to-temperature']).map
        self.temp_to_humid = TempHumidMap(self.all_data['temperature-to-humidity']).map
        self.humid_to_loc = HumidLocationMap(self.all_data['humidity-to-location']).map
        self.seeds = self.all_data['seeds'][0]
    
    def find_seed_data(self):
        for each in self.seeds:
            seed = each
            print(seed)
            # find soil from seed values
            if seed in self.seed_to_soil:
                soil = self.seed_to_soil[seed]
            else:
                soil = seed
            # find fert from soil values
            if soil in self.soil_to_fert:
                fert = self.soil_to_fert[soil]
            else:
                fert = soil
            # find water from fert values
            if fert in self.fert_to_water:
                water = self.fert_to_water[fert]
            else:
                water = fert
            # find light from water values
            if water in self.water_to_light:
                light = self.water_to_light[water]
            else:
                light = water
            # find temp from light values
            if light in self.light_to_temp:
                temp = self.water_to_light[light]
            else:
                temp = light
            # find humid from temp values
            if temp in self.temp_to_humid:
                humid = self.temp_to_humid[temp]
            else:
                humid = temp
            # find location from humid values
            if humid in self.humid_to_loc:
                loc = self.humid_to_loc[humid]
            else:
                loc = humid
            seed_inst = SeedData(seed, soil, fert, water, light, temp, humid, loc)
            self.seed_inst.append(seed_inst)
            
    def least_location_value(self):
        location_val = None
        for each in self.seed_inst:
            if not location_val:
                location_val = each.loc
            if each.loc < location_val:
                location_val = each.loc
        return location_val

def main():
    data = open('aoc_05_sample.txt', 'r').readlines()
    all_data = {}
    heading = None
    for each in data:
        heading_data = re.findall('[^0-9 \\n:]+', each)
        num_data = re.findall('[0-9]+', each)
        if heading_data:
            heading = heading_data[0]
            all_data[heading] = []
        if num_data:
            converted_data = [int(each) for each in num_data]
            all_data[heading].append(converted_data)

    analyse_data = AnalyseData(all_data)
    print(analyse_data.least_location_value())
    
main()
    
