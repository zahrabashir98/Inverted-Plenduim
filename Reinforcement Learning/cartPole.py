# import gym
# env = gym.make("CartPole-v1")
# observation = env.reset()
# for _ in range(2000):
#   env.render()
#   action = env.action_space.sample() # your agent here (this takes random actions)
#   observation, reward, done, info = env.step(action)

#   if done:
#     observation = env.reset()
# env.close()


import gym
env = gym.make('CartPole-v0')
# print(dir(env.action_space))
# print(env.action_space.high)

for i_episode in range(60):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        if action == 0:
          observation, reward, done, info = env.step(action)
          print(action, reward)

        # print(reward)
        # print(info)
          if done:
              print("Episode finished after {} timesteps".format(t+1))
              break
env.close()