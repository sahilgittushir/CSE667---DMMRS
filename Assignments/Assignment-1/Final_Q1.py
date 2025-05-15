import numpy as np
from itertools import product

class StrategicFormGame:
    def __init__(self, payoff_matrices):
        self.payoff_matrices = payoff_matrices
        self.n_players = len(payoff_matrices)
        self.n_actions = [matrix.shape[i] for i, matrix in enumerate(payoff_matrices)]
        
    def find_dominant_strategies(self, dominance_type='strong'):
        dominant_strategies = [[] for _ in range(self.n_players)]
        
        for player in range(self.n_players):
            for strategy in range(self.n_actions[player]):
                is_dominant = True
                
                # Compare against all other strategies
                for other_strategy in range(self.n_actions[player]):
                    if strategy == other_strategy:
                        continue
                    
                    # Check all possible opponent strategy profiles
                    for opponents_profile in product(*[range(n) for i, n in enumerate(self.n_actions) if i != player]):
                        # Construct full strategy profile
                        profile = list(opponents_profile)
                        profile.insert(player, strategy)
                        current_payoff = self.payoff_matrices[player][tuple(profile)]
                        
                        # Construct profile with alternative strategy
                        alt_profile = list(opponents_profile)
                        alt_profile.insert(player, other_strategy)
                        alt_payoff = self.payoff_matrices[player][tuple(alt_profile)]
                        
                        if dominance_type == 'strong':
                            if alt_payoff >= current_payoff:
                                is_dominant = False
                                break
                        elif dominance_type == 'weak':
                            if alt_payoff > current_payoff:
                                is_dominant = False
                                break
                    
                    if not is_dominant:
                        break
                
                if is_dominant:
                    dominant_strategies[player].append(strategy)
        
        return dominant_strategies
    
    def find_maxmin_values_and_strategies(self):
        maxmin_values = []
        maxmin_strategies = [[] for _ in range(self.n_players)]
        
        for player in range(self.n_players):
            max_min_value = -np.inf
            best_strategies = []
            
            for strategy in range(self.n_actions[player]):
                # Find minimum payoff for this strategy across all opponent profiles
                min_payoff = np.inf
                
                for opponents_profile in product(*[range(n) for i, n in enumerate(self.n_actions) if i != player]):
                    profile = list(opponents_profile)
                    profile.insert(player, strategy)
                    payoff = self.payoff_matrices[player][tuple(profile)]
                    
                    if payoff < min_payoff:
                        min_payoff = payoff
                
                # Update maxmin value and strategies
                if min_payoff > max_min_value:
                    max_min_value = min_payoff
                    best_strategies = [strategy]
                elif min_payoff == max_min_value:
                    best_strategies.append(strategy)
            
            maxmin_values.append(max_min_value)
            maxmin_strategies[player] = best_strategies
        
        return maxmin_values, maxmin_strategies
    
    def find_dominant_strategy_equilibria(self, dominance_type='strong'):
        if dominance_type == 'strong':
            dominant_strategies = self.find_dominant_strategies('strong')
        else:
            dominant_strategies = self.find_dominant_strategies('weak')
        
        # Check if each player has at least one dominant strategy
        for player in range(self.n_players):
            if not dominant_strategies[player]:
                return []
        
        # All combinations of dominant strategies form the equilibrium
        equilibria = list(product(*dominant_strategies))
        return equilibria
    
    def analyze_game(self):
        print(f"Analyzing {self.n_players}-player strategic form game")
        
        # Strongly dominant strategies
        strong_dominant = self.find_dominant_strategies('strong')
        print("\nStrongly dominant strategies:")
        for i, strategies in enumerate(strong_dominant, 1):
            print(f"Player {i}: {strategies if strategies else 'None'}")
        
        # Weakly dominant strategies
        weak_dominant = self.find_dominant_strategies('weak')
        print("\nWeakly dominant strategies:")
        for i, strategies in enumerate(weak_dominant, 1):
            print(f"Player {i}: {strategies if strategies else 'None'}")
        
        # Maxmin values and strategies
        maxmin_values, maxmin_strategies = self.find_maxmin_values_and_strategies()
        print("\nMaxmin values and strategies:")
        for i in range(self.n_players):
            print(f"Player {i+1}: Value = {maxmin_values[i]}, Strategies = {maxmin_strategies[i]}")
        
        # Strongly dominant strategy equilibrium
        strong_eq = self.find_dominant_strategy_equilibria('strong')
        print("\nStrongly dominant strategy equilibria:", strong_eq if strong_eq else "None")
        
        # Weakly dominant strategy equilibria
        weak_eq = self.find_dominant_strategy_equilibria('weak')
        print("Weakly dominant strategy equilibria:", weak_eq if weak_eq else "None")

# Example usage:

# BOS
print("-------------------------------------------------------------")
print("\nBOS:")
payoff_matrices_bos = [
    np.array([[2, 0], [0, 1]]),  # Player 1
    np.array([[1, 0], [0, 2]])   # Player 2
]
game_bos = StrategicFormGame(payoff_matrices_bos)
game_bos.analyze_game()
print("-------------------------------------------------------------")

# Prisoner's Dilemma
print("-------------------------------------------------------------")
print("\nPrisoner's Dilemma:")
payoff_matrices_pd = [
    np.array([[-2, -10], [-1, -5]]),  # Player 1
    np.array([[-2, -1], [-10, -5]])   # Player 2
]
game_pd = StrategicFormGame(payoff_matrices_pd)
game_pd.analyze_game()
print("-------------------------------------------------------------")

# Matching Pennies
print("-------------------------------------------------------------")
print("\nMatching Pennies:")
payoff_matrices_mp = [
    np.array([[1, -1], [-1, 1]]),  # Player 1
    np.array([[-1, 1], [1, -1]])   # Player 2
]
game_mp = StrategicFormGame(payoff_matrices_mp)
game_mp.analyze_game()
print("-------------------------------------------------------------")

# Pigous Network Game
print("-------------------------------------------------------------")
print("\nPigous Network Game:")
payoff_matrices_pn = [
    np.array([[-1, -0.5], [-1, -1]]),  # Player 1
    np.array([[-1, -1], [-0.5, -1]])   # Player 2
]
game_mp = StrategicFormGame(payoff_matrices_pn)
game_mp.analyze_game()
print("-------------------------------------------------------------")

# Rock Paper Scissor
print("-------------------------------------------------------------")
print("\nRock Paper Scissor Game:")
payoff_matrices_rps = [
    np.array([[0, -1, 1],   # Player 1's payoffs
              [1, 0, -1],
              [-1, 1, 0]]),
    np.array([[0, 1, -1],   # Player 2's payoffs
              [-1, 0, 1],
              [1, -1, 0]])
]
game_rps = StrategicFormGame(payoff_matrices_rps)
game_rps.analyze_game()
print("-------------------------------------------------------------")

# 3-Player Bar Crowding Game
print("-------------------------------------------------------------")
print("\n3-Player Bar Crowding Game:")
payoff_matrices_3ps = [
    np.array([
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
]
game_3ps = StrategicFormGame(payoff_matrices_3ps)
game_3ps.analyze_game()
print("-------------------------------------------------------------")
