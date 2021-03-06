#
# SPDX-FileCopyrightText: 2020 John Samuel <johnsamuelwrites@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import argparse
from shexstatements.shexfromcsv import CSV
from shexstatements.shexjfromcsv import ShExJCSV
from shexstatements.shexfromapplprofilecsv import ApplicationProfile


parser = argparse.ArgumentParser(prog='shexstatements')
parser.add_argument('-o','--output', type=str, help='output file')
parser.add_argument('-ap','--applicationprofile', action='store_true', help='input is application profile')
parser.add_argument('-d','--delimiter', type=str, help='output file')
parser.add_argument('-s', '--skipheader', action='store_true', help='Skip CSV header')
parser.add_argument('-j', '--shexj', action='store_true', help='Generate ShExJ')
parser.add_argument('csvfile', type=str, help='path of CSV file')
skipheader = False
delimiter=","

args = parser.parse_args()
if args.skipheader:
  skipheader = args.skipheader
if args.delimiter:
  delimiter = args.delimiter

if args.applicationprofile:
  shexstatement = ApplicationProfile.generate_shex_from_csv(args.csvfile, delim=delimiter, skip_header=skipheader)
  if args.shexj:
    shexstatement = ShExJCSV.generate_shexj_from_shexstament(shexstatement)
else:
  shexstatement = CSV.generate_shex_from_csv(args.csvfile, delim=delimiter, skip_header=skipheader)
  if args.shexj:
    shexstatement = ShExJCSV.generate_shexj_from_csv(args.csvfile, delim=delimiter, skip_header=skipheader)

if args.output:
  with open(args.output, 'w') as shexfile:
    shexfile.write(shexstatement)
else:
  print(shexstatement)
