
import argparse
import pathlib as pl
import sys

sys.path.append(str(pl.Path(__file__).parent.parent))

import lyckyd.part_s.p01_gen_file as p01


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='lyckyd',
        description='let your code knows your data',
    )

    parser.add_argument('-i', '--input_file', default=None, help='path to target .csv file')
    parser.add_argument('-o', '--output_file', default='output.py', help='code generation output file')
    parser.add_argument('-d', '--df_name', default='df', help='name for dataframe in generation code')
    parser.add_argument('-c', '--col_cls_name', default='C', help='name for columns class in generation code')
    parser.add_argument('-n', '--no_info', default=True, action='store_false', help='not include df.info as comments')

    args = parser.parse_args()

    lines = p01.generate_script_code(
        path_to_csv=args.input_file,
        output_file_name=args.output_file,
        name_for_df=args.df_name,
        name_for_col_cls=args.col_cls_name,
        pd_info_comment=args.no_info,
    )

    args.output = args.output_file if args.output_file.endswith('.py') else f'{args.output_file}.py'
    with open(args.output_file, 'w') as out:
        out.write(lines)
