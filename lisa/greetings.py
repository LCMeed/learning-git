import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-n", "--name", type=str, help="The name to greet.")
args = parser.parse_args()

name = args.name
if not name:
  name = "there"

if args.verbose:
    print(f"Hello {name}! How's it going?")
else:
    print(f"Hi {name}.")

