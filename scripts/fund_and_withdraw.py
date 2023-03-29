from brownie import FundMe
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def fund():
    account = get_account()
    if FundMe:
        fund_me = FundMe[-1]
    else:
        fund_me = deploy_fund_me()
        print("finish deployed")
    entrance_fee = fund_me.getEntranceFee()
    print("hi")
    print(entrance_fee)
    print("hi2")
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    tx=fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)


def withdraw():
    account = get_account()
    if FundMe:
        print("hi withdraw")
        fund_me = FundMe[-1]
    else:
        fund_me = deploy_fund_me()
    tx=fund_me.withdraw({"from": account})
    tx.wait(1)
    print("bye")
    


def main():
    fund()
    withdraw()