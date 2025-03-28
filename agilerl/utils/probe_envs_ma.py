import random

import numpy as np
import torch
import torch.nn as nn
from gymnasium import spaces
from tqdm import trange


class ConstantRewardEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.observation_space = {
            "agent_0": spaces.Discrete(1),
            "agent_1": spaces.Discrete(1),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [{"agent_0": np.array([[0]]), "agent_1": np.array([[0]])}]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])}
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None]

    def step(self, action):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        reward = {"agent_0": 1, "agent_1": 0}  # Constant reward of 1
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return observation, info


class ConstantRewardImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))}
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])}
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None]

    def step(self, action):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        reward = {"agent_0": 1, "agent_1": 0}  # Constant reward of 1
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return observation, info


class ConstantRewardContActionsEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.observation_space = {
            "agent_0": spaces.Discrete(1),
            "agent_1": spaces.Discrete(1),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [{"agent_0": np.array([[0]]), "agent_1": np.array([[0]])}]
        self.sample_actions = [
            {"agent_0": np.array([[0.0]]), "agent_1": np.array([[1.0]])}
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None]

    def step(self, action):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        reward = {"agent_0": 1, "agent_1": 0}  # Constant reward
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return observation, info


class ConstantRewardContActionsImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))}
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.0]]), "agent_1": np.array([[1.0]])}
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None]

    def step(self, action):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        reward = {"agent_0": 1, "agent_1": 0}  # Constant reward
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return observation, info


class ObsDependentRewardEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[1]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])},
            {"agent_0": np.array([[0.8, 0.2]]), "agent_1": np.array([[0.2, 0.8]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = self.last_obs
        reward = (
            {"agent_0": 1, "agent_1": 0}
            if self.last_obs["agent_0"] == 0
            else {"agent_0": 0, "agent_1": 1}
        )  # Reward depends on observation
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.array([0]), "agent_1": np.array([0])},
                {"agent_0": np.array([1]), "agent_1": np.array([1])},
            ]
        )
        info = {}
        return self.last_obs, info


class ObsDependentRewardImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])},
            {"agent_0": np.array([[0.8, 0.2]]), "agent_1": np.array([[0.2, 0.8]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = self.last_obs
        reward = (
            {"agent_0": 1, "agent_1": 0}
            if np.mean(self.last_obs["agent_0"]) == 0
            else {"agent_0": 0, "agent_1": 1}
        )  # Reward depends on observation
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
            ]
        )
        info = {}
        return self.last_obs, info


class ObsDependentRewardContActionsEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[1]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2]]), "agent_1": np.array([[0.0]])},
            {"agent_0": np.array([[0.8]]), "agent_1": np.array([[0.6]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = self.last_obs
        reward = (
            {"agent_0": 1, "agent_1": 0}
            if self.last_obs["agent_0"] == 0
            else {"agent_0": 0, "agent_1": 1}
        )  # Reward depends on observation
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.array([0]), "agent_1": np.array([0])},
                {"agent_0": np.array([1]), "agent_1": np.array([1])},
            ]
        )
        info = {}
        return self.last_obs, info


class ObsDependentRewardContActionsImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2]]), "agent_1": np.array([[0.0]])},
            {"agent_0": np.array([[0.8]]), "agent_1": np.array([[0.6]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = self.last_obs
        reward = (
            {"agent_0": 1, "agent_1": 0}
            if np.mean(self.last_obs["agent_0"]) == 0
            else {"agent_0": 0, "agent_1": 1}
        )  # Reward depends on observation
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
            ]
        )
        info = {}
        return self.last_obs, info


class DiscountedRewardEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[1]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])},
            {"agent_0": np.array([[0.8, 0.2]]), "agent_1": np.array([[0.2, 0.8]])},
        ]
        self.q_values = [
            {"agent_0": 0.99, "agent_1": 0.495},
            {"agent_0": 1.0, "agent_1": 0.5},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = {"agent_0": np.array([1]), "agent_1": np.array([1])}
        reward = (
            {"agent_0": 1, "agent_1": 0.5}
            if self.last_obs["agent_0"] == 1
            else {"agent_0": 0, "agent_1": 0}
        )  # Reward depends on observation  # Reward depends on observation
        terminated = self.last_obs  # Terminate after second step
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        self.last_obs = {"agent_0": np.array([1]), "agent_1": np.array([1])}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return self.last_obs, info


class DiscountedRewardImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2, 0.8]]), "agent_1": np.array([[0.8, 0.2]])},
            {"agent_0": np.array([[0.8, 0.2]]), "agent_1": np.array([[0.2, 0.8]])},
        ]
        self.q_values = [
            {"agent_0": 0.99, "agent_1": 0.495},
            {"agent_0": 1.0, "agent_1": 0.5},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))}
        reward = (
            {"agent_0": 1, "agent_1": 0.5}
            if np.mean(self.last_obs["agent_0"]) == 1
            else {"agent_0": 0, "agent_1": 0}
        )  # Reward depends on observation  # Reward depends on observation
        terminated = {
            "agent_0": int(np.mean(self.last_obs["agent_0"])),
            "agent_1": int(np.mean(self.last_obs["agent_0"])),
        }  # Terminate after second step
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        self.last_obs = {
            "agent_0": np.ones((1, 3, 3)),
            "agent_1": np.ones((1, 3, 3)),
        }
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return self.last_obs, info


class DiscountedRewardContActionsEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[1]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2]]), "agent_1": np.array([[0.4]])},
            {"agent_0": np.array([[0.8]]), "agent_1": np.array([[0.1]])},
        ]
        self.q_values = [
            {"agent_0": 0.99, "agent_1": 0.495},
            {"agent_0": 1.0, "agent_1": 0.5},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = {"agent_0": np.array([1]), "agent_1": np.array([1])}
        reward = (
            {"agent_0": 1, "agent_1": 0.5}
            if self.last_obs["agent_0"] == 1
            else {"agent_0": 0, "agent_1": 0}
        )  # Reward depends on observation  # Reward depends on observation
        terminated = self.last_obs  # Terminate after second step
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        self.last_obs = {"agent_0": np.array([1]), "agent_1": np.array([1])}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return self.last_obs, info


class DiscountedRewardContActionsImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[0.2]]), "agent_1": np.array([[0.4]])},
            {"agent_0": np.array([[0.8]]), "agent_1": np.array([[0.1]])},
        ]
        self.q_values = [
            {"agent_0": 0.99, "agent_1": 0.495},
            {"agent_0": 1.0, "agent_1": 0.5},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [None, None]

    def step(self, action):
        observation = {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))}
        reward = (
            {"agent_0": 1, "agent_1": 0.5}
            if np.mean(self.last_obs["agent_0"]) == 1
            else {"agent_0": 0, "agent_1": 0}
        )  # Reward depends on observation  # Reward depends on observation
        terminated = {
            "agent_0": int(np.mean(self.last_obs["agent_0"])),
            "agent_1": int(np.mean(self.last_obs["agent_0"])),
        }  # Terminate after second step
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        self.last_obs = {
            "agent_0": np.ones((1, 3, 3)),
            "agent_1": np.ones((1, 3, 3)),
        }
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return self.last_obs, info


class FixedObsPolicyEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(1),
            "agent_1": spaces.Discrete(1),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 1.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])}
        ]

    def step(self, action):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        reward = {
            "agent_0": [1, -1][action["agent_0"]],
            "agent_1": [-1, 1][action["agent_1"]],
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return observation, info


class FixedObsPolicyImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 0.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 0.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 1.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])}
        ]

    def step(self, action):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        reward = {
            "agent_0": [1, -1][action["agent_0"]],
            "agent_1": [-1, 1][action["agent_1"]],
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return observation, info


class FixedObsPolicyContActionsEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(1),
            "agent_1": spaces.Discrete(1),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0]]), "agent_1": np.array([[0.0]])},
        ]
        self.q_values = [
            {"agent_0": 0.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [{"agent_0": np.array([1.0]), "agent_1": np.array([0.0])}]

    def step(self, action):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        reward = {
            "agent_0": -((1 - action["agent_0"]) ** 2),
            "agent_1": -((0 - action["agent_1"]) ** 2),
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        info = {}
        return observation, info


class FixedObsPolicyContActionsImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 0.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 0.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1,)),
            "agent_1": spaces.Box(0.0, 1.0, (1,)),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0]]), "agent_1": np.array([[0.0]])},
        ]
        self.q_values = [
            {"agent_0": 0.0, "agent_1": 0.0}
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [{"agent_0": np.array([1.0]), "agent_1": np.array([0.0])}]

    def step(self, action):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        reward = {
            "agent_0": -((1 - action["agent_0"]) ** 2),
            "agent_1": -((0 - action["agent_1"]) ** 2),
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        observation = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        info = {}
        return observation, info


class PolicyEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 0.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {
            "agent_0": action["agent_0"] == self.last_obs["agent_0"],
            "agent_1": action["agent_1"] != self.last_obs["agent_1"],
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.array([0]), "agent_1": np.array([0])},
                {"agent_0": np.array([1]), "agent_1": np.array([1])},
                {"agent_0": np.array([0]), "agent_1": np.array([1])},
                {"agent_0": np.array([1]), "agent_1": np.array([0])},
            ]
        )
        info = {}
        return self.last_obs, info


class PolicyImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
        ]
        self.q_values = [
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 0.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {
            "agent_0": action["agent_0"] == np.mean(self.last_obs["agent_0"]),
            "agent_1": action["agent_1"] != np.mean(self.last_obs["agent_1"]),
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
            ]
        )
        info = {}
        return self.last_obs, info


class PolicyContActionsEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (2,)),
            "agent_1": spaces.Box(0.0, 1.0, (2,)),
        }
        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 0.0]]), "agent_1": np.array([[0.0, 0.0]])},
            {"agent_0": np.array([[1.0, 1.0]]), "agent_1": np.array([[1.0, 1.0]])},
        ]
        self.q_values = [
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": -2.0, "agent_1": -2.0},
            {"agent_0": -2.0, "agent_1": -2.0},
            {"agent_0": -1.0, "agent_1": -1.0},
            {"agent_0": -1.0, "agent_1": -1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {}
        if self.last_obs["agent_0"]:  # last obs = 1, policy should be [0, 1]
            reward["agent_0"] = -((0 - action["agent_0"][0]) ** 2) - (
                (1 - action["agent_0"][1]) ** 2
            )
        else:  # last obs = 0, policy should be [1, 0]
            reward["agent_0"] = -((1 - action["agent_0"][0]) ** 2) - (
                (0 - action["agent_0"][1]) ** 2
            )
        if self.last_obs["agent_1"]:  # last obs = 1, policy should be [1, 0]
            reward["agent_1"] = -((1 - action["agent_1"][0]) ** 2) - (
                (0 - action["agent_1"][1]) ** 2
            )
        else:  # last obs = 0, policy should be [0, 1]
            reward["agent_1"] = -((0 - action["agent_1"][0]) ** 2) - (
                (1 - action["agent_1"][1]) ** 2
            )
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.array([0]), "agent_1": np.array([0])},
                {"agent_0": np.array([1]), "agent_1": np.array([1])},
                {"agent_0": np.array([0]), "agent_1": np.array([1])},
                {"agent_0": np.array([1]), "agent_1": np.array([0])},
            ]
        )
        info = {}
        return self.last_obs, info


class PolicyContActionsImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Box(0.0, 1.0, (2,)),
            "agent_1": spaces.Box(0.0, 1.0, (2,)),
        }
        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 0.0]]), "agent_1": np.array([[0.0, 0.0]])},
            {"agent_0": np.array([[1.0, 1.0]]), "agent_1": np.array([[1.0, 1.0]])},
        ]
        self.q_values = [
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": 0.0, "agent_1": 0.0},
            {"agent_0": -2.0, "agent_1": -2.0},
            {"agent_0": -2.0, "agent_1": -2.0},
            {"agent_0": -1.0, "agent_1": -1.0},
            {"agent_0": -1.0, "agent_1": -1.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {}
        if np.mean(self.last_obs["agent_0"]):  # last obs = 1, policy should be [0, 1]
            reward["agent_0"] = -((0 - action["agent_0"][0]) ** 2) - (
                (1 - action["agent_0"][1]) ** 2
            )
        else:  # last obs = 0, policy should be [1, 0]
            reward["agent_0"] = -((1 - action["agent_0"][0]) ** 2) - (
                (0 - action["agent_0"][1]) ** 2
            )
        if np.mean(self.last_obs["agent_1"]):  # last obs = 1, policy should be [1, 0]
            reward["agent_1"] = -((1 - action["agent_1"][0]) ** 2) - (
                (0 - action["agent_1"][1]) ** 2
            )
        else:  # last obs = 0, policy should be [0, 1]
            reward["agent_1"] = -((0 - action["agent_1"][0]) ** 2) - (
                (1 - action["agent_1"][1]) ** 2
            )
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
            ]
        )
        info = {}
        return self.last_obs, info


class MultiPolicyEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {"agent_0": np.array([0]), "agent_1": np.array([0])}
        self.observation_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
            {"agent_0": np.array([[0]]), "agent_1": np.array([[1]])},
            {"agent_0": np.array([[1]]), "agent_1": np.array([[0]])},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
        ]
        self.q_values = [
            {"agent_0": 2.0, "agent_1": 2.0},
            {"agent_0": 2.0, "agent_1": 2.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 0.0, "agent_1": 3.0},
            {"agent_0": 0.0, "agent_1": 3.0},
            {"agent_0": 3.0, "agent_1": 0.0},
            {"agent_0": 3.0, "agent_1": 0.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {
            "agent_0": 2 * (action["agent_0"] == self.last_obs["agent_0"])
            + (action["agent_1"] == self.last_obs["agent_1"]),
            "agent_1": 2 * (action["agent_1"] != self.last_obs["agent_1"])
            + (action["agent_0"] != self.last_obs["agent_0"]),
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.array([0]), "agent_1": np.array([0])},
                {"agent_0": np.array([1]), "agent_1": np.array([1])},
                {"agent_0": np.array([0]), "agent_1": np.array([1])},
                {"agent_0": np.array([1]), "agent_1": np.array([0])},
            ]
        )
        info = {}
        return self.last_obs, info


class MultiPolicyImageEnv:
    def __init__(self):
        self.possible_agents = ["agent_0", "agent_1"]
        self.agents = self.possible_agents
        self.max_num_agents = len(self.possible_agents)
        self.num_agents = len(self.agents)

        self.last_obs = {
            "agent_0": np.zeros((1, 3, 3)),
            "agent_1": np.zeros((1, 3, 3)),
        }
        self.observation_space = {
            "agent_0": spaces.Box(0.0, 1.0, (1, 3, 3)),
            "agent_1": spaces.Box(0.0, 1.0, (1, 3, 3)),
        }
        self.action_space = {
            "agent_0": spaces.Discrete(2),
            "agent_1": spaces.Discrete(2),
        }

        self.sample_obs = [
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
            {"agent_0": np.zeros((1, 1, 3, 3)), "agent_1": np.ones((1, 1, 3, 3))},
            {"agent_0": np.ones((1, 1, 3, 3)), "agent_1": np.zeros((1, 1, 3, 3))},
        ]
        self.sample_actions = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[1.0, 0.0]])},
        ]
        self.q_values = [
            {"agent_0": 2.0, "agent_1": 2.0},
            {"agent_0": 2.0, "agent_1": 2.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 1.0, "agent_1": 1.0},
            {"agent_0": 0.0, "agent_1": 3.0},
            {"agent_0": 0.0, "agent_1": 3.0},
            {"agent_0": 3.0, "agent_1": 0.0},
            {"agent_0": 3.0, "agent_1": 0.0},
        ]  # Correct Q values to learn, s x a table
        self.policy_values = [
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
            {"agent_0": np.array([[1.0, 0.0]]), "agent_1": np.array([[1.0, 0.0]])},
            {"agent_0": np.array([[0.0, 1.0]]), "agent_1": np.array([[0.0, 1.0]])},
        ]

    def step(self, action):
        observation = self.last_obs
        reward = {
            "agent_0": 2
            * (np.mean(action["agent_0"]) == np.mean(self.last_obs["agent_0"]))
            + (np.mean(action["agent_1"]) == np.mean(self.last_obs["agent_1"])),
            "agent_1": 2
            * (np.mean(action["agent_1"]) != np.mean(self.last_obs["agent_1"]))
            + (np.mean(action["agent_0"]) != np.mean(self.last_obs["agent_0"])),
        }  # Reward depends on action
        terminated = {"agent_0": True, "agent_1": True}
        truncated = {"agent_0": False, "agent_1": False}
        info = {}
        return observation, reward, terminated, truncated, info

    def reset(self):
        self.last_obs = random.choice(
            [
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.zeros((1, 3, 3)), "agent_1": np.ones((1, 3, 3))},
                {"agent_0": np.ones((1, 3, 3)), "agent_1": np.zeros((1, 3, 3))},
            ]
        )
        info = {}
        return self.last_obs, info


def prepare_ma_states(states, one_hot, state_dims, device="cpu"):
    if one_hot:
        states = {
            agent_id: nn.functional.one_hot(
                torch.Tensor(state).long(), num_classes=state_dim[0]
            )
            .float()
            .squeeze(1)
            .to(device)
            for (agent_id, state), state_dim in zip(states.items(), state_dims)
        }
    else:
        states = {
            agent_id: torch.Tensor(state).to(device)
            for (agent_id, state) in states.items()
        }
    return states


def prepare_ma_actions(actions, device="cpu"):
    actions = {
        agent_id: torch.Tensor(action).to(device)
        for (agent_id, action) in actions.items()
    }
    return actions


def check_policy_q_learning_with_probe_env(
    env, algo_class, algo_args, memory, learn_steps=1000, device="cpu"
):
    print(f"Probe environment: {type(env).__name__}")

    agent = algo_class(**algo_args, vect_noise_dim=1, device=device)

    state, _ = env.reset()
    for _ in range(10000):
        # Make vectorized
        state = {agent_id: np.expand_dims(s, 0) for agent_id, s in state.items()}
        cont_actions, discrete_action = agent.get_action(state, training=True)
        action = discrete_action if agent.discrete_actions else cont_actions
        next_state, reward, done, _, _ = env.step(action)
        reward = {
            agent_id: np.expand_dims(np.array(r), 0) for agent_id, r in reward.items()
        }
        done = {
            agent_id: np.expand_dims(np.array(d), 0) for agent_id, d in done.items()
        }
        mem_next_state = {
            agent_id: np.expand_dims(ns, 0) for agent_id, ns in next_state.items()
        }
        memory.save_to_memory(
            state, cont_actions, reward, mem_next_state, done, is_vectorised=True
        )
        state = next_state
        if done[agent.agent_ids[0]]:
            state, _ = env.reset()

    # Learn from experiences
    for _ in trange(learn_steps):
        experiences = memory.sample(agent.batch_size)

        # Learn according to agent's RL algorithm
        agent.learn(experiences)

    with torch.no_grad():
        for agent_id, actor, critic in zip(
            agent.agent_ids, agent.actors, agent.critics
        ):
            for sample_obs, sample_action, q_values, policy_values in zip(
                env.sample_obs, env.sample_actions, env.q_values, env.policy_values
            ):
                state = prepare_ma_states(
                    sample_obs, agent.one_hot, agent.state_dims, device
                )

                if q_values is not None:
                    action = prepare_ma_actions(sample_action, device)

                    # Stack states and actions
                    if agent.is_image_space:
                        stacked_states = torch.stack(list(state.values()), dim=2)
                    else:
                        stacked_states = torch.cat(list(state.values()), dim=1)

                    stacked_actions = torch.cat(list(action.values()), dim=1)
                    predicted_q_values = (
                        critic(stacked_states, stacked_actions)
                        .detach()
                        .cpu()
                        .numpy()[0]
                    )
                    # print("---")
                    # print(agent_id, "q", q_values[agent_id], predicted_q_values)
                    # assert np.allclose(q_values[agent_id], predicted_q_values, atol=0.1):
                    if not np.allclose(
                        q_values[agent_id], predicted_q_values, atol=0.1
                    ):
                        print(agent_id, "q", q_values[agent_id], predicted_q_values)

                if policy_values is not None:
                    predicted_policy_values = (
                        actor(state[agent_id]).detach().cpu().numpy()[0]
                    )

                    # print(agent_id, "pol", policy_values[agent_id], predicted_policy_values)
                    # assert np.allclose(policy_values[agent_id], predicted_policy_values, atol=0.1)
                    if not np.allclose(
                        policy_values[agent_id], predicted_policy_values, atol=0.1
                    ):
                        print(
                            agent_id,
                            "pol",
                            policy_values[agent_id],
                            predicted_policy_values,
                        )
