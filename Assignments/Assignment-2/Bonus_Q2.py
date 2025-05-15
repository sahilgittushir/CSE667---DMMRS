import numpy as np
import itertools
from typing import List, Tuple, Dict, Set, Optional

class StrategicFormGame:
    def __init__(self, payoff_matrices: List[np.ndarray], player_actions: List[int]):
        self.n_players = len(player_actions)
        self.player_actions = player_actions
        self.payoff_matrices = payoff_matrices
        
        # Validate dimensions
        for i, payoff_matrix in enumerate(payoff_matrices):
            if payoff_matrix.shape != tuple(player_actions):
                raise ValueError(f"Payoff matrix for player {i} has incorrect shape. Expected {tuple(player_actions)}, got {payoff_matrix.shape}")
    
    def find_pure_nash_equilibria(self) -> List[Tuple]:
        nash_equilibria = []
        
        # Generate all possible action profiles
        action_profiles = list(itertools.product(*[range(actions) for actions in self.player_actions]))
        
        for profile in action_profiles:
            is_nash = True
            
            # Check if any player can profitably deviate
            for player in range(self.n_players):
                current_payoff = self._get_payoff(player, profile)
                
                # Check all possible deviations for this player
                for alt_action in range(self.player_actions[player]):
                    if alt_action == profile[player]:
                        continue
                    
                    # Create the alternative profile with the deviation
                    alt_profile = list(profile)
                    alt_profile[player] = alt_action
                    alt_profile = tuple(alt_profile)
                    
                    # Get payoff from the deviation
                    alt_payoff = self._get_payoff(player, alt_profile)
                    
                    # If deviation is profitable, not a Nash equilibrium
                    if alt_payoff > current_payoff:
                        is_nash = False
                        break
                
                if not is_nash:
                    break
            
            if is_nash:
                nash_equilibria.append(profile)
        
        return nash_equilibria
    
    def find_all_mixed_nash_equilibria(self) -> List[List[np.ndarray]]:
        if self.n_players == 2:
            return self._find_all_mixed_nash_two_player()
        else:
            return self._find_all_mixed_nash_n_player()
    
    def _find_all_mixed_nash_two_player(self) -> List[List[np.ndarray]]:
        # Check for pure NE first, as they're also mixed NE
        pure_ne = self.find_pure_nash_equilibria()
        
        # Convert pure NE to mixed strategy representation
        mixed_ne_list = []
        for profile in pure_ne:
            mixed_profile = []
            for i, action in enumerate(profile):
                strategy = np.zeros(self.player_actions[i])
                strategy[action] = 1.0
                mixed_profile.append(strategy)
            mixed_ne_list.append(mixed_profile)
        
        # Now find mixed NE that aren't pure
        all_mixed_ne = self._find_all_mixed_nash_n_player()
        
        # Add non-duplicate mixed NE
        for mixed_ne in all_mixed_ne:
            # Check if this is already in our list (avoiding near-duplicates)
            is_duplicate = False
            for existing_ne in mixed_ne_list:
                if self._is_same_mixed_ne(mixed_ne, existing_ne):
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                mixed_ne_list.append(mixed_ne)
        
        return mixed_ne_list
    
    def _is_same_mixed_ne(self, ne1: List[np.ndarray], ne2: List[np.ndarray], tolerance: float = 1e-6) -> bool:
        if len(ne1) != len(ne2):
            return False
        
        for i in range(len(ne1)):
            if ne1[i].shape != ne2[i].shape:
                return False
            
            if not np.allclose(ne1[i], ne2[i], atol=tolerance):
                return False
        
        return True
    
    def _find_all_mixed_nash_n_player(self) -> List[List[np.ndarray]]:
        all_equilibria = []
        
        for support_size in range(1, max(self.player_actions) + 1):
            # Generate all possible strategy combinations for each player
            player_supports = []
            for p in range(self.n_players):
                player_p_supports = []
                n_actions = self.player_actions[p]
                
                # Generate all profiles of sizes 1 to max available
                max_size = min(support_size, n_actions)
                for size in range(1, max_size + 1):
                    for support in itertools.combinations(range(n_actions), size):
                        player_p_supports.append(set(support))
                
                player_supports.append(player_p_supports)
            
            # Check all combinations
            for supports in itertools.product(*player_supports):
                mixed_ne = self._check_support_profile(supports)
                
                if mixed_ne is not None:
                    # Check if this equilibrium is already in our list (avoiding near-duplicates)
                    is_duplicate = False
                    for existing_ne in all_equilibria:
                        if self._is_same_mixed_ne(mixed_ne, existing_ne):
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        all_equilibria.append(mixed_ne)
        
        return all_equilibria
    
    def _check_support_profile(self, supports: Tuple[Set[int], ...]) -> Optional[List[np.ndarray]]:
        n_players = self.n_players
        mixed_strategies = []
        
        # For each player, solve for their mixed strategy
        for player in range(n_players):
            support = supports[player]
            n_actions = self.player_actions[player]
            
            # If support is the full action set, use uniform distribution
            if len(support) == n_actions:
                mixed_strategies.append(np.ones(n_actions) / n_actions)
                continue
            
            # Create strategy vector
            strategy = np.zeros(n_actions)
            
            # For single action support, it's a pure strategy
            if len(support) == 1:
                action = list(support)[0]
                strategy[action] = 1.0
                mixed_strategies.append(strategy)
                continue
            
            support_list = list(support)
            A = np.zeros((len(support), len(support)))
            b = np.zeros(len(support))
            
            # Add constraint: sum of probabilities = 1
            A[-1, :] = 1
            b[-1] = 1
            
            # Add indifference constraints
            baseline_action = support_list[0]
            
            for i, action in enumerate(support_list[1:]):
                # For each action profile of other players
                other_player_indices = list(range(n_players))
                other_player_indices.remove(player)
                other_player_actions = [self.player_actions[p] for p in other_player_indices]
                
                other_player_profiles = list(itertools.product(*[range(actions) for actions in other_player_actions]))
                
                for j, other_profile in enumerate(other_player_profiles):
                    # Insert baseline action and alternative action
                    baseline_profile = list(other_profile)
                    alternative_profile = list(other_profile)
                    
                    # Insert at the correct position for player
                    for k, p in enumerate(other_player_indices):
                        if p < player:
                            baseline_profile.insert(p, baseline_action)
                            alternative_profile.insert(p, action)
                        else:
                            baseline_profile.insert(p, baseline_action)
                            alternative_profile.insert(p, action)
                    
                    # Compute payoff difference
                    baseline_payoff = self._get_payoff(player, tuple(baseline_profile))
                    alt_payoff = self._get_payoff(player, tuple(alternative_profile))
                    
                    # Add coefficients to the system
                    A[i, 0] += baseline_payoff - alt_payoff
                    A[i, i+1] += alt_payoff - baseline_payoff
        
        # Check if the strategies form a Nash equilibrium
        if self._is_mixed_nash_equilibrium(mixed_strategies):
            return mixed_strategies
        
        return None
    
    def _is_mixed_nash_equilibrium(self, strategies: List[np.ndarray]) -> bool:
        for player in range(self.n_players):
            # Calculate expected payoff for each action
            expected_payoffs = self._calculate_expected_payoffs(player, strategies)
            
            # Get the support of the player's strategy
            support = set(np.where(strategies[player] > 1e-10)[0])
            
            # Check if all actions in support yield the same payoff
            if support:
                baseline_payoff = expected_payoffs[list(support)[0]]
                
                for action in support:
                    if abs(expected_payoffs[action] - baseline_payoff) > 1e-6:
                        return False
                
                # Check if actions outside support yield lower or equal payoffs
                for action in range(self.player_actions[player]):
                    if action not in support and expected_payoffs[action] > baseline_payoff + 1e-6:
                        return False
        
        return True
    
    def _calculate_expected_payoffs(self, player: int, strategies: List[np.ndarray]) -> np.ndarray:
        n_actions = self.player_actions[player]
        expected_payoffs = np.zeros(n_actions)
        
        # For each action of the player
        for action in range(n_actions):
            # Create a modified strategy where the player plays this action with probability 1
            pure_strategy = np.zeros(n_actions)
            pure_strategy[action] = 1.0
            
            # Create a profile with this pure strategy
            profile = strategies.copy()
            profile[player] = pure_strategy
            
            # Calculate expected payoff
            expected_payoffs[action] = self._calculate_expected_payoff(player, profile)
        
        return expected_payoffs
    
    def _calculate_expected_payoff(self, player: int, strategies: List[np.ndarray]) -> float:
        indices = [range(self.player_actions[p]) for p in range(self.n_players)]
        
        # Calculate expected payoff by summing over all action profiles
        expected_payoff = 0.0
        
        for action_profile in itertools.product(*indices):
            # Calculate probability of this action profile
            profile_prob = 1.0
            for p, action in enumerate(action_profile):
                profile_prob *= strategies[p][action]
            
            # Add contribution to expected payoff
            payoff = self._get_payoff(player, action_profile)
            expected_payoff += profile_prob * payoff
        
        return expected_payoff
    
    def _get_payoff(self, player: int, action_profile: Tuple[int, ...]) -> float:
        return self.payoff_matrices[player][action_profile]

