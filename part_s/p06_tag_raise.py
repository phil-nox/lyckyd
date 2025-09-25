

def line_for_tag_raise(lineno: str) -> str:
    arg_line = (f'File "{{__file__}}", line {lineno} patched. '
                f'Remove/comment this line if the patch is valid.')
    return f'raise SystemExit(f\'{arg_line}\')  # tag_raise'


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    print(line_for_tag_raise(str(7)))
