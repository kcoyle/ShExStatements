#
# SPDX-FileCopyrightText: 2020 John Samuel <johnsamuelwrites@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import csv
import re
from shexstatements.shexstatementsparser import ShExStatementLexerParser

class CSV:
  def generate_shex_from_csv(filepath, delim=","):
    pattern = '\s*'
    data = ""
    with open(filepath, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=delim)
     for row in csvreader:
       line = ""
       for value in row:
         if value and re.search(pattern, value):
           if not line:
             line = value
           else:
             line = line + "|" + value
       data = data + line
    lexerparser = ShExStatementLexerParser()
    lexerparser.build()
    lexerparser.buildparser()
    tokens = lexerparser.input(data)
    result = lexerparser.parse(data)
    shexstatement = result.generate_shex()
    return shexstatement

