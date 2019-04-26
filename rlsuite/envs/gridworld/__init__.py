from gym.envs.registration import register

register(
    id='GridWorld-v0',
    entry_point='rlsuite.envs.gridworld.gridworld:GridWorld',
    max_episode_steps=50,
)
