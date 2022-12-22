import traceback

# Explores the degree of similarity of follow through bars for any given bar on the chart


class ChanceSimilar:
    def __init__(self) -> None:
        pass

    def explore(self, bars):
        try:
            for b in range(0, len(bars) - 1):
                if bars[b].direction == bars[b + 1].direction:
                    psim = bars[b].percentSimilarToBar(bars[b + 1])

                    if psim:
                        print(f"{bars[b].barTime} {psim}")
                else:
                    print(f"{bars[b].barTime} 0")

        except:
            print(traceback.format_exc())
