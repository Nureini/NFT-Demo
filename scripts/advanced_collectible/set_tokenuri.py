from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

# https://ipfs.io/ipfs/QmRB16Ubtx2nWHzrVyiVUf1wV5prbkZSf2E3f7QzLAkBEh?filename=0-ST_BERNARD.json


dog_metadata_dic = {
    "PUG": "",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmPZoXnLFYEeKxhpujLc9TaMuDvxnJNwqYq6TxeeK7SPjA?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmRB16Ubtx2nWHzrVyiVUf1wV5prbkZSf2E3f7QzLAkBEh?filename=0-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
