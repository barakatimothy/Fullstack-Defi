from brownie import (network,Interfaces,config,accounts,MockAggregatorV3,MockWETH,contract,VRFCoordinator,MockDAI)
from web3 import Web3


decimals=8
startingPrice=200000000
FORKED_BLOCKCHAIN=['mainnet-fork','mainnet-fork-dev']
LOCAL_BLOCKCHAIN=['development','ganache-local']
BREED_MAPPING = {0:'pug',1:'shiba_inu',2:'st_benard'}
def get_breed(breed_number):
     BREED_MAPPING[breed_number]


def get_accounts(index=None ,id=None):
     #accounts[0]
     #accounts.add("env")
     #accounts.load("id ")
     if index:
          return accountsp[index]
     if id:
          return accounts.load(id)
     
     if network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]
   
     return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    print("Deploying Mock Link Token...")
    link_token = LinkToken.deploy({"from": account})
    print("Deploying Mock Price Feed...")
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": account}
    )
    print(f"Deployed to {mock_price_feed.address}")
    print("Deploying Mock VRFCoordinator...")
    mock_vrf_coordinator = VRFCoordinatorV2Mock.deploy(
        BASE_FEE, GAS_PRICE_LINK, {"from": account}
    )
    print(f"Deployed to {mock_vrf_coordinator.address}")

    print("Deploying Mock Oracle...")
    mock_oracle = MockOracle.deploy(link_token.address, {"from": account})
    print(f"Deployed to {mock_oracle.address}")

    print("Deploying Mock Operator...")
    mock_operator = MockOperator.deploy(link_token.address, account, {"from": account})
    print(f"Deployed to {mock_operator.address}")
    print("Deployed to {mock_price_feed.address}")
    print("Deploying Mock DAI...")
    dai_token = MockDAI.deploy({'from':account})
    print("Deployed to {dai_token.address}")
    print('Deploying WETH')
    weth_token = MockWETH.deploy({"from":account})
    print("Deployed to {weth_token.address}")
    print("Mocks Deployed!")





contract_to_mock = {
     "eth_usd_price_feed":MockAggregatorV3,
     "dai_usd_price_feed":MockAggregatorV3,
     'fau_token': MockDAI,
     'weth_token': MockWET
          
}

def get_contratcts(contract_name,):
     """ This function grabs the contract address from brownie config 
        if defined,othherwise it deploys a mock version of the contract ,and 
        returns that contract
        Args:
          contract_name(string)
          return 
          brownie.network.contract.projectContact: The most recently 
          deployed version of this contract
          mockV3Aggreggator[-1]
     """
     contract_type = contract_to_mock[contract_name]
     if network.show_active() in  LOCAL_BLOCKCHAIN:
          if len(contract_type)<=0:
               deploy_mocks()
          contract = contract_type[-1]
     else:
           contract = config['networks'][network.show_active()]
           [contract_name]
           #contract 
           #ABI
           contract = Contract.from_abi(contract_type._name,contract_address,contract_type.abi)
           return contract     
DECIMAL = 8
INITIAL_VALUE =200000000000
def deploy_mocks(decimals = DECIMAL,initial_value =INITIAL_VALUE):
     accounts = get_accounts()
     mock_price_feed = MockAggregatorV3.deploy(decimals,initial_value,{"from":account})
     link_token =LinkToken.deploy({'from':accounts})
     VRFCoordinator.deploy(link_token.address, {'from':accounts})
     print ("depployed")     
def fund_with_link(contract_address,account =None,link_token=None,amount=100000):
     accounts = accounts if account else get_accounts()
     
     link_token = link_token if link_token else get_contratcts("link_token")
     tx = link_token.transfer(contract_address,amount,{'from':account})
     tx.wait(1)