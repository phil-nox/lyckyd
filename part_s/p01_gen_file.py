
import pandas as pd

import lyckyd.part_s.p00_gen_col_cls as p00


def generate_script_code(
        path_to_csv:            str | None = None,
        output_file_name:       str = 'output',
        name_for_df:            str = 'df',     # as default name for pd.DataFrame
        name_for_col_cls:       str = 'C',      # C for Columns
        pd_info_comment:        bool = True,
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
    code_line_s.extend(p00.gen_col_cls_lines(
        df,
        name_for_col_cls,
        pd_info_comment,
    ))
    code_line_s.append('# end_columns #######################################################')
    code_line_s.append('')
    code_line_s.append('')

    # self_patch #######################################################################################################
    code_line_s.append('# check and self_patch ##############################################')

    args = [
        f'    df={name_for_df},',
        f'    col_cls={name_for_col_cls},',
        f'    pd_info_comment=' + 'True,' if pd_info_comment else 'False,',
        f'    data_name_2_enum_name=lambda x: x.lower().replace(" ", "_"),',
        f'    start_line_patch="# columns #",',
        f'    end_line_patch="# end_columns #",',
        f'    path_2_file=__file__,',
    ]

    code_line_s.append(f'if lyckyd.check_n_self_patch(')
    code_line_s.extend(args)
    code_line_s.append(f'):')
    code_line_s.append(f'    raise SystemExit(f\'data_mismatch - {{__file__}} patched - Script ready to run again\')')

    # __main__ #########################################################################################################
    output_file_name = output_file_name[:-3] if output_file_name.endswith('.py') else output_file_name

    code_line_s.append('')
    code_line_s.append('')
    code_line_s.append('# Usage (in other files) ######################################################')
    code_line_s.append("if __name__ == '__main__':  # #################################################")
    code_line_s.append('')
    code_line_s.append(f'    from {output_file_name} import {name_for_df}, {name_for_col_cls}')
    code_line_s.append('')
    first_name_in_enum = df.columns[0].lower().replace(' ', '_')    # TODO create default func in gen_col_cls
    code_line_s.append(f'    foo = {name_for_df}[{name_for_col_cls}.{first_name_in_enum}].unique()')
    code_line_s.append('    print(foo[:8])')

    # last_line ########################################################################################################
    code_line_s.append('')

    return '\n'.join(code_line_s)


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    txt = generate_script_code(
        path_to_csv='../_planet.csv',
        output_file_name='output',
        name_for_df='df',
        name_for_col_cls='F',
        pd_info_comment=True,
    )

    [print(line) for line in txt.split('\n')]
