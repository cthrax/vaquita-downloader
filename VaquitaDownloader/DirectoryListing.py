class DirectoryListing:
    def __init__(self):
        self.buffer = []
        self.filenames = []

    def add_bytes(self, block: str):
        self.buffer.append(block)

    def assemble(self):
        for line in self.buffer:
            cols = line.split()
            if len(cols) > 1:
                self.filenames.append(cols[-1])


if __name__ == "__main__":
    d = DirectoryListing()
    example = '''-rwxr-xr-x    1 0        0          354069 May 03  2022 LOG10.csv
-rwxr-xr-x    1 0        0           38968 Dec 09 22:39 LOG100.csv
-rwxr-xr-x    1 0        0          383553 Dec 09 23:33 LOG101.csv
-rwxr-xr-x    1 0        0            6397 Dec 09 23:40 LOG102.csv
-rwxr-xr-x    1 0        0            3877 Dec 10 00:45 LOG103.csv
-rwxr-xr-x    1 0        0           28945 Dec 10 01:21 LOG104.csv
-rwxr-xr-x    1 0        0           14688 Dec 10 01:23 LOG105.csv
-rwxr-xr-x    1 0        0           25541 Dec 10 02:11 LOG106.csv
-rwxr-xr-x    1 0        0            6951 Dec 30 16:12 LOG107.csv
-rwxr-xr-x    1 0        0            8190 May 03  2022 LOG11.csv
-rwxr-xr-x    1 0        0           55512 May 03  2022 LOG12.csv
-rwxr-xr-x    1 0        0           62622 May 03  2022 LOG13.csv
-rwxr-xr-x    1 0        0           23868 May 03  2022 LOG14.csv
-rwxr-xr-x    1 0        0          307460 May 03  2022 LOG15.csv
-rwxr-xr-x    1 0        0           75032 May 04  2022 LOG16.csv
-rwxr-xr-x    1 0        0            1635 May 04  2022 LOG17.csv
-rwxr-xr-x    1 0        0           27015 May 04  2022 LOG18.csv
-rwxr-xr-x    1 0        0             292 May 04  2022 LOG19.csv
-rwxr-xr-x    1 0        0           25744 May 04  2022 LOG20.csv
-rwxr-xr-x    1 0        0           31678 May 04  2022 LOG21.csv
-rwxr-xr-x    1 0        0         1844317 May 04  2022 LOG22.csv
-rwxr-xr-x    1 0        0            4028 May 04  2022 LOG23.csv
-rwxr-xr-x    1 0        0           29126 Nov 25 23:59 LOG24.csv
-rwxr-xr-x    1 0        0           43958 Nov 26 00:05 LOG25.csv
-rwxr-xr-x    1 0        0            2151 Nov 26 03:57 LOG26.csv
-rwxr-xr-x    1 0        0           72028 Nov 26 04:07 LOG27.csv
-rwxr-xr-x    1 0        0           38916 Nov 26 04:18 LOG28.csv
-rwxr-xr-x    1 0        0            1220 Nov 27 13:58 LOG29.csv
-rwxr-xr-x    1 0        0          421304 Nov 27 15:59 LOG30.csv
-rwxr-xr-x    1 0        0            2309 Nov 27 21:25 LOG31.csv
-rwxr-xr-x    1 0        0           28861 Nov 27 21:59 LOG32.csv
-rwxr-xr-x    1 0        0           74895 Nov 28 12:01 LOG33.csv
-rwxr-xr-x    1 0        0          538356 Nov 28 15:32 LOG34.csv
-rwxr-xr-x    1 0        0          170204 Nov 28 15:53 LOG35.csv
-rwxr-xr-x    1 0        0         1006125 Nov 28 19:49 LOG36.csv
-rwxr-xr-x    1 0        0             696 Nov 28 20:30 LOG37.csv
-rwxr-xr-x    1 0        0           28149 Nov 28 20:49 LOG38.csv
-rwxr-xr-x    1 0        0           74885 Nov 28 21:12 LOG39.csv
-rwxr-xr-x    1 0        0           23752 Nov 29 01:40 LOG40.csv
-rwxr-xr-x    1 0        0          579015 Nov 29 19:45 LOG41.csv
-rwxr-xr-x    1 0        0          747154 Nov 29 22:20 LOG42.csv
-rwxr-xr-x    1 0        0           31189 Nov 29 22:43 LOG43.csv
-rwxr-xr-x    1 0        0           75036 Nov 30 00:07 LOG44.csv
-rwxr-xr-x    1 0        0         1505536 Nov 30 15:34 LOG45.csv
-rwxr-xr-x    1 0        0            1073 Nov 30 15:35 LOG46.csv
-rwxr-xr-x    1 0        0           75014 Nov 30 16:27 LOG47.csv
-rwxr-xr-x    1 0        0          503282 Nov 30 20:38 LOG48.csv
-rwxr-xr-x    1 0        0            1718 Nov 30 20:38 LOG49.csv
-rwxr-xr-x    1 0        0           41299 Nov 30 21:54 LOG50.csv
-rwxr-xr-x    1 0        0           30551 Nov 30 22:17 LOG51.csv
-rwxr-xr-x    1 0        0          745869 Dec 01 15:09 LOG52.csv
-rwxr-xr-x    1 0        0           75030 Dec 01 16:09 LOG53.csv
-rwxr-xr-x    1 0        0          593088 Dec 01 19:53 LOG54.csv
-rwxr-xr-x    1 0        0            7018 Dec 02 00:00 LOG55.csv
-rwxr-xr-x    1 0        0           26786 Dec 02 00:12 LOG56.csv
-rwxr-xr-x    1 0        0           75062 Dec 02 00:40 LOG57.csv
-rwxr-xr-x    1 0        0          481593 Dec 02 13:43 LOG58.csv
-rwxr-xr-x    1 0        0          504475 Dec 02 15:32 LOG59.csv
-rwxr-xr-x    1 0        0            1476 Dec 02 23:06 LOG60.csv
-rwxr-xr-x    1 0        0           26353 Dec 02 23:19 LOG61.csv
-rwxr-xr-x    1 0        0           75195 Dec 03 00:02 LOG62.csv
-rwxr-xr-x    1 0        0          465854 Dec 03 13:34 LOG63.csv
-rwxr-xr-x    1 0        0          155877 Dec 03 13:56 LOG64.csv
-rwxr-xr-x    1 0        0          598534 Dec 03 18:46 LOG65.csv
-rwxr-xr-x    1 0        0          515334 Dec 03 20:25 LOG66.csv
-rwxr-xr-x    1 0        0           75094 Dec 03 21:10 LOG67.csv
-rwxr-xr-x    1 0        0            2429 Dec 03 23:11 LOG68.csv
-rwxr-xr-x    1 0        0           28362 Dec 03 23:40 LOG69.csv
-rwxr-xr-x    1 0        0           75298 Dec 03 23:51 LOG70.csv
-rwxr-xr-x    1 0        0          531969 Dec 04 15:05 LOG71.csv
-rwxr-xr-x    1 0        0          583450 Dec 04 19:40 LOG72.csv
-rwxr-xr-x    1 0        0            2414 Dec 04 20:42 LOG73.csv
-rwxr-xr-x    1 0        0           25241 Dec 04 21:05 LOG74.csv
-rwxr-xr-x    1 0        0           75014 Dec 05 00:10 LOG75.csv
-rwxr-xr-x    1 0        0          819485 Dec 06 15:14 LOG76.csv
-rwxr-xr-x    1 0        0           75090 Dec 06 16:26 LOG77.csv
-rwxr-xr-x    1 0        0          732340 Dec 06 20:07 LOG78.csv
-rwxr-xr-x    1 0        0            1095 Dec 07 00:14 LOG79.csv
-rwxr-xr-x    1 0        0            1212 May 03  2022 LOG8.csv
-rwxr-xr-x    1 0        0           26013 Dec 07 00:39 LOG80.csv
-rwxr-xr-x    1 0        0           75032 Dec 07 01:21 LOG81.csv
-rwxr-xr-x    1 0        0          431261 Dec 07 15:03 LOG82.csv
-rwxr-xr-x    1 0        0            1214 Dec 07 15:12 LOG83.csv
-rwxr-xr-x    1 0        0           74743 Dec 07 15:31 LOG84.csv
-rwxr-xr-x    1 0        0          732313 Dec 07 19:43 LOG85.csv
-rwxr-xr-x    1 0        0            8264 Dec 08 01:26 LOG86.csv
-rwxr-xr-x    1 0        0           45114 Dec 08 02:21 LOG87.csv
-rwxr-xr-x    1 0        0           74979 Dec 08 02:32 LOG88.csv
-rwxr-xr-x    1 0        0           75173 Dec 08 11:24 LOG89.csv
-rwxr-xr-x    1 0        0          473981 May 03  2022 LOG9.csv
-rwxr-xr-x    1 0        0            2669 Dec 08 13:27 LOG90.csv
-rwxr-xr-x    1 0        0          511076 Dec 08 15:06 LOG91.csv
-rwxr-xr-x    1 0        0           75107 Dec 08 16:21 LOG92.csv
-rwxr-xr-x    1 0        0          535421 Dec 08 19:41 LOG93.csv
-rwxr-xr-x    1 0        0           75655 Dec 09 01:09 LOG94.csv
-rwxr-xr-x    1 0        0           59227 Dec 09 14:23 LOG95.csv
-rwxr-xr-x    1 0        0           10309 Dec 09 14:39 LOG96.csv
-rwxr-xr-x    1 0        0          616638 Dec 09 19:52 LOG97.csv
-rwxr-xr-x    1 0        0           77581 Dec 09 20:03 LOG98.csv
-rwxr-xr-x    1 0        0           85629 Dec 09 22:33 LOG99.csv

    '''
    d.add_bytes(example)
    d.assemble()

    print(d.filenames)
