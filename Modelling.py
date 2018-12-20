class MiningInstance:

    def __init__(self, name, hashrate, power, cost=None, release_month=None):
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
        self.release_month = release_month


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

