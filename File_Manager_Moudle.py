import pandas as pd
from datetime import datetime
import csv

class FileManager:

    def __init__(self):
        self.df_list = []

    def convert_indicators_to_CSV(self, asset_list ,indicator_Data):
        df = self.create_dataframe(asset_list, indicator_Data)
        self.add_time_to_csv(path = 'Data\\indicators_file.csv')
        df.to_csv('Data\\indicators_file.csv', mode='a', index=True, header=True, float_format="%.4f")

    def convert_recommendation_to_CSV(self, asset_list, recommendation_Data):
        df = self.create_dataframe(asset_list, recommendation_Data)
        self.add_time_to_csv(path = 'Data\\recommendation_file.csv')
        df.to_csv('Data\\recommendation_file.csv', mode='a', index=False, header=True, float_format="%.4f")

    def convert_trade_payload_to_CSV(self, payload_Data):
        df = self.create_dataframe_for_payload(payload_Data)
        df.to_csv('Data\\payload_file.csv', mode='a', index=False, header=True, float_format="%.4f")
        # print(df)

    
    def create_dataframe_for_payload(self, payload):
        header_list = payload.keys()
        ls = []
        ls.append(payload.values())
        df = pd.DataFrame(ls, columns=header_list)
        return df
    

    def create_dataframe(self, asset_list ,Data):
        header_list = self.create_header_for_dataFrame(Data)
        ls = []
        for asset in Data:
            ls.append(asset.values())
        df = pd.DataFrame(ls, columns=header_list, index=asset_list)
        return df
    
    
    def create_header_for_dataFrame(self, Data):  
        header_list = Data[0].keys()
        return header_list
    
        
    def add_time_to_csv(self, path):
        current_time = [datetime.now()]
        with open(path,"a") as csvFile:
            Fileout = csv.writer(csvFile)
            Fileout.writerow(current_time)
