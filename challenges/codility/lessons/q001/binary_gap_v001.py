#!/usr/bin/env python3


def solution(n):
  """
  Given a positive integer N,
  returns the length of its longest binary gap.
  """

  # possible states (START state is necessary to ignore trailing zeros)
  START = -1
  LAST_SAW_ONE = 1
  LAST_SAW_ZERO = 0

  current_state = START

  # we move the bit mask's bit one position at a time,
  # so we can iterate over all bits in n
  bit_mask = 0x00000001

  max_gap = 0
  loop_gap = 0

  # in other programming languages,
  # we would check for integer overflow bit_mask > 0,
  # but as in Python we won't ever reach it,
  # we can (easily) just check if the bit mask is off the range of n itself: bit_mask <= n
  while bit_mask <= n:
    # When we do a Bitwise AND with a bit mask containing only one 1,
    # we can tell if the bit in the same position in N is 0 or 1
    if n & bit_mask == 0:
      if current_state is not START:
        current_state = LAST_SAW_ZERO
        loop_gap += 1
    else:
      current_state = LAST_SAW_ONE
      if loop_gap > max_gap:
        max_gap = loop_gap
      loop_gap = 0

    # we now use a left shift to move the bit 1 one position to the left
    bit_mask <<= 1

  return max_gap
