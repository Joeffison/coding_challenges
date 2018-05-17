#!/usr/bin/python3
import os
import sys
import math
import pandas as pd

# Allowable names for voltage, current, and power factor
V_NAMES = {'v', 'V', 'Volts', 'Voltage'}
I_NAMES = {'i', 'I', 'Amps', 'Amperes', 'Current'}
PF_NAMES = {'pf', 'PF', 'Power Factor'}

DICT_ORIENT = 'index'
CALCULATED_COLUMNS = ['s', 'p', 'q']
DEFAULT_POWER_FACTOR = 0.9


def calc_power(volts, amps, pf):
  """
    Returns tuple of (p, q, s) powers from the inputs.
  """
  try:
    s = volts * amps
    p = s * pf
    q = math.sqrt(s**2 - p**2)
    return (p, q, s)
  except (ValueError, TypeError):
    return (None, None, None)


def combine_columns(allowed_columns):
  """
    Combines Columns which were named with multiple names
    :return: column with the appropriate values
  """

  v_columns = [v for v in allowed_columns if v in df.columns]
  v_columns.sort()
  for i in range(1, len(v_columns)):
    df[v_columns[0]] = df[v_columns[0]].fillna(df[v_columns[i]])
    df.drop(v_columns[i], 1, inplace=True)
  return v_columns[0]

def __get_file_path(f):
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  return os.path.join(__location__, f)

# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
  # Firstly, we gather the data in the JSON file
  f = __get_file_path(sys.argv[1])
  df = pd.read_json(f, orient=DICT_ORIENT)
  # print(df)

  # Then reduce the columns to just one allowed column per *quantity* (measurement)
  v = combine_columns(V_NAMES)
  i = combine_columns(I_NAMES)
  pf = combine_columns(PF_NAMES)
  # print(df)

  # Filling missing values for Power Factor to default
  df[pf] = df[pf].fillna(DEFAULT_POWER_FACTOR)
  # print(df)

  # Create the columns for the *calculated quantities* (namely apparent power, real power and reactive power)
  df[CALCULATED_COLUMNS] = df.apply(lambda x: pd.Series(calc_power(x[v], x[i], x[pf])), axis=1)
  # print(df)

  # and finally output the result
  print(df[CALCULATED_COLUMNS].to_dict(DICT_ORIENT))
