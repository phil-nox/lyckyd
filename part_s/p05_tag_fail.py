

def tag_fail_lines(lineno: str) -> list[str]:
    arg_line = f'lyckyd.check failed - File "{{__file__}}", line {lineno} patched'
    return [f'    raise SystemExit(f\'{arg_line}\')  # tag_fail']


# sample and/or test code below ###############################################
if __name__ == '__main__':  # #################################################
    print(tag_fail_lines(str(5)))