def main():
    coord_game = StrategicFormGame(
    [   np.array([
            [[-1, 2], [2, 0]],  # Gus's payoffs
            [[1, 1], [1, 1]]
        ]),
        np.array([
            [[-1, 2], [1, 1]],  # Yelnic's payoffs
            [[2, 1], [1, 1]]
        ]),
        np.array([
            [[-1, 1], [2, 1]],  # Tolbert's payoffs
            [[2, 1], [0, 1]]
        ])
    ], 
    [2, 2, 2])
    
    # Find pure Nash equilibria
    pure_ne = coord_game.find_pure_nash_equilibria()
    print("Pure Strategy Nash Equilibria:")
    for ne in pure_ne:
        print(f"  {ne}")
    
    # Find a mixed Nash equilibrium
    mixed_ne = coord_game.find_all_mixed_nash_equilibria()
    print("Mixed Strategy Nash Equilibrium:")
    for i, strategy in enumerate(mixed_ne):
        print(f"Eq-{i+1}: {strategy}")
        
if __name__ == "__main__":
    main()
    
    
# # 6. 3-Player Bar Crowding Game
# print("-------------------------------------------------------------")
# print("\n3-Player Bar Crowding Game:")
# payoff_matrices_3ps = [
#     np.array([
#         [[-1, 2], [2, 0]],  # Gus's payoffs
#         [[1, 1], [1, 1]]
#     ]),
#     np.array([
#         [[-1, 2], [1, 1]],  # Yelnic's payoffs
#         [[2, 1], [1, 1]]
#     ]),
#     np.array([
#         [[-1, 1], [2, 1]],  # Tolbert's payoffs
#         [[2, 1], [0, 1]]
#     ])
# ]
# analyze_game(payoff_matrices_3ps)
# print("-------------------------------------------------------------")