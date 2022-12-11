// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import"@Openzeppelin/contract/token/ERC20/ERC20.sol";


contract DappToken is ERC20 {
    constructor() public    
    ERC20 ("Dapp Token", "DAPP"){
    _mint(msg.sender, 10000000000000000000000000);
    }
}