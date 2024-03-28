import sys
# for item in sys.argv:
#     print(sys.argv)

import argparse
# def main():
#     parser = argparse.ArgumentParser(
#         description='My first command-line tool, I guess!'
#     )
#     parser.parse_args()

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', is_flag=True, help='Produce more output')
@click.pass_context
def main(ctx, verbose):
    """ A Tool that deals with filesystems """
    return

@main.command()
@click.argument('size', type=int)
@click.pass_context
def lvm(ctx, size):
    # if size > 50:
    #     print('Got a large-enough size!')
    # else:
    #     print('Size of %s might not be enough for this operation' % size)

    print('Parent params: %s' % ctx.parent.params)
    print('Current params: %s' % ctx.params)


if __name__ == '__main__':
    main()