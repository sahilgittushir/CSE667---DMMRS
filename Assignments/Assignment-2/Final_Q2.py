import numpy as np
import nashpy as nash
from itertools import product

def find_pure_nash(payoff_matrices):
    n_players = len(payoff_matrices)
    shapes = [matrix.shape for matrix in payoff_matrices]
    n_actions_per_player = [shape[i] for i, shape in enumerate(shapes)]
    
    # Generate all possible action profiles
    all_action_profiles = product(*[range(n) for n in n_actions_per_player])
    
    nash_equilibria = []
    for profile in all_action_profiles:
        is_nash = True
        
        for player in range(n_players):
            current_payoff = payoff_matrices[player][profile]
            
            # Check all possible deviations for this player
            for deviation in range(n_actions_per_player[player]):
                if deviation == profile[player]:
                    continue
                
                # Create the deviated profile
                deviated_profile = list(profile)
                deviated_profile[player] = deviation
                deviated_profile = tuple(deviated_profile)
                
                if payoff_matrices[player][deviated_profile] > current_payoff:
                    is_nash = False
                    break
            
            if not is_nash:
                break
        
        if is_nash:
            nash_equilibria.append(profile)
    
    return nash_equilibria

def find_mixed_nash(payoff_matrices):
    game = nash.Game(*payoff_matrices)                # Convert to nashpy game format
    equilibria = list(game.support_enumeration())     # Compute all Nash equilibria
    return equilibria


def analyze_game(payoff_matrices):
    print("Analyzing game...")
    print(f"Number of players: {len(payoff_matrices)}")
    
    # Find pure Nash equilibria
    pure_nash = find_pure_nash(payoff_matrices)
    print("\nPure Strategy Nash Equilibria:")
    if pure_nash:
        for i, eq in enumerate(pure_nash, 1):
            print(f"{i}. {eq}")
    else:
        print("No pure strategy Nash equilibrium found.")
    
    # Find mixed Nash equilibria
    mixed_nash = find_mixed_nash(payoff_matrices)
    print("\nMixed Strategy Nash Equilibria:")
    if mixed_nash:
        for i, eq in enumerate(mixed_nash, 1):
            print(f"{i}. " + " | ".join([f"Player {p+1}: {strategy.round(3)}" for p, strategy in enumerate(eq)]))
    else:
        print("No mixed strategy Nash equilibrium found.")


## Examples:

# 1. BOS
print("-------------------------------------------------------------")
print("\nBOS:")
payoff_matrices_bos = [
    np.array([[2, 0], [0, 1]]),  # Player 1
    np.array([[1, 0], [0, 2]])   # Player 2
]
analyze_game(payoff_matrices_bos)
print("-------------------------------------------------------------")

# 2. Prisoner's Dilemma (2-player game)
print("---------------------------------------------------")
print("\nPrisoner's Dilemma:")
payoff_matrices_pd = [
    np.array([[-2, -10], [-1, -5]]),  # Player 1
    np.array([[-2, -1], [-10, -5]])   # Player 2
]
analyze_game(payoff_matrices_pd)
print("---------------------------------------------------")

# 3. Matching Pennies (2-player game)
print("---------------------------------------------------")
print("\nMatching Pennies:")
payoff_matrices_mp = [
    np.array([[1, -1], [-1, 1]]),  # Player 1
    np.array([[-1, 1], [1, -1]])   # Player 2
]
analyze_game(payoff_matrices_mp)
print("---------------------------------------------------")

# 4. Pigous Network Game
print("-------------------------------------------------------------")
print("\nPigous Network Game:")
payoff_matrices_pn = [
    np.array([[-1, -0.5], [-1, -1]]),  # Player 1
    np.array([[-1, -1], [-0.5, -1]])   # Player 2
]
analyze_game(payoff_matrices_pn)
print("-------------------------------------------------------------")

# 5. Rock Paper Scissor
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
analyze_game(payoff_matrices_rps)
print("-------------------------------------------------------------")