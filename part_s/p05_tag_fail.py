

def line_for_tag_fail(lineno: str) -> str:
    arg_line = f'lyckyd.check failed - File "{{__file__}}", line {lineno} patched'
    return f'    raise SystemExit(f\'{arg_line}\')  # tag_fail'


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    print(line_for_tag_fail(str(5)))
