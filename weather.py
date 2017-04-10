#Kelvin Murumba
#Weather.py
#10/04/2017


from operator import itemgetter

class OpenSomeFile():
    """
    A class which will open the file and return the maximum of the list items
    """
    def __init__(self):# Initialize all the relevant values here
        self.most_diff = 0
        self.open_file()
        print "Day: {0} with a difference of {1}".format(self.most_diff["day"], self.most_diff["diff"])

    def open_file(self): # A function which will open the file
        with open("weather.dat", "r") as weather_dat_f:
            data = weather_dat_f.readlines()
        key_row = data[0]
        other_rows = data[1:]
        self.read_k_v(keys= key_row, data = other_rows)

    def read_k_v(self, **kwargs):# A function which will read the keys and the values
        keys = kwargs.get("keys")
        values = kwargs.get("data")
        all_k_fields = keys.strip().split(" ")
        needed_k_fields = [rel_field for rel_field in all_k_fields if rel_field != ""][:3]
        all_data_fields = [value_r.strip() for value_r in values if len(value_r) > 1]
        dict_ver_list = []
        for row in all_data_fields:
            needed = [needed for needed in row.strip().split(" ") if needed!=""][:3]
            dict_ver = dict(zip(needed_k_fields, needed))
            dict_ver_list.append(dict_ver)

        self.ret_max(dict_list = dict_ver_list)
    def ret_max(self, **kwargs): # A function which will return the maximum valued day
        dict_list = kwargs.get("dict_list")
        diffed_dict = []
        for encoded_row in dict_list:
            max_r = float("".join([val for val in encoded_row["MxT"] if val.isdigit() or val == "."]))
            min_r = float("".join([val for val in encoded_row["MnT"] if val.isdigit() or val == "."]))
            dummy_dict = {
                "day": encoded_row["Dy"],
                "diff": (max_r - min_r)
            }
            diffed_dict.append(dummy_dict)
        self.most_diff = sorted(diffed_dict, key=itemgetter("diff"), reverse = True)[0]

if __name__ == "__main__":
    OpenSomeFile()