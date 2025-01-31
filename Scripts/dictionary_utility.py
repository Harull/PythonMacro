class DictionaryUtil():
    @staticmethod
    def GetUniqueStringKey(dictionnary : dict, wanted_key : str):
        index_to_add = 1
        new_wanted_key = wanted_key

        while new_wanted_key in dictionnary:
            new_wanted_key = wanted_key + "_" + index_to_add
            index_to_add += 1

        return new_wanted_key
    