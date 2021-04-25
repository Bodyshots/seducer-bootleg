from reactions import (Character, distasteful, confusion, badass, understanding,
                       impressed, loves_energy, revulsion, fight, appreciate,
                       crowd_silence_effects, choke_neg, choke_pos, funny,
                       unimpressed, weights, honesty, lies, fap_confused,
                       event_remembers_B, person_is_profession, event_blind_A,
                       event_blind_B, event_blind_C, event_blind_D, slap,
                       event_remembers_C, chess, sincere_laugh, event_video_A,
                       event_video_C, lack_energy, arm_wrestle, event_robbery_A,
                       event_robbery_B, event_friend_ignore, event_fight_win,
                       crowd_silence_child_B, event_robbery_C, pathetic,
                       event_friend_buzz_neg, choke_neg_pos, abs_muscles,
                       event_robbery_D)
from constants import OPTION_A, OPTION_B, OPTION_C, OPTION_D, NORMAL
from typing import Dict

class NormalCharacter(Character):
    """
    Create a Normal Character, a subclass of Character

    """

    def reactions(self) -> Dict:
        react_dict = {0: {OPTION_A: confusion,
                          OPTION_B: appreciate,
                          OPTION_C: distasteful,
                          OPTION_D: confusion},
                       1: {OPTION_A: distasteful,
                           OPTION_B: distasteful,
                           OPTION_C: confusion,
                           OPTION_D: appreciate},
                       2: {OPTION_A: choke_neg,
                           OPTION_B: choke_pos,
                           OPTION_C: confusion,
                           OPTION_D: confusion},
                       3: {OPTION_A: crowd_silence_effects,
                           OPTION_B: understanding,
                           OPTION_C: distasteful,
                           OPTION_D: understanding},
                       4: {OPTION_A: distasteful,
                           OPTION_B: revulsion,
                           OPTION_C: understanding,
                           OPTION_D: confusion},
                       5: {OPTION_A: confusion,
                           OPTION_B: funny,
                           OPTION_C: understanding,
                           OPTION_D: distasteful},
                       6: {OPTION_A: fight,
                           OPTION_B: confusion,
                           OPTION_C: confusion,
                           OPTION_D: distasteful},
                       7: {OPTION_A: unimpressed,
                           OPTION_B: weights,
                           OPTION_C: unimpressed,
                           OPTION_D: understanding},
                       8: {OPTION_A: distasteful,
                           OPTION_B: understanding,
                           OPTION_C: distasteful,
                           OPTION_D: fap_confused},
                       9: {OPTION_A: fight,
                           OPTION_B: distasteful,
                           OPTION_C: unimpressed,
                           OPTION_D: unimpressed},
                       10: {OPTION_A: honesty,
                            OPTION_B: revulsion,
                            OPTION_C: badass,
                            OPTION_D: confusion},
                       11: {OPTION_A: event_blind_A,
                            OPTION_B: event_blind_B,
                            OPTION_C: event_blind_C,
                            OPTION_D: event_blind_D},
                       12: {OPTION_A: person_is_profession,
                            OPTION_B: understanding,
                            OPTION_C: slap,
                            OPTION_D: distasteful},
                       13: {OPTION_A: confusion,
                            OPTION_B: crowd_silence_child_B,
                            OPTION_C: crowd_silence_effects,
                            OPTION_D: appreciate},
                       14: {OPTION_A: distasteful,
                            OPTION_B: event_remembers_B,
                            OPTION_C: event_remembers_C,
                            OPTION_D: confusion},
                       15: {OPTION_A: confusion,
                            OPTION_B: confusion,
                            OPTION_C: sincere_laugh,
                            OPTION_D: abs_muscles},
                       16: {OPTION_A: event_video_A,
                            OPTION_B: appreciate,
                            OPTION_C: distasteful,
                            OPTION_D: revulsion},
                       17: {OPTION_A: event_robbery_A,
                            OPTION_B: event_robbery_B,
                            OPTION_C: event_robbery_C,
                            OPTION_D: event_robbery_D},
                       18: {OPTION_A: appreciate,
                            OPTION_B: revulsion,
                            OPTION_C: revulsion,
                            OPTION_D: revulsion},
                       19: {OPTION_A: event_friend_ignore,
                            OPTION_B: event_fight_win,
                            OPTION_C: event_friend_ignore,
                            OPTION_D: event_friend_ignore}}   
        return react_dict

class ActiveCharacter(Character):
    """ 
    Create an Active Character, a subclass of Character

    """

    def reactions(self) -> Dict:
        react_dict = {0: {OPTION_A: badass,
                          OPTION_B: distasteful,
                          OPTION_C: badass,
                          OPTION_D: confusion},
                       1: {OPTION_A: distasteful,
                           OPTION_B: distasteful,
                           OPTION_C: badass,
                           OPTION_D: impressed},
                       2: {OPTION_A: choke_neg,
                           OPTION_B: choke_pos,
                           OPTION_C: loves_energy,
                           OPTION_D: confusion},
                       3: {OPTION_A: crowd_silence_effects,
                           OPTION_B: impressed,
                           OPTION_C: distasteful,
                           OPTION_D: understanding},
                       4: {OPTION_A: distasteful,
                           OPTION_B: loves_energy,
                           OPTION_C: appreciate,
                           OPTION_D: confusion},
                       5: {OPTION_A: distasteful,
                           OPTION_B: sincere_laugh,
                           OPTION_C: confusion,
                           OPTION_D: loves_energy},
                       6: {OPTION_A: fight,
                           OPTION_B: loves_energy,
                           OPTION_C: impressed,
                           OPTION_D: badass},
                       7: {OPTION_A: unimpressed,
                           OPTION_B: weights,
                           OPTION_C: unimpressed,
                           OPTION_D: understanding},
                       8: {OPTION_A: badass,
                           OPTION_B: appreciate,
                           OPTION_C: loves_energy,
                           OPTION_D: fap_confused},
                       9: {OPTION_A: fight,
                           OPTION_B: distasteful,
                           OPTION_C: unimpressed,
                           OPTION_D: revulsion},
                       10: {OPTION_A: revulsion,
                            OPTION_B: loves_energy,
                            OPTION_C: badass,
                            OPTION_D: revulsion},
                       11: {OPTION_A: event_blind_A,
                            OPTION_B: event_blind_B,
                            OPTION_C: event_blind_C,
                            OPTION_D: event_blind_D},
                       12: {OPTION_A: person_is_profession,
                            OPTION_B: distasteful,
                            OPTION_C: distasteful,
                            OPTION_D: unimpressed},
                       13: {OPTION_A: confusion,
                            OPTION_B: crowd_silence_child_B,
                            OPTION_C: crowd_silence_effects,
                            OPTION_D: distasteful},
                       14: {OPTION_A: distasteful,
                            OPTION_B: event_remembers_B,
                            OPTION_C: event_remembers_C,
                            OPTION_D: confusion},
                       15: {OPTION_A: arm_wrestle,
                            OPTION_B: distasteful,
                            OPTION_C: confusion,
                            OPTION_D: abs_muscles},
                       16: {OPTION_A: event_video_A,
                            OPTION_B: lack_energy,
                            OPTION_C: event_video_C,
                            OPTION_D: revulsion},
                       17: {OPTION_A: event_robbery_A,
                            OPTION_B: event_robbery_B,
                            OPTION_C: event_robbery_C,
                            OPTION_D: event_robbery_D},
                       18: {OPTION_A: badass,
                            OPTION_B: revulsion,
                            OPTION_C: revulsion,
                            OPTION_D: revulsion},
                       19: {OPTION_A: event_friend_ignore,
                            OPTION_B: event_fight_win,
                            OPTION_C: event_friend_ignore,
                            OPTION_D: event_friend_buzz_neg}}
        return react_dict

class NegativeCharacter(Character):
    """ 
    Create a Negative Character, a subclass of Character

    """
    
    def reactions(self) -> Dict:
        react_dict = {0: {OPTION_A: unimpressed,
                          OPTION_B: distasteful,
                          OPTION_C: appreciate,
                          OPTION_D: confusion},
                       1: {OPTION_A: confusion,
                           OPTION_B: pathetic,
                           OPTION_C: understanding,
                           OPTION_D: distasteful},
                       2: {OPTION_A: choke_neg_pos,
                           OPTION_B: choke_neg_pos,
                           OPTION_C: choke_neg_pos,
                           OPTION_D: choke_neg_pos},
                       3: {OPTION_A: crowd_silence_effects,
                           OPTION_B: understanding,
                           OPTION_C: sincere_laugh,
                           OPTION_D: distasteful},
                       4: {OPTION_A: funny,
                           OPTION_B: revulsion,
                           OPTION_C: distasteful,
                           OPTION_D: confusion},
                       5: {OPTION_A: confusion,
                           OPTION_B: distasteful,
                           OPTION_C: pathetic,
                           OPTION_D: distasteful},
                       6: {OPTION_A: fight,
                           OPTION_B: confusion,
                           OPTION_C: confusion,
                           OPTION_D: pathetic},
                       7: {OPTION_A: honesty,
                           OPTION_B: weights,
                           OPTION_C: honesty,
                           OPTION_D: distasteful},
                       8: {OPTION_A: distasteful,
                           OPTION_B: pathetic,
                           OPTION_C: unimpressed,
                           OPTION_D: honesty},
                       9: {OPTION_A: fight,
                           OPTION_B: funny,
                           OPTION_C: unimpressed,
                           OPTION_D: pathetic},
                       10: {OPTION_A: honesty,
                            OPTION_B: distasteful,
                            OPTION_C: funny,
                            OPTION_D: pathetic},
                       11: {OPTION_A: event_blind_A,
                            OPTION_B: event_blind_B,
                            OPTION_C: event_blind_C,
                            OPTION_D: event_blind_D},
                       12: {OPTION_A: person_is_profession,
                            OPTION_B: honesty,
                            OPTION_C: funny,
                            OPTION_D: unimpressed},
                       13: {OPTION_A: understanding,
                            OPTION_B: crowd_silence_child_B,
                            OPTION_C: crowd_silence_effects,
                            OPTION_D: distasteful},
                       14: {OPTION_A: funny,
                            OPTION_B: event_remembers_B,
                            OPTION_C: event_remembers_C,
                            OPTION_D: confusion},
                       15: {OPTION_A: distasteful,
                            OPTION_B: distasteful,
                            OPTION_C: distasteful,
                            OPTION_D: abs_muscles},
                       16: {OPTION_A: event_video_A,
                            OPTION_B: appreciate,
                            OPTION_C: event_video_C,
                            OPTION_D: pathetic},
                       17: {OPTION_A: event_robbery_A,
                            OPTION_B: event_robbery_B,
                            OPTION_C: event_robbery_C,
                            OPTION_D: event_robbery_D},
                       18: {OPTION_A: honesty,
                            OPTION_B: revulsion,
                            OPTION_C: revulsion,
                            OPTION_D: revulsion},
                       19: {OPTION_A: event_friend_ignore,
                            OPTION_B: event_fight_win,
                            OPTION_C: event_friend_ignore,
                            OPTION_D: event_friend_buzz_neg}}
        return react_dict

class ObjectiveCharacter(Character):
    """ 
    Create an Objective Character, a subclass of Character

    """

    def reactions(self) -> Dict:
        react_dict = {0: {OPTION_A: confusion,
                          OPTION_B: understanding,
                          OPTION_C: confusion,
                          OPTION_D: confusion},
                       1: {OPTION_A: impressed,
                           OPTION_B: understanding,
                           OPTION_C: distasteful,
                           OPTION_D: understanding},
                       2: {OPTION_A: choke_neg,
                           OPTION_B: choke_pos,
                           OPTION_C: confusion,
                           OPTION_D: confusion},
                       3: {OPTION_A: crowd_silence_effects,
                           OPTION_B: understanding,
                           OPTION_C: distasteful,
                           OPTION_D: unimpressed},
                       4: {OPTION_A: distasteful,
                           OPTION_B: revulsion,
                           OPTION_C: appreciate,
                           OPTION_D: funny},
                       5: {OPTION_A: distasteful,
                           OPTION_B: distasteful,
                           OPTION_C: confusion,
                           OPTION_D: distasteful},
                       6: {OPTION_A: fight,
                           OPTION_B: confusion,
                           OPTION_C: confusion,
                           OPTION_D: confusion},
                       7: {OPTION_A: honesty,
                           OPTION_B: weights,
                           OPTION_C: funny,
                           OPTION_D: impressed},
                       8: {OPTION_A: sincere_laugh,
                           OPTION_B: unimpressed,
                           OPTION_C: revulsion,
                           OPTION_D: revulsion},
                       9: {OPTION_A: fight,
                           OPTION_B: unimpressed,
                           OPTION_C: distasteful,
                           OPTION_D: revulsion},
                       10: {OPTION_A: honesty,
                            OPTION_B: funny,
                            OPTION_C: lies,
                            OPTION_D: unimpressed},
                       11: {OPTION_A: event_blind_A,
                            OPTION_B: event_blind_B,
                            OPTION_C: event_blind_C,
                            OPTION_D: event_blind_D},
                       12: {OPTION_A: person_is_profession,
                            OPTION_B: unimpressed,
                            OPTION_C: distasteful,
                            OPTION_D: sincere_laugh},
                       13: {OPTION_A: confusion,
                            OPTION_B: crowd_silence_child_B,
                            OPTION_C: crowd_silence_effects,
                            OPTION_D: appreciate},
                       14: {OPTION_A: revulsion,
                            OPTION_B: event_remembers_B,
                            OPTION_C: event_remembers_C,
                            OPTION_D: confusion},
                       15: {OPTION_A: confusion,
                            OPTION_B: chess,
                            OPTION_C: impressed,
                            OPTION_D: abs_muscles},
                       16: {OPTION_A: event_video_A,
                            OPTION_B: impressed,
                            OPTION_C: distasteful,
                            OPTION_D: revulsion},
                       17: {OPTION_A: event_robbery_A,
                            OPTION_B: event_robbery_B,
                            OPTION_C: event_robbery_C,
                            OPTION_D: event_robbery_D},
                       18: {OPTION_A: appreciate,
                            OPTION_B: revulsion,
                            OPTION_C: revulsion,
                            OPTION_D: revulsion},
                       19: {OPTION_A: event_friend_ignore,
                            OPTION_B: event_fight_win,
                            OPTION_C: event_friend_ignore,
                            OPTION_D: event_friend_ignore}}
        return react_dict
