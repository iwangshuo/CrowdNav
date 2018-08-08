from gym_crowd.envs.policy.policy_factory import policy_factory
from dynav.policy.cadrl import CADRL
from dynav.policy.srl import SRL
from dynav.policy.sarl import SARL

policy_factory['cadrl'] = CADRL
policy_factory['srl'] = SRL
policy_factory['sarl'] = SARL
