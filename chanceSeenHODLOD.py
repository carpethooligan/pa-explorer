import traceback

# Explores the probability of having seen either HOD or LOD for every 5 min bar of a day session in the ES
# walks through all the bars of a day and records whether HOD/LOD held until EOD
class SeenHODLOD:
    def __init__(self) -> None:
        pass

    def explore(self, bars):
        try:
            # records whether on this day a new HOD or LOD was seen after each bar's range
            resultsByBarIndx = {}

            if not bars:
                print("Bars object is empty!")
                return

            # initial HOD/LOD are set using the first bar of the day
            hod = bars[0].high
            lod = bars[0].low

            for i, bar in enumerate(bars):

                brokeHOD = False
                brokeLOD = False

                # update new HOD/LOD if this bar set either one
                hod = max(hod, bar.high)
                lod = min(lod, bar.low)

                # scan forward and record whether price broke to new HOD/LOD
                barsAboveHOD = [
                    b for b in bars if b.barTime > bar.barTime and b.high > hod
                ]
                barsBelowLOD = [
                    b for b in bars if b.barTime > bar.barTime and b.low < lod
                ]

                if barsAboveHOD:
                    brokeHOD = True

                if barsBelowLOD:
                    brokeLOD = True

                # if haven't broken HOD or LOD then one of them held so this bar is recorded as true, otherwise false
                resultsByBarIndx[i] = (
                    True
                    if (not brokeHOD or not brokeLOD)
                    else False
                )

            return resultsByBarIndx

        except:
            print(traceback.format_exc())
 
        return resultsByBarIndx
