

def tag_setup_lines(
        name_for_df:            str,
        name_for_col_cls:       str,
        pd_info_comment:        bool,
        add_raise_after_patch:  bool,
) -> list[str]:

    return [
        f'    df={name_for_df},',
        f'    col_cls={name_for_col_cls},',
        f'    pd_info_comment=True,' if pd_info_comment else f'    pd_info_comment=False,',
        f'    add_raise_after_patch=True,' if add_raise_after_patch else f'    add_raise_after_patch=False,',
    ]


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    rlt = tag_setup_lines(
        name_for_df='test_df',
        name_for_col_cls='TestC',
        pd_info_comment=True,
        add_raise_after_patch=False,
    )
    [print(el) for el in rlt]
