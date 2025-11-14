import plotly.graph_objs as go
import random

# Kelly Criterion Parameters:
# - f: Fraction of capital to bet each round
# - p: Probability of winning a bet
# - q: Probability of losing (q = 1 - p)
# - a: Payout multiplier when winning (e.g. 1.0 for 100% gain)
# - b: Loss multiplier when losing (e.g. 1.0 for 100% loss)

# Set up probability and payoff parameters
win_prob = 0.6  # 0.55
lose_prob = 1 - win_prob
profit_multiplier = 1.0
loss_multiplier = 1.0

# Simulation settings
num_players = 10
initial_capital = 1
num_rounds = 200

# --- Plot: Final Capital vs. Bet Fraction (Theoretical Curve) ---
bet_fractions = []
final_capitals = []

for i in range(1, 1000):
    f = 0.001 * i
    # Theoretical final capital over num_rounds bets, assuming independent trials
    final_capital = ((1 + profit_multiplier * f) ** (win_prob * num_rounds)) * \
                    ((1 - loss_multiplier * f) ** (lose_prob * num_rounds))
    bet_fractions.append(f)
    final_capitals.append(final_capital)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=bet_fractions,
    y=final_capitals,
    mode='lines+markers',
    name='Final Capital vs Bet Fraction'
))
fig.update_layout(
    title="Theoretical Final Capital vs Bet Fraction",
    xaxis_title="Bet Fraction (f)",
    yaxis_title="Final Capital"
)
fig.show()

# --- Plot: Simulated Kelly Betting with Different Fractions ---
# Try several commonly used Kelly fractions
for f in [0.05, 0.10, 0.15, 0.20]:  # 5%, 10%, 15%, 20%, i.e. Quarter/Half/Full Kelly
    sim_fig = go.Figure()
    for player in range(num_players):
        capital = initial_capital
        capital_path = []
        wins = losses = 0

        # Simulate num_rounds bets for each player
        for round_num in range(1, num_rounds + 1):
            if random.random() < win_prob:
                capital += capital * profit_multiplier * f
                wins += 1
            else:
                capital -= capital * loss_multiplier * f
                losses += 1
            capital_path.append(capital)

        sim_fig.add_trace(go.Scatter(
            x=list(range(1, num_rounds + 1)),
            y=capital_path,
            mode='lines+markers',
            name=f'Player {player + 1}: Wins {wins}/Losses {losses}'
        ))

    sim_fig.update_layout(
        title=(f"Kelly Betting Simulation: "
               f"win={win_prob}, lose={lose_prob}, "
               f"gain={profit_multiplier}, loss={loss_multiplier}, "
               f"fraction={f:.2%}"),
        xaxis_title="Number of Bets",
        yaxis_title="Capital (log scale)",
        yaxis_type='log'
    )
    sim_fig.show()
