

def tag_patch(
        before:                 list[str],
        to_replace:             dict[str, list[str]],       # use %lineno - if str required specific lineno
) -> list[str]:

    now: list[str] = []

    tag_s = tuple(to_replace.keys())

    lineno_old, lineno_new = 0, 0
    while lineno_old < len(before):
        line = before[lineno_old]

        if not line.endswith(tag_s):                                    # just add old_line to new_file
            now.append(line)
            lineno_old += 1
            lineno_new += 1
            continue

        the_tag = [tag for tag in tag_s if line.endswith(tag)][0]       # define a the_tag
        while lineno_old < len(before) and before[lineno_old].endswith(the_tag):
            lineno_old += 1                                             # skip old sequence of the_tag

        for p_line in to_replace[the_tag]:
            now.append(p_line.replace('%lineno', str(lineno_new + 1)))
            lineno_new += 1

        to_replace.pop(the_tag)                                         # remove the_tag
        tag_s = tuple(to_replace.keys())

    return now


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    import pathlib as pl

    this_file = pl.Path(__file__)
    this_file_lines = this_file.read_text().split('\n')

    patched_lines = tag_patch(
        before=this_file_lines,
        to_replace={
            'tag2patch': ['    # new_1  # tag2patch', '    # new_2  # tag2patch', ],
            'tag_with_lineno': ['    # this line_number= %lineno  # tag_with_lineno'],
        }
    )

    this_file.write_text('\n'.join(patched_lines))

    # start ####
    # old                   # tag2patch
    # this line_number= 55  # tag_with_lineno
    # end ######
