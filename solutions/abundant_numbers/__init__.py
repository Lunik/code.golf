import os
import cProfile
import pstats

# Score : 77 bytes, 77 chars
def main():
  for i in range(1,201):
    if sum([j for j in range(1,i) if i%j==0])>i:print(i)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
