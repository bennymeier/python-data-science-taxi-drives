import pandas as pd
import glob
import os
import matplotlib.pyplot as plt


class TaxiTrips:
    def __init__(self, path="test"):
        self.frame = None
        self.path = path
        self.initFrame()

    def initFrame(self):
        path = r'test'
        all_files = glob.glob(os.path.join(path, "*.txt"))
        print("Files used: \n", all_files)

        li = []
        for current_file in all_files:
            df = pd.read_csv(current_file, index_col=None,
                             header=0, delimiter="|", encoding="utf-8")
            li.append(df)
        self.frame = pd.concat(li, axis=0, ignore_index=True)

    def getInfo(self):
        print(self.frame.info())

    # Durchschnittliche Stecke in Miles
    def get_mean_mileage(self):
        col_mileage = self.frame["MILEAGE"]
        mean_mileage = col_mileage.mean()
        print("Durchschnittliche Strecke: ", round(mean_mileage, 2), "m")

    # Durchschnittlicher Preis
    def get_mean_amont_per_drive(self):
        col_totalamount = self.frame["TOTALAMOUNT"]
        mean_totalamount = col_totalamount.mean()
        print("Durchschnittlicher Preis pro Strecke: ",
              round(mean_totalamount, 2), "$")

    # Weiteste Strecke
    def get_furthest_way(self):
        col_mileage = self.frame["MILEAGE"]
        max_mileage = col_mileage.max()
        print("Weiteste Strecke: ", round(max_mileage, 2), "m")

    # Teuerste Fahrt
    def get_most_expensive_drive(self):
        col_totalamount = self.frame["TOTALAMOUNT"]
        max_totalamount = col_totalamount.max()
        print("Teuerste Fahrt: ", round(max_totalamount, 2), "$")

    # Alle Providernames, duplikate entfernt
    def get_distinct_providernames(self):
        col_providernames = self.frame["PROVIDERNAME"]
        distinct_providernames = col_providernames.drop_duplicates()
        print("Alle Providernames:\n", distinct_providernames)

    # Meisten Fahrten an einem Datum
    def get_date_of_most_trips(self):
        col_origindate = self.frame["ORIGINDATETIME_TR"]
        origindate_most_drives = col_origindate.value_counts()
        col_destinationdate = self.frame["DESTINATIONDATETIME_TR"]
        destinationdate_most_drives = col_destinationdate.value_counts()
        print("Meistes Datum/Uhrzeit Abfahrt:\n", origindate_most_drives)
        print("Meistes Datum/Uhrzeit Ankunft:\n", destinationdate_most_drives)


Trips = TaxiTrips()
# Trips.getInfo()
Trips.get_mean_mileage()
Trips.get_mean_amont_per_drive()
Trips.get_furthest_way()
Trips.get_most_expensive_drive()
Trips.get_distinct_providernames()
Trips.get_date_of_most_trips()
