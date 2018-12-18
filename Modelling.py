import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plt.interactive(True)
# pd.options.display.max_columns = 15


class MiningInstance:

    def __init__(self, name, hashrate, power, cost=None):
        """

        :param name: str, name of the instance
        :param hashrate: int, Megahashes per second
        :param power: int, Watt?
        :param cost: int, USA dollars
        """

        self.name = name
        self.hashrate = hashrate
        self.power = power
        self.cost = cost


class MiningLocation:

    def __init__(self, electricity_price, name=None):
        """

        :param name: str, name of location
        :param electricity_price: float, electricity_price in USD/KWh
        """
        self.electricity_price = electricity_price
        self.name = name


class EtheriumParams:

    def __init__(self, block_reward, block_time, network_hashrate, etherium_price=None):
        """

        :param block_reward: int, block reward in ETH
        :param block_time: int, time between blocks in seconds
        :param network_hashrate: float, network hash rate in MH/S
        :param etherium_price: float, ETH price in USA dollars
        """
        self.block_reward = block_reward
        self.block_time = block_time
        self.network_hashrate = network_hashrate
        self.etherium_price = etherium_price

def estimate_profit(mining_instance, mining_location, etherium_params, in_dollars=True):
    hashrate = mining_instance.hashrate
    network_hashrate = etherium_params.network_hashrate
    block_reward = etherium_params.block_reward
    block_time = etherium_params.block_time
    etherium_price = etherium_params.etherium_price

    electricity_price = mining_location.electricity_price
    electricity_price_w_per_second = electricity_price / (3600 * 10 ** 3)
    power = mining_instance.power


    hashrate_share = hashrate / network_hashrate
    value_from_mining_eth = hashrate_share * (block_reward / block_time)  # In ETH
    value_from_mining = value_from_mining_eth * etherium_price
    cost_for_electricity = electricity_price_w_per_second * power

    # if (in_dollars) and (etherium_price is not None):
    #     value_from_mining *= etherium_price
    # cost_for_electricity *= etherium_price

    profit = value_from_mining - cost_for_electricity

    return value_from_mining, cost_for_electricity, profit




# df_etherium_prices = pd.read_csv('data/ETH-USD.csv')
# df_etherium_prices = df_etherium_prices[['Date', 'Adj Close']]
# df_etherium_prices.rename(columns={'Adj Close': 'Price'}, inplace=True)
# mask = ('2017-11-01' <= df_etherium_prices['Date']) & (df_etherium_prices['Date'] < '2018-12-01')
# df_etherium_prices = df_etherium_prices.loc[mask, :].reset_index(drop=True)
#
# hashrates = pd.read_csv('data/network_hashrate.csv', sep=';')
#
# df = df_etherium_prices.merge(hashrates, on='Date')
#
# df['Date'] = ['2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05',
#               '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11']
# df.rename(columns={'Date': 'Month'}, inplace=True)
#
#
# # mining_instance = MiningInstance(name='AMD Radeon Vega', hashrate=45, power=150)
# radeon_vega = MiningInstance(name='AMD Radeon Vega', hashrate=37.5, power=200)
# amd_rx_580 = MiningInstance(name='AMD RX 580', hashrate=25, power=175)
# asic = MiningInstance(name='ASIC', hashrate=180, power=800)
# etherium_params = EtheriumParams(block_reward=3, block_time=15, network_hashrate=166*10**6, etherium_price=110)
# mining_location = MiningLocation(0.1, 'Somethere on the Earth')
#
# mining_instances_results = {}
#
# for mining_instance in [radeon_vega, amd_rx_580, asic]:
#     mining_instance_name = mining_instance.name
#     profit_results_list = []
#
#     for n_row in range(df.shape[0]):
#         month = df.loc[n_row, 'Month']
#         etherium_price = df.loc[n_row, 'Price']
#         network_hashrate = df.loc[n_row, 'network_hashrate']
#
#         etherium_params.etherium_price = etherium_price
#         etherium_params.network_hashrate = network_hashrate * 10 ** 6
#
#         value_from_mining, cost_for_electricity, profit = estimate_profit(mining_instance, mining_location, etherium_params)
#         profit_result = {
#             'Month': month,
#             'value_from_mining': value_from_mining,
#             'cost_for_electricity': cost_for_electricity,
#             'profit_per_second': profit,
#             'profit_per_month': profit * 60 * 60 * 24 * 30,
#         }
#         profit_results_list.append(profit_result)
#
#     df_mining_instance = pd.DataFrame(profit_results_list)
#     mining_instances_results[mining_instance_name] = df_mining_instance
#
#
# plt.close()
# fig, ax = plt.subplots(1, 1, figsize=(12, 7))
#
# for mining_instances_name, mining_instances_result in mining_instances_results.items():
#     months = mining_instances_result['Month'].values
#     profit_per_month = mining_instances_result['profit_per_month']
#     ax.plot(months, profit_per_month, label=mining_instances_name)
#
# ax.set_xlabel('Month')
# ax.set_ylabel('USD dollars per month')
# fig.legend()
# # fig.tight_layout()
# plt.savefig('pic/profit.png')
#







# print(value_from_mining, cost_for_electricity, profit)











