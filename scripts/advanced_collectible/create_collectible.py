from brownie import AdvancedCollectible
from web3 import Web3
from scripts.helpful_scripts import fund_With_link, get_account


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_With_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("Collectible created!")
