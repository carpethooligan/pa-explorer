import utils
import os
import traceback
from chanceSeenHODLOD import SeenHODLOD



def exploreChanceSeenHODLOD():
    try:

        shl = SeenHODLOD()

        filenames = utils.getAllDataFilenames()
        allResults = []
        for filename in sorted(filenames):

            # load bars from csv file
            bars = utils.getBarsFromDatafile(os.path.join("data", "ES", filename))

            if bars:
                dayResult = shl.explore(bars)
                if dayResult:
                    print(bars[0].barTime.date())
                    allResults.append(dayResult)

        # calculate chance of having seen HOD/LOD or every bar index over all days seen
        for b in range(0, 82):
            thisBarResults = []
            for day in allResults:
                if b in day:
                    thisBarResults.append(day[b])
            if len(thisBarResults) > 0:
                print(
                    f"Bar {b+1} {round(thisBarResults.count(True)/len(thisBarResults),2)*100}%"
                )
        print(f"Total days: {len(allResults)}")
    except:
        print(traceback.format_exc())


if __name__ == "__main__":
    exploreChanceSeenHODLOD()
