import pandas as pd
import glob
import os
import matplotlib.pyplot as plt


class TaxiRoutes:
    def __init__(self, path="test"):
        self.frame = None
        self.path = path
        self.initFrame()

    def initFrame(self):
        path = r'test'
        all_files = glob.glob(os.path.join(path, "*.txt"))
        print(all_files)

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


Routes = TaxiRoutes()
# Routes.getInfo()
Routes.get_mean_mileage()
Routes.get_mean_amont_per_drive()
Routes.get_furthest_way()
Routes.get_most_expensive_drive()
# print(frame.info())
# col_totalamount = frame["TOTALAMOUNT"]
# max_totalamount = col_totalamount.max()
# median_toalamount = col_totalamount.median()
# all_columns = frame.columns
# col_providernames = frame["PROVIDERNAME"]
# distinct_providernames = frame.drop_duplicates(subset = ["PROVIDERNAME"])
# # print("Max: ", max_fareamount)
# # print("Median: ", median_fareamount)
# # print("Providernames: ", distinct_providernames)
# # print("Cols: ", list(all_columns))
# # print(frame)

# # Erkennen von Datenmustern, etwa zu welchen Tageszeiten oder Wochentagen die meisten Fahrten stattfinden
# col_origindate = frame["ORIGINDATETIME_TR"]
# origindate_most_drives = col_origindate.value_counts()
# col_destinationdate = frame["DESTINATIONDATETIME_TR"]
# destinationdate_most_drives = col_destinationdate.value_counts()
# print("Meistes Datum/Uhrzeit Abfahrt: ", origindate_most_drives)
# print("Meistes Datum/Uhrzeit Ankunft: ", destinationdate_most_drives)

# # Berechnen von Measures wie durchschnittlicher Fahrpreis, durchschnittliche Strecke und Gesamtstrecke aller Taxis pro
# # Jahr und deren jeweiliger Entwicklung über die Zeit hinweg
# mean_totalamount = col_totalamount.mean()
# print("Durchschnittlicher Fahrpreis: ", round(mean_totalamount, 2), "$")
