import os
import pandas as pd

class FileReader:

    @staticmethod
    def read_from_file(filename):
        dir_path = os.getcwd()
        file_path = os.path.join(dir_path,"/data/", filename)
        df = pd.read_csv(file_path)
        return df
