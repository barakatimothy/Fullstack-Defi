pragma solidity ^0.8.0;

import "@openzepelin/contracts/token/ERC20/ERC20.so;";

contract MockDAI is ERC20 {
    constructor()public ERC20("Mock DAI","DAI") {}
}