"""Calculations history class"""
import pandas as pd
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from tests.csvread_writer import csv_write


class Calculations:
    """Class with fundamental methods to operate calculator"""

    history = []

    @staticmethod
    def clear_history():
        """clears history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """counts number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """gets latest calculation from user as an object"""
        return Calculations.history[0]

    @staticmethod
    def get_last_calculation_actual_value():
        """gets latest calculation from user as a result"""
        return Calculations.get_last_calculation().get_result()


    @staticmethod
    def get_first_calculation():
        """gets first calculation from user"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """get a specific calculation from history input index"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(inserted_calculation):
        """append calculation from history"""
        Calculations.clear_history()
        return Calculations.history.append(inserted_calculation)

    @staticmethod
    def addition_calculation(values):  # pass list of values
        """add Addition to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Addition.create(values))
        return Calculations.history[-1]  # return the result of the addition from the history

    @staticmethod
    def multiplication_calculation(values):
        """add Multiplication to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.history[-1]

    @staticmethod
    def subtraction_calculation(values):
        """add Subtraction to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.history[-1]

    @staticmethod
    def division_calculation(values):
        """add Division to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Division.create(values))
        return Calculations.history[-1]

    @staticmethod
    def create_dataframe_to_write(val1, val2, result, operation):
        """appends values and operation to history"""
        df_to_write = pd.DataFrame(columns=['Value 1', 'Value 2', 'Result', 'Operation'])
        df_to_write = df_to_write.append({'Value 1': val1,
                                          'Value 2': val2,
                                          'Result': result,
                                          'Operation': operation},
                                         ignore_index=True)
        return csv_write(df_to_write)
