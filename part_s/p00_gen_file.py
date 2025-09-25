
import pandas as pd

import lyckyd.part_s.p02_self_patch as p02
import lyckyd.part_s.p04_tag_col as p04
import lyckyd.part_s.p05_tag_fail as p05


def generate_script_code(
        path_to_csv:            str | None = None,
        output_file_name:       str = 'output',
        name_for_df:            str = 'df',     # as default name for pd.DataFrame
        name_for_col_cls:       str = 'C',      # C for Columns
        pd_info_comment:        bool = True,
        add_raise_after_patch:  bool = True,
):

    code_line_s: list[str] = []

    # imports ##########################################################################################################
    code_line_s.extend(['', 'import enum', '', 'import pandas as pd', '', 'import lyckyd', ''])

    # read data ########################################################################################################
    code_line_s.append('# load ##############################################################')
    if path_to_csv is not None:
        code_line_s.append(f'{name_for_df} = pd.read_csv("{path_to_csv}")')

        df = pd.read_csv(path_to_csv)
    else:
        code_line_s.append(f'{name_for_df} = pd.DataFrame({{')
        code_line_s.append(f'    "planet": ["Earth", "Mars"],')
        code_line_s.append(f'    "radius_km": [6371, 3390],')
        code_line_s.append(f'    # "count": [3, 4],        # uncomment & run')
        code_line_s.append(f'}})')

        df = pd.DataFrame({'planet': ['Earth', 'Mars'], 'radius_km': [6371, 3390]})
    code_line_s.append('')

    # modification #####################################################################################################
    code_line_s.append('# modification ######################################################')
    code_line_s.append(f'# {name_for_df}["new_col"] = 0')
    code_line_s.append('')

    # gen class ########################################################################################################
    code_line_s.append('')
    code_line_s.append('# columns ###########################################################')

    cls_lines = p04.gen_col_cls_lines(df, name_for_col_cls, pd_info_comment)
    cls_lines_with_tag = p02.self_patch(before=['tag_col'], to_replace={'tag_col': cls_lines})
    code_line_s.extend(cls_lines_with_tag)

    code_line_s.append(' ' * (len(code_line_s[-1]) - len('# tag_col')) + '# tag_raise')

    code_line_s.append('')
    code_line_s.append('')

    # self_patch #######################################################################################################
    code_line_s.append('# check and self_patch ##############################################')

    args = [
        f'    df={name_for_df},',
        f'    col_cls={name_for_col_cls},',
        f'    pd_info_comment=' + ('True,' if pd_info_comment else 'False,'),
        f'    add_raise_after_patch=' + ('True,' if add_raise_after_patch else 'False,'),
        f'    data_name_2_enum_name=lambda x: x.lower().replace(" ", "_"),',
        f'    path_2_file=__file__,',
    ]

    code_line_s.append(f'if lyckyd.check_n_self_patch(')
    code_line_s.extend(args)
    code_line_s.append(f'):')
    code_line_s.append(p05.line_for_tag_fail(str(len(code_line_s) + 1)))

    # __main__ #########################################################################################################
    output_file_name = output_file_name[:-3] if output_file_name.endswith('.py') else output_file_name

    code_line_s.append('')
    code_line_s.append('')
    code_line_s.append('# Usage (in other files) ######################################################')
    code_line_s.append("if __name__ == '__main__':  # #################################################")
    code_line_s.append('')
    code_line_s.append(f'    import {output_file_name}')
    code_line_s.append('')
    first_name_in_enum = df.columns[0].lower().replace(' ', '_')    # TODO create one source of truth - in gen_col_cls
    code_line_s.append(f'    foo = {output_file_name}.{name_for_df}'
                       f'[{output_file_name}.{name_for_col_cls}.{first_name_in_enum}]'
                       f'.unique()')
    code_line_s.append('    print(foo[:8])')

    # last_line ########################################################################################################
    code_line_s.append('')

    return '\n'.join(code_line_s)


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    txt = generate_script_code(
        path_to_csv=None,
        output_file_name='output',
        name_for_df='df',
        name_for_col_cls='F',
        pd_info_comment=True,
    )

    [print(line) for line in txt.split('\n')]
