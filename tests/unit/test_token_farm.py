from brownie import networks ,exceptions
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN,get_accounts,get_contracts,deploy_mocks
from scripts.deploy import deploy_token_farm_and_dapp_token
import pytest

def test_set_price_feed_contract():
    #aArrange
    if network.show_active not in LOCAL_BLOCKCHAIN:
        pytest.skip("only for local testing!")
    account = get_account()
    non_owner = get_account( index =1)
    token_farm ,dapp_token = deploy_token_farm_and_dapp_token()
    #Act 
    price_feed_address =get_contract("eth_usd_price_feed")
    token_farm.setPriceFeedContract(dapp_token.address,price_feed_address,{"from":account})
    #Assert
    assert  token_farm.tokenPriceFeedMapping(dapp_token.address ) == price_feed_address
    
    with pytest.raises(exception.VirtualMachineError):
        token_farm.setPriceFeedContract(
            dapp_token.address,price_feed_addres,{"from":non_owner}
        )
def test_staking_tokens(amount_staked):
    #aArrange
    if network.show_active not in LOCAL_BLOCKCHAIN:
        pytest.skip("only for local testing!")  
        account = get_account()    
        dapp_token ,token_farm = deploy_token_farm_and_dapp_token()
        #Act
        dapp_token.approve (token_farm.address,amount_staked,{"from":account})
        token_farm.stakeTokens(amount_staked , dapp_token.address,{"from":account})
        #Assert
        assert (token_farm.stakingBalance(dapp_token.address,account.address)) == amount_staked
        
        assert token_farm.uniqueTokenStaked(account.address) ==1
        assert token_farm.stakers == account.address
    return token_farm ,dapp_token
        
        
def test_issue_token(amount_staked):
    
    #Arrange
    if network.show_active not in LOCAL_BLOCKCHAIN:
        pytest.skip("only for local testing!")  
        account = get_account()
    token_farm ,dapp_token = test_staking_tokens(amount_staked)
    starting_balance = dapp_token.balanceOf(account.address)
    #Act
    token_farm.issueToken({'from':account})
    #Assert
    assert ( 
            dapp_token.balanceOf(account.address ))== starting_balance + starting_price