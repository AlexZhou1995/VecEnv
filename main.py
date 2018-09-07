import gym
from VecEnv import SubprocVecEnv
import numpy as np

if __name__ == '__main__':
    n_envs = 4
    envs = []

    for i in range(n_envs):
        envs.append(gym.make('CartPole-v0'))

    env = SubprocVecEnv(envs)

    env.reset()
    for i in range(1000):
        #acts = np.random.randint(2,size=n_envs)
        acts = [0,1,0,1]
        env.step(acts)
        env.render()