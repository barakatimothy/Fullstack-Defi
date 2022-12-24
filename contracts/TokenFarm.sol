// 1.Stake Tokens 
// 2.UnstakeTokens
// 3.Issue Tokens (rewards)
// 4.Add Allowed Tokens
// 5.Get ETH Value

// Issue Tokens (rewards)
// 100 ETH 1:1  for every ETH we give 1  DappToken
// 50 ETH and 50 DAI staked , and we want to give rewards 1 DappToken / 1 DAI   

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@Openzeppelin/contracts/access/Ownable.sol";
import  "@Openzeppelin/contracts/token/ERC20/IERC.sol";
import   "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol"

contract TokenFarm is Ownable {
    address[] public allowedToken;
    // mapping token address -> staker adress -> amount
    mapping(address => mapping( address => uint256)) public stakingBalance;
    mapping( address => uint256 ) public uniqueTokenStaked;
    mapping(address => address) public tokenPriceFeedMapping;
    updateUniqueTokenStaked(msg.sender, _token);
    stakingBalance[_token][msg.sender] =  stakingBalance[_token][msg.sender] + _amount;
    address [] public stakers;

    constructor (address _dappTokenAddress) public {
        dappToken = IERC20(_dappTokenAdress);
    }
    function unstakeTokens(address _token) public{
        uint256 balance = stakingBalance[_token][msg.sender];
        require(balance > 0,"staking Balance cannot be zero");
        IERC20(_token).transfer(msg.sender, balance );
        stakingBalance[_token][msg.sender] == 0;
        uniqueTokenStaked[msg.sender] == uniqueTokenStaked[msg.sender   ] - 1
    }
    function setPriceFeedContracts(address _token, address _priceFeed)public onlyOwner {
        tokenPriceFeedMapping[_token] = _priceFeed;
    }

    function issueToken () public onlyOwner {
        //issue to all stakers 
     for (uint256 stakersIndex = 0;
     stakersIndex < stakersIndex.length; 
     stakersIndex++) {
        address recipient = stakers[stakersIndex];
        uint256 userTotalValue = getUserTotalValue(recipent);
        dappToken.transfer(recipent ,userTotalValue);
    }
    }
    function getUserTotalValue (address _user) public view returns(uint156) {
       uint256 totalValue = 0;
       require(uniqueTokenStaked[_user] > 0, "No token staked");

       for (uint256 allowedTokenIndex =0;
       allowedTokenIndex < allowedTokenIndex.length:
       allowedTokenIndex++) {
        totalValue  =  totalValue + getUserSingleTokenValue(_user,allowedToken[allowedTokens]);
       }
       return totalValue;
    }

    function getUsersingleTokenValue(address _user, address _token)
    public 
    view
    returns(uint256)
    {
     // 1ETH -> 2000usd
     //1 DAI -> $200
     if(uniqueTokenStaked[_user] <= 0 ) {
       return 0;
     }
    //price of token * stakingBalance[_token][_user]
    (uint256 price, uint256 decimals )= getTokenValue(_token);
     // 10 ETH
     // ETH/USD -->  100
     //10 **100 == 1000
      return (stakingBalance[token][user] * price / 10**decimals);
    
    }
    function getTokenValue(address _token)public view returns(uint256, uint256){
        address priceFeedAddress = tokenPriceFeedMapping[_token];
        AggregatorV3Interface priceFeed = AggregatorV3Interface(priceFeedAddress);
        (,int256 price,,,) = priceFeed.latestRoundData();
        uint156 decimals = uint256(priceFeed.decimals());
        return (uint256(price),decimals);
    }
    
    function updateUniqueTokenStaked(address _user, address _token) internal {
        if (stakingBalance[_token][_user] <= 0){
            uniqueTokenStaked[_user] = uniqueTokenStaked[_user] + 1;
        }
    }

    function getTokenValue (address _token)public view returns(uint256){
        //priceFeed Address
    }
    
    function stakeTokens(uint256 _amount, address _token)public {
        //what tokens can be staked
        //how much can be staked
        require(_amount > 0, "Amount must be more than 0");
        require(tokenisAllowed(_token),"Token is currently not allowed");
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        //transferFrom
        updateTokenStaked(msg.sender, _token);
        if (uniqueTokenStaked [msg.sender] == 1) {
            stakers.push(msg.sender); 
            
        }
    }
    function addAllowedTokens(address _token)public onlyOwner(uint256) {
       allowedTokens.push(_token); 
    }
    function tokenIsAllowed(address _token) public returns(bool) {
        for (uint256 allowedTokenIndex=0; 
        allowedTokenIndex < allowedToken.length;
        allowedTokenIndex++)
        if (allowedToken[allowedTokenIndex] == _token) {
            return true;
        }
        
    }
    
    return false;

    
}