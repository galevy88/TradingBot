

from Data_Collecter_Moudle import DataCollecter
from Asset_Picker_Logic_Moudle import AssetPicker
from tradingview_ta import TradingView, TA_Handler, Interval
from API_User_Moudle import API_User
from Data_Collecter_Moudle import DataCollecter
from File_Manager_Moudle import FileManager
import time
import Time_Counter_Moudle


RAW_ASSET_LIST = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'SOLUSDT',
                  'MATICUSDT', 'CHZUSDT', 'ATOMUSDT', 'AVAXUSDT', 'DOTUSDT', 'ALGOUSDT',
                  'AAVEUSDT', 'MANAUSDT', 'SANDUSDT', 'FTMUSDT', 'UNIUSDT',
                  'TRXUSDT', 'NEARUSDT', 'XLMUSDT', 'ZILUSDT', 'XTZUSDT', 'LTCUSDT']


def timing(TIME_INTERVAL):
    time_counter = Time_Counter_Moudle.get_time_counter(TIME_INTERVAL)
    for i in range(1, time_counter):
        print(i)
        time.sleep(1)

class Handler:
    def __init__(self):
        self.API = API_User()
        self.picker = AssetPicker()
        self.collecter = DataCollecter()
        self.file_manager = FileManager()


    def Start_Routine(self):
        self.cycle_one_time()


    def cycle_one_time(self):
        print("EXECUTE")
        chosen_asset = self.choose_asset()
        self.API.convert_to_usdt()
        self.API.change_asset(chosen_asset)
        self.save_data()
        print("FINISH EXECUTE")
        timing(self.collecter.get_time_interval())
        self.cycle_one_time()

    def choose_asset(self):
        chosen_asset = self.picker.pick_asset()
        return chosen_asset
    
    def save_data(self):
       self.file_manager.convert_indicators_to_CSV(RAW_ASSET_LIST , self.collecter.generate_data_indicators_all())
       self.file_manager.convert_recommendation_to_CSV(RAW_ASSET_LIST , self.picker.current_rating_list)
       self.file_manager.convert_trade_payload_to_CSV(self.API.get_payload())



handler = Handler()
handler.Start_Routine()