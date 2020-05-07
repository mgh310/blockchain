from single_validator import *

def broadcastBlock(lst_of_validators, last_hash, new_hash, proof):
    total_validators = len(lst_of_validators)
    #get a count for how many votes it has
    vote_yes = 0
    vote_no = 0
    #we can somehow use these arrays containing who says yes and no to figure out
    #who should be punished or rewarded
    says_no = []
    says_yes = []
    for validator in lst_of_validators:
        value = validator.vote_proof(last_hash, new_hash, proof)
        if value == "no":
            says_no.append(validator)
            vote_no += 1
        elif value == "yes":
            says_yes.append(validator)
            vote_yes += 1
    #check if two/thirds of all validators agree.  If agreement is yes, then award
    #those that say yes and punish those that say no.
    validator_award=6
    if vote_yes > total_validators*(2/3):
        for valdiator in says_no:
            system.owl_coins_cleaned=validator.owl_coins_staked
            validator.owl_coins_staked=0
        for validator in say_yes:
            validator.owl_coins_staked+=validator_award

        return True
    else:
    #check if two/thirds of all validators agree.  If agreement is no, then award
    #those that say no and punish those that say no.

        if vote_no > total_validators*(2/3):
            for valdiator in says_yes:
                validator.owl_coins_staked-=(validator.owl_coins_staked)*.06
                system.owl_coins_cleaned=(validator.owl_coins_staked)*.06
                for validator in say_no:
                    validator.owl_coins_staked+=validator_award


    #check if you have 5 validators says_yes (vote=5)
        #increase all validator.owl_coins_staked in the list of total_validators
    #check if you have 4 validators says_yes (vote=4)
        #increase 4 validators with say_yes (vote=4) and slash all says_no
    #check if you have 3 validators says_yes (vote=3)
        #increase 3 validators with say_yes (vote=3) and slash all says_no

        #increase all validator.owl_coins_staked in the list of total_validators


        return False
