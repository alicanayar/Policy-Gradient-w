import os
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import matplotlib.pyplot as plt
names = ["cartpole", "cartpole_rtg", "cartpole_na","cartpole_rtg_na"]
names_lb = ["cartpole_lb", "cartpole_lb_rtg", "cartpole_lb_na","cartpole_lb_rtg_na"]

colors = ["b","g","r","c"]
log_dirs= ["data\q2_pg_cartpole_CartPole-v0_13-12-2024_12-38-15","data\q2_pg_cartpole_na_CartPole-v0_13-12-2024_12-41-48","data\q2_pg_cartpole_rtg_CartPole-v0_13-12-2024_12-40-27","data\q2_pg_cartpole_rtg_na_CartPole-v0_13-12-2024_12-42-51"]
log_dirs_lb = ["data\q2_pg_cartpole_lb_CartPole-v0_13-12-2024_13-07-51","data\q2_pg_cartpole_lb_rtg_CartPole-v0_13-12-2024_13-09-49","data\q2_pg_cartpole_lb_na_CartPole-v0_13-12-2024_13-11-50","data\q2_pg_cartpole_lb_rtg_na_CartPole-v0_13-12-2024_13-13-50"]

plt.figure(figsize=(10, 8))

for i in range(len(names)):


    event_acc = EventAccumulator(log_dirs_lb[i])
    event_acc.Reload()


    train_avg_return_events = event_acc.Scalars("Train_AverageReturn")
    env_steps_events = event_acc.Scalars("Train_EnvstepsSoFar")


    return_values = [event.value for event in train_avg_return_events]
    env_steps_values = [event.value for event in env_steps_events]


    plt.plot(env_steps_values, return_values, label=names_lb[i], color=colors[i])

plt.xlabel("Env Steps")
plt.ylabel("Average Return")
plt.title("Average Return Rewards vs Env Steps")
plt.legend()
plt.grid()

# Show the single plot with all datasets
plt.show()