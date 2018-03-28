#!/usr/bin/env python3

import unittest

from challenges.spoj.sbank.sorting_bank_accounts_v001 import solution


class SortingBankAccountsTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(self.__format_solution(['03 10103538 2222 1233 6160 0141 1', '03 10103538 2222 1233 6160 0142 1',
                                             '30 10103538 2222 1233 6160 0141 2', '30 10103538 2222 1233 6160 0142 2']),
                     solution(['03 10103538 2222 1233 6160 0141', '03 10103538 2222 1233 6160 0142',
                               '30 10103538 2222 1233 6160 0141', '30 10103538 2222 1233 6160 0142',
                               '30 10103538 2222 1233 6160 0141', '30 10103538 2222 1233 6160 0142']))


  def __format_solution(self, response):
    return '\n'.join(response) + '\n\n'


if __name__ == '__main__':
  unittest.main()
