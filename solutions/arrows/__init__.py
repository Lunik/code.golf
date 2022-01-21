import os
import cProfile
import pstats

# Score : 274 bytes, 214 chars
def main():
  import sys
  p=print
  r=range(-1,2)
  a=[[i,j] for i in r for j in r]
  _=" "*4
  b=f"↙←↖↓↔↑↘→↗↲⇐↰⇓↕⇑↳⇒↱⇙⇦⇖⇩⇔⇧⇘⇨⇗{_}⇕{_*2}⥀{_*2}⥁"
  s=(0,0)
  for arg in sys.argv[1:]:
    s=tuple(map(sum,zip(s,a[b.index(arg)%9])))
    p("%s %s"%s)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
