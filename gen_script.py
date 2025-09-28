
import argparse
import pathlib as pl
import sys

import pandas as pd

sys.path.append(str(pl.Path(__file__).parent.parent))

import part_s.p03_tag_patch as p03
import part_s.p04_tag_col as p04
import part_s.p05_tag_fail as p05
import part_s.p06_tag_raise as p06
import part_s.p07_tag_load as p07
import part_s.p08_tag_setup as p08
import part_s.p09_tag_usage as p09


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
    parser.add_argument('-r', '--add_raise', default=True, action='store_false', help='not add raise after patch')

    args = parser.parse_args()

    the_sample = pl.Path(__file__).with_name('sample.py')

    output_stem = args.output_file[:-3] if args.output_file.endswith('.py') else args.output_file

    df = p07.sample_df if args.input_file is None else pd.read_csv(args.input_file)

    to_patch = {
        'tag_load':     p07.tag_load_lines(args.input_file, args.df_name),
        'tag_col':      p04.tag_col_lines(df, args.col_cls_name, args.no_info),
        'tag_fail':     p05.tag_fail_lines('%lineno'),
        'tag_raise':    p06.tag_raise_lines('%lineno', False),
        'tag_setup':    p08.tag_setup_lines(args.df_name, args.col_cls_name, args.no_info, args.add_raise),
        'tag_usage':    p09.tag_usage_lines(output_stem, args.df_name, args.col_cls_name),
    }

    line_s = p03.tag_patch(before=the_sample.read_text().split('\n'), to_replace=to_patch)

    args.output = args.output_file if args.output_file.endswith('.py') else f'{args.output_file}.py'
    with open(args.output, 'w') as out:
        out.write('\n'.join(line_s))
