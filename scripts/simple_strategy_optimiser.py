__author__ = 'camzzz'

import sys
sys.path.append("D:\\APT_Game\\Blotto")
sys.path.append("D:\\APT_Game\\Blotto\\Strategies")
sys.path.append("D:\\APT_Game\\Blotto\\StrategyUtils")
sys.path.append("D:\\APT_Game\\Blotto\\scripts")


from Strategies import StaticStrategy
from StrategyUtils import StrategyRanker


def main():
    static_strat_list = []
    for i in range(0, 101, 1):
        for j in range(0, 101-i, 1):
            for k in range(j, 101-i-j):
                static_strat_list.append([i, j, k])

    strategies = []
    for s in static_strat_list:
        strategies.append(StaticStrategy('static_%s_1' % s, s, True))

    sr = StrategyRanker(strategies, num_fields=3, num_runs=1, total_score=True)
    sr.run()

    top_strats = sr.get_top_strategies(1)
    print(top_strats)


if __name__ == "__main__":
    main()