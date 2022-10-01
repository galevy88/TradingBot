from asyncio.windows_events import NULL
from Asset_Picker_Logic_Moudle import AssetPicker
from Data_Collecter_Moudle import DataCollecter
import Data_Collecter_Moudle
from tradingview_ta import TradingView, TA_Handler, Interval
from datetime import datetime

TRADE_FEE_PRECENT = 0.001

class API_User:
    def __init__(self, amount = 10000):
        self.collecter = DataCollecter()
        self.amount = float(amount) #
        self.amount_usdt = float(amount) #
        self.base_asset = 'USDT' #
        self.current_asset = 'USDT' #
        self.amount_after_fee_usdt = 0
        self.asset_price_at_buying = 1 #
        self.asset_price_at_selling = 1 #
        self.trade_fee_usdt_at_buying = 0 #
        self.trade_fee_usdt_at_selling = 0 #
        self.amount_usdt_at_buying = 10000
        self.payload = NULL


    def change_asset(self, chosen_asset):
        
        self.current_asset = chosen_asset
        self.asset_price_at_buying = Data_Collecter_Moudle.get_current_price_for_asset(chosen_asset)
        self.trade_fee_usdt_at_buying = self.calculate_trade_fee_usdt()
        self.amount_usdt = self.amount_usdt - self.trade_fee_usdt_at_buying
        self.amount_usdt_at_buying = self.amount_usdt
        self.amount = self.amount_usdt / self.asset_price_at_buying
        print(f'NEXT ASSET: {self.current_asset} AMOUNT: {self.amount} AMOUNT_USDT: {self.amount_usdt}')

    
    def convert_to_usdt(self):
        
        if self.current_asset != 'USDT':
            self.asset_price_at_selling = Data_Collecter_Moudle.get_current_price_for_asset(self.current_asset)
            self.trade_fee_usdt_at_selling = self.calculate_trade_fee_usdt()
            self.amount_usdt = self.amount * self.asset_price_at_selling
            self.amount_usdt = self.amount_usdt - self.trade_fee_usdt_at_selling
            self.generate_trade_payload()
            self.amount = self.amount_usdt
            self.current_asset = 'USDT'
        else:
            self.generate_trade_payload()

    def calculate_trade_fee_usdt(self):
        fee = self.amount_usdt * TRADE_FEE_PRECENT
        return fee

    def calculate_gain_lose(self, x , y):
        p = ((x - y) / x) * 100
        return p

    def generate_trade_payload(self):
        payload1 = { "Time" : str(datetime.now()),
                     "Asset" : self.current_asset,
                     "Amount" : self.amount,
                     "Amount (USDT)" : self.amount_usdt,
                     "Asset Price At Buying (USDT)" : self.asset_price_at_buying,
                     "Asset Price At Selling (USDT)" : self.asset_price_at_selling,
                     "Amount At Buying (USDT)" : self.amount_usdt_at_buying,
                     "Amount At Selling (USDT)" : self.amount_usdt,
                     "Fee At Buying (USDT)" : self.trade_fee_usdt_at_buying,
                     "Fee At Selling (USDT)" : self.trade_fee_usdt_at_selling,
                     "+ / -" : self.calculate_gain_lose(self.asset_price_at_selling, self.asset_price_at_buying),
                     "+ / - (With Fee)" : self.calculate_gain_lose(self.amount_usdt, self.amount_usdt_at_buying)
                }
        self.payload = payload1
        # print(payload1)

    def get_payload(self):
        return self.payload

