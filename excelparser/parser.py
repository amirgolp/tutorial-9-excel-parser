import numpy as np
import pandas as pd

from nomad.metainfo import MSection, Quantity


def row_col_extractor(s):
    head = s.rstrip('0123456789')
    tail = int(s[len(head):]) - 1
    return head, tail


class MyLabExcelSection(MSection):
    cell_range_schema = Quantity(type=str, default='B1:B2')

    my_cell_data = Quantity(type=np.float64)
    my_range_data = Quantity(type=np.float64, shape=['*'])


class MyLabExcelParser:
    def parse(self, mainfile, archive, logger):

        # Part 1: Parsing cell data
        ## Parsing a single quantity from a single cell in the excel file
        cell_loc_1: str = 'B1'
        cell_loc_2: str = 'B2'
        sheet: str = 'Sheet1'

        ## Extracting row and column from the strings using row_col_extractor helper function
        r1, c1 = row_col_extractor(cell_loc_1)
        r2, c2 = row_col_extractor(cell_loc_2)

        ## Reading data using pandas from the excel file
        data_1 = pd.read_excel(
            mainfile, sheet, index_col=None, usecols=r1, header=0, nrows=c1)
        data_2 = pd.read_excel(
            mainfile, sheet, index_col=None, usecols=r2, header=0, nrows=c2)

        # Parsing cell data into NOMAD metadata and Quantities
        archive.metadata.external_id = str(data_1.columns.values[0])
        archive.data = MyLabExcelSection()
        archive.data.my_cell_data = data_2.columns.values[0]

        # Part 2: Parsing range data
        ## Extracting the range data from schema
        cell_range = archive.data.cell_range_schema.split(':')
        row_data, col_data = [], []
        for cell in cell_range:
            col, row = row_col_extractor(cell)
            row_data.append(row)
            col_data.append(col)

        ## Reading data from excel file
        data_3 = pd.read_excel(mainfile, sheet, header=None)
        columns = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        data_3.columns = columns[:data_3.shape[1]]
        specific_range = data_3.iloc[
                         row_data[0]:row_data[1]+1,
                         data_3.columns.get_loc(col_data[0]):data_3.columns.get_loc(col_data[1]) + 1]

        ## Parsing data into NOMAD Quantity
        archive.data.my_range_data = specific_range.values
