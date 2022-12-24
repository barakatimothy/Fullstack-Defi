from scripts import helpful_scripts 
from web3 import Web3
from brownie import DappToken

KEPT_BALANCE = Web3.toWei(100,'ether')

def deploy_token_farm_and_dapp_token():
     account = get_account()
     dapp_token = DappToken.deploy({"from": account})
     token_farm = TokenFarm.deploy(dapp_token.address,{"from": account},publish_source =config["networks"]
    [network.show_active]["verify"])   
    
tx = dapp_token.transfer(token_farm.address,dapp_token.totalSupply()- KEPT_BALANCE,{"from":account}) 
tx.wait(1) 
     
def main():
    deploy_token_farm_and_dapp_token()
    