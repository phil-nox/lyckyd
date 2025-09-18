
import enum
import typing as ty

import pandas as pd


def data_mismatch(
        df: pd.DataFrame,
        col_cls: ty.Type[enum.StrEnum]
) -> bool:

    col_by_code: set[str] = {el for el in col_cls}
    col_by_data: set[str] = set(df.columns)

    return bool(col_by_data ^ col_by_code)


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    the_df: pd.DataFrame = pd.DataFrame({
        'planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'radius_km': [2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622],
    })


    class F(enum.StrEnum):
        planet = 'planet'
        radius_km = 'radius_km'
        more = 'more'

    rlt = data_mismatch(the_df, F)
    print(rlt)
