
import pandas as pd

sample_df = pd.DataFrame({"planet": ["Earth", "Mars"], "radius_km": [6371, 3390]})


def tag_load_lines(
        path_to_csv:    str | None,
        name_for_df:    str,
) -> list[str]:

    if path_to_csv is None:
        return [
            f'{name_for_df} = pd.DataFrame({{',
            f'    "planet": ["Earth", "Mars"],',
            f'    "radius_km": [6371, 3390],',
            f'    # "count": [3, 4],        # uncomment & run',
            f'}})',
        ]

    return [f'{name_for_df} = pd.read_csv("{path_to_csv}")']


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    rlt = tag_load_lines(name_for_df='test_df', path_to_csv=None)
    # rlt = tag_load_lines(name_for_df='test_df', path_to_csv='the_path_to_csv')
    [print(el) for el in rlt]
