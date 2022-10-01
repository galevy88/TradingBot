
from tradingview_ta import TradingView, TA_Handler, Interval
from File_Manager_Moudle import FileManager


TIME_INTERVAL = Interval.INTERVAL_5_MINUTES


RAW_ASSET_LIST = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'SOLUSDT',
                  'MATICUSDT', 'CHZUSDT', 'ATOMUSDT', 'AVAXUSDT', 'DOTUSDT', 'ALGOUSDT',
                  'AAVEUSDT', 'MANAUSDT', 'SANDUSDT', 'FTMUSDT', 'UNIUSDT',
                  'TRXUSDT', 'NEARUSDT', 'XLMUSDT', 'ZILUSDT', 'XTZUSDT', 'LTCUSDT']



def get_current_price_for_asset(chosen_asset):
    TA_Object = TA_Handler(symbol=chosen_asset, screener='Crypto', exchange='Binance', interval=Interval.INTERVAL_1_MINUTE)
    current_price = TA_Object.get_analysis().indicators["close"]
    return current_price



class DataCollecter:
    def __init__(self):
        self.asset_list = self.create_object_asset_list()
        self.file_manager = FileManager()


    def create_object_asset_list(self):
        object_asset_list = []
        for item in RAW_ASSET_LIST:
            object_asset_list.append(TA_Handler(symbol=item, screener='Crypto', exchange='Binance', interval=TIME_INTERVAL))
        return object_asset_list


    def generate_recommendation_list(self):
        Data_List = []
        for asset in self.asset_list:
            print(f'Generaeting Data for asset {asset.symbol} ... ')
            asset_recommendation_dictonary = self.create_dictonary(asset.symbol, asset.get_analysis())
            Data_List.append(asset_recommendation_dictonary)
        return Data_List

 

    def create_dictonary(self,symbol, asset_analysis):
        
        Dict = { 
          "SYMBOL" : symbol,
          "RECOMMENDATION" : asset_analysis.summary["RECOMMENDATION"],
          "SELL" : asset_analysis.summary["SELL"], 
          "BUY" : asset_analysis.summary["BUY"],
          "NEUTRAL":asset_analysis.summary["NEUTRAL"],
          "TOTAL": ""
        }

        return Dict

    def generate_data_indicators_all(self):
        print('Generating CSV Files...')
        indicator_asset_list = []
        for item in self.asset_list:
            print(f'CSV FOR: {item.symbol}')
            indicator_asset_list.append(item.get_analysis().indicators)

        return indicator_asset_list
    
    def get_time_interval(self):
        return TIME_INTERVAL

