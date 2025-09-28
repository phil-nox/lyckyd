
import enum

import pandas as pd

import lyckyd

# load ##############################################################
df = pd.DataFrame({                                     # tag_load
    "planet": ["Earth", "Mars"],                        # tag_load
    "radius_km": [6371, 3390],                          # tag_load
    # "count": [3, 4],        # uncomment & run         # tag_load
})                                                      # tag_load

# modification ######################################################
# df["new_col"] = 0


# columns ###########################################################
                                # <class 'pandas.core.frame.DataFrame'> # tag_col
                                # RangeIndex: 2 entries, 0 to 1         # tag_col
                                # Data columns (total 2 columns):       # tag_col
                                # #   Column     Non-Null Count  Dtype  # tag_col
class C(enum.StrEnum):          # --  ------     --------------  -----  # tag_col
    planet = 'planet'           # 0   planet     2 non-null      object # tag_col
    radius_km = 'radius_km'     # 1   radius_km  2 non-null      int64  # tag_col
                                # dtypes: int64(1), object(1)           # tag_col
                                # memory usage: 164.0+ bytes            # tag_col
                                #                                       # tag_col
                                # 2025-09-01 00:00:01.000000+00:00      # tag_col
# raise SystemExit(f'File "{__file__}", line 31 patched. Remove/comment this line if the patch is valid.')  # tag_raise


# check and tag_patch ##############################################
if lyckyd.check_n_tag_patch(
    df=df,                                                              # tag_setup
    col_cls=C,                                                          # tag_setup
    pd_info_comment=True,                                               # tag_setup
    add_raise_after_patch=True,                                         # tag_setup
    data_name_2_enum_name=lambda x: x.lower().replace(" ", "_"),
    path_2_file=__file__,
):
    raise SystemExit(f'lyckyd.check failed - File "{__file__}", line 43 patched')  # tag_fail


# usage (in other files) ######################################################
if __name__ == '__main__':  # #################################################

    import output                                                       # tag_usage
                                                                        # tag_usage
    foo = output.df[output.C.planet].unique()                           # tag_usage
    print(foo[:8])                                                      # tag_usage
