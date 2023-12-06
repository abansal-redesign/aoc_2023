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
    def __init__(self, data):
        self.data = data
                
    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class SoilFertilizerMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class FertilizerWaterMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class WaterLightMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class LightTempMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class TempHumidMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val

class HumidLocationMap:
    def __init__(self, data):
        self.data = data

    def find_map_val(self, src_val):
        val = None
        for each_line_data in self.data:
            if not val:
                des, src, length = each_line_data[0], each_line_data[1], each_line_data[2]
                if src_val in range(src, src + length):
                    val = des + (src_val - src)
        if not val:
            val = src_val
        return val
            

class AnalyseData:
    def __init__(self, all_data):
        self.all_data = all_data
        self.map_all_data()
        self.least_loc_val = None
        
    def map_all_data(self):
        self.seed_to_soil = SeedSoilMap(self.all_data['seed-to-soil'])
        self.soil_to_fert = SoilFertilizerMap(self.all_data['soil-to-fertilizer'])
        self.fert_to_water = FertilizerWaterMap(self.all_data['fertilizer-to-water'])
        self.water_to_light = WaterLightMap(self.all_data['water-to-light'])
        self.light_to_temp = LightTempMap(self.all_data['light-to-temperature'])
        self.temp_to_humid = TempHumidMap(self.all_data['temperature-to-humidity'])
        self.humid_to_loc = HumidLocationMap(self.all_data['humidity-to-location'])
    
    def find_seed_data(self, seed):
        # find soil from seed values
        soil = self.seed_to_soil.find_map_val(seed)
        # find fert from soil values
        fert = self.soil_to_fert.find_map_val(soil)
        # find water from fert values
        water = self.fert_to_water.find_map_val(fert)
        # find light from water values
        light = self.water_to_light.find_map_val(water)
        # find temp from light values
        temp = self.light_to_temp.find_map_val(light)
        # find humid from temp values
        humid = self.temp_to_humid.find_map_val(temp)
        # find location from humid values
        loc = self.humid_to_loc.find_map_val(humid)
        # print(seed, soil, fert, water, light, temp, humid, loc)
        seed_inst = SeedData(seed, soil, fert, water, light, temp, humid, loc)
        self.update_least_location_value(seed_inst)

    def update_least_location_value(self, seed_inst):
        if not self.least_loc_val:
            self.least_loc_val = seed_inst.loc
        if seed_inst.loc < self.least_loc_val:
            self.least_loc_val = seed_inst.loc

def main():
    data = open('aoc_05.txt', 'r').readlines()
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
    seeds = all_data['seeds'][0]
    for i in range(0, len(seeds), 2):
        for j in range(0, seeds[i + 1]):
            analyse_data.find_seed_data(seeds[i] + j)
    print(analyse_data.least_loc_val)
    
main()
    
