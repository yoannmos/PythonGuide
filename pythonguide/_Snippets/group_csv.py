import os
import glob
import pandas as pd


def groupcsv(my_dir, col1, col2, arrondi):
    """
    Blabla
    """
    filelist = []
    os.chdir(my_dir)
    for files in glob.glob("*.csv"):
        filelist.append(files)
    # filelist
    dat = pd.concat(
        [
            (
                pd.read_csv(
                    (my_dir + "\\" + f),
                    skiprows=1,
                    na_values=["NA"],
                    converters={col1: float, col2: float},
                ).T
            )
            for f in filelist
        ],
        keys=filelist,
    ).T
    dat = round(dat, arrondi)
    dat.to_csv("Group.txt")
    return dat.head()


DIR = r"mydir\Table.csv"
COL1 = "(V)"
COL2 = "(ms)"
ARRONDI = 3
groupcsv(DIR, COL1, COL2, ARRONDI)
