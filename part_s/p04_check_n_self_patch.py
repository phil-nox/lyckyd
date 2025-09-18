
import enum
import typing as ty

import pandas as pd

import lyckyd.part_s.p00_gen_col_cls as p00
import lyckyd.part_s.p02_check_df as p02
import lyckyd.part_s.p03_self_patch as p03


def check_n_self_patch(
        df:                     pd.DataFrame,
        col_cls:                ty.Type[enum.StrEnum],
        pd_info_comment:        bool,
        data_name_2_enum_name:  ty.Callable[[str], str],
        start_line_patch:       str,
        end_line_patch:         str,
        path_2_file:            str,
) -> int:
    if p02.data_mismatch(df, col_cls) == 0:
        return 0

    line_s = p00.gen_col_cls_lines(
        df,
        col_cls.__name__,
        pd_info_comment,
        data_name_2_enum_name,
    )

    p03.self_patch(
        path_2_file=path_2_file,
        trg_start_line=start_line_patch,
        trg_end_line=end_line_patch,
        patch_line_s=line_s,
    )
    return 1


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    pass
