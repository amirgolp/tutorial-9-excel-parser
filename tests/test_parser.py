import os.path
from nomad.client import parse, normalize_all


def test_parser():
    test_file = os.path.join(os.path.dirname(__file__), 'data', 'test.excel-file.xlsx')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.my_cell_data == 1
    assert (entry_archive.data.my_range_data == [[1], [2]]).all()
