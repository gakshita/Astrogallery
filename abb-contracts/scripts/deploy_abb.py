import os
import time

import brownie
from brownie import AstroToken, StakingABB, accounts, network

from .utility import deploy_contract


def main():

    token_contract_address = None
    staking_contract_address = None

    if network.show_active() == "bsc-test":
        admin = accounts.add(os.environ["BSC_TEST_ADMIN"])
        token_contract_address = "0xA167211Aa0DcD4453Bc7D05d5CA0667De25fa2f6"
    elif network.show_active() == "bsc-main":
        admin = accounts.add(os.environ["BSC_MAIN_ADMIN"])
        token_contract_address = "0x277aE79C42c859cA858d5A92C22222C8b65c6D94"

    ########### Get TokenX ###########

    if not token_contract_address:
        token_contract = deploy_contract(
            admin,
            network,
            AstroToken,
            [],
        )
        token_contract_address = token_contract.address
    else:
        token_contract = AstroToken.at(token_contract_address)

    ########### Get Staking Contract ###########

    if not staking_contract_address:
        staking_contract = deploy_contract(
            admin,
            network,
            StakingABB,
            [token_contract_address],
        )
        staking_contract_address = staking_contract.address
    else:
        staking_contract = StakingABB.at(staking_contract_address)
