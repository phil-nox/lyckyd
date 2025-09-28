

def tag_raise_lines(lineno: str, uncomment: bool) -> list[str]:
    arg_line = (f'File "{{__file__}}", line {lineno} patched. '
                f'Remove/comment this line if the patch is valid.')
    start = '' if uncomment else '# '
    return [f'{start}raise SystemExit(f\'{arg_line}\')  # tag_raise']


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    print(tag_raise_lines(str(7), True))
