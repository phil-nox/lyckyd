

def tag_usage_lines(
        output_file_name:       str,
        name_for_df:            str,
        name_for_col_cls:       str,
) -> list[str]:

    return [
        f'    import {output_file_name}',
        f'',
        f'    foo = {output_file_name}.{name_for_df}[{output_file_name}.{name_for_col_cls}.planet].unique()',
        f'    print(foo[:8])',
    ]


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    rlt = tag_usage_lines(
        output_file_name='testout',
        name_for_df='test_df',
        name_for_col_cls='TestC',
    )
    [print(el) for el in rlt]
