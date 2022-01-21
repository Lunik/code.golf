import os
import cProfile
import pstats

# Score : 90 bytes, 90 chars
def main():
  for i in range(1,201):
    (lambda _:_,print)[sum([(j,0)[i%j!=0] for j in range(1,i)])>i](i)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
