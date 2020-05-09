from single_validator import *
from broadcastBlock import *
from list_of_miners import pick_winners

def Transaction (yes_validators, no_validators):
    pnsh=True,
    Status=""
    yes_validators=[]
    no_validators=[]
    validator_award=6
    miner_award=60
    win_miner=MinerList(miner_list).pick_winners()
    broadcastBlock (Pnsh, status, yes_validators, no_validators)

# Complete Transaction for miners and validators and miners

    if pnsh==True and len(yes_validators) > len(no_validators):
        for valdiator in says_no:
            validator.owl_coins_staked=0
        for validator in say_yes:
            validator.owl_coins_staked+=validator_award
            win_miner[0].mistakes-=1

     else
        for valdiator in says_yes:
        validator.owl_coins_staked-=(validator.owl_coins_staked)*.06
        for validator in say_no:
            validator.owl_coins_staked+=validator_award

return (Status)
