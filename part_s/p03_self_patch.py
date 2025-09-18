
import pathlib as pl


def self_patch(
        path_2_file:    str,
        trg_start_line: str,
        trg_end_line:   str,
        patch_line_s:   list[str],
):

    caller_file = pl.Path(path_2_file)
    old: list[str] = caller_file.read_text().split('\n')
    now: list[str] = []

    patching_on = 0
    for line in old:
        if patching_on and not line.startswith(trg_end_line):
            continue
        patching_on = 0

        if line.startswith(trg_start_line):
            patching_on = 1
            now.append(line)
            now.extend(patch_line_s)
            continue
        
        now.append(line)

    caller_file.write_text('\n'.join(now))


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################

    self_patch(
        path_2_file=__file__,
        trg_start_line='    # start',
        trg_end_line='    # end',
        patch_line_s=['    # new_00', '    # new_01']
    )

    # start ####
    # old
    # end ######
