import os
import cProfile
import pstats


# Score : 144 bytes, 144 chars
def main():
  p=print
  r=range
  j=' '.join
  m=map
  p('  ',j(m(str, r(2, 8)))+'\n','-'*13)
  for x in r(16):p("%X"%x+': '+j((list(m(chr,r(32,127)))+['DEL'])[x::16]))


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
