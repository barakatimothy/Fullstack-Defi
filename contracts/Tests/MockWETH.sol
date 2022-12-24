pragma solidity ^0.8.0;

import "@openzepelin/contracts/token/ERC20/ERC20.so;";

contract MockWETH is ERC20 {
    constructor()public ERC20("Mock WETH","WETH") {}