
import enum
import typing as ty
import pathlib as pl

import pandas as pd

import lyckyd.part_s.p02_self_patch as p02
import lyckyd.part_s.p03_check_df as p03
import lyckyd.part_s.p04_tag_col as p04
import lyckyd.part_s.p05_tag_fail as p05
import lyckyd.part_s.p06_tag_raise as p06


def check_n_tag_patch(
        df:                     pd.DataFrame,
        col_cls:                ty.Type[enum.StrEnum],
        pd_info_comment:        bool,
        add_raise_after_patch:  bool,
        data_name_2_enum_name:  ty.Callable[[str], str],
        path_2_file:            str,
) -> int:
    if p03.data_mismatch(df, col_cls) == 0:
        return 0

    target_file = pl.Path(path_2_file)

    line_s = p04.gen_col_cls_lines(
        df,
        col_cls.__name__,
        pd_info_comment,
        data_name_2_enum_name,
    )

    to_patch = {
        'tag_col': line_s,
        'tag_fail': [p05.line_for_tag_fail('%lineno')],
    }

    if add_raise_after_patch:
        to_patch['tag_raise'] = [p06.line_for_tag_raise('%lineno')]

    patched_lines = p02.tag_patch(before=target_file.read_text().split('\n'), to_replace=to_patch)

    target_file.write_text('\n'.join(patched_lines))

    return 1


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    pass
