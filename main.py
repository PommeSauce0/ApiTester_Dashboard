from argparse import ArgumentParser
from api_dashboard import app


if __name__ == '__main__':
    ap = ArgumentParser(prog='ApiTester Dashboard',
                        description='A dashboard to to analyze the results from ApiTester.',
                        epilog='Developed with Flask')
    ap.add_argument('-D', '--debug', action='store_true', dest='debug', help='Use debug mode (default: False')
    args = ap.parse_args()

    app.run(debug=args.debug)
