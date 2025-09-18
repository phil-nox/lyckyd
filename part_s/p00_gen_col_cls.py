
import datetime as dt
import io
import typing as ty

import pandas as pd


def gen_col_cls_lines(
        df:                     pd.DataFrame,
        name_for_col_cls:       str,
        pd_info_comment:        bool,
        data_name_2_enum_name:  ty.Callable[[str], str] = lambda x: x.lower().replace(' ', '_'),
) -> list[str]:

    rlt: list[str] = [f'class {name_for_col_cls}(enum.StrEnum):']

    for col in list(df.columns):
        code_like = data_name_2_enum_name(col)  # case df.columns = ['Top', 'top'] -> ['top', 'top']?
        rlt.append(f"    {code_like} = '{col}'")

    if not pd_info_comment:
        return rlt

    info_df = io.StringIO()
    df.info(buf=info_df)
    shift: int = max(map(len, rlt)) + 2     # 2 space before comment
    shift += 4 - shift % 4                  # n * tab size

    rlt_adv = []
    for c_part, i_part in zip(['', '', '', '', *rlt, '', ''], info_df.getvalue().split('\n')):
        rlt_adv.append(
            f'{c_part:<{shift}}# {i_part}'.replace("#  ", "# ", 1).replace("# -", "# ", 1)
        )

    rlt_adv.append(f'{"":<{shift}}#')
    rlt_adv.append(f'{"":<{shift}}# {dt.datetime.now(dt.timezone.utc)}')
    return rlt_adv


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    the_df: pd.DataFrame = pd.DataFrame({
        'planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'radius_km': [2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622],
    })

    line_s = gen_col_cls_lines(the_df, 'F', pd_info_comment=True)
    [print(el) for el in line_s]
