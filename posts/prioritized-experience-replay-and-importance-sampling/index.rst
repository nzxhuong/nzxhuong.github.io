.. title: Prioritized Experience Replay and Importance Sampling
.. slug: prioritized-experience-replay-and-importance-sampling
.. date: 2025-04-02 09:31:56 UTC-04:00
.. tags: reinforcement learning, importance sampling, prioritized experience replay, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

.. |br| raw:: html

   <br />

.. |H2| raw:: html

   <br/><h3>

.. |H2e| raw:: html

   </h3>

.. |H3| raw:: html

   <h4>

.. |H3e| raw:: html

   </h4>

.. |center| raw:: html

   <center>

.. |centere| raw:: html

   </center>

Before diving into importance sampling and prioritized experience, we should be on the same page. In Deep Reinforcement Learning, especially in algorithms like Deep Q-Networks (DQN), we often use an Experience Replay buffer. This buffer stores past transitions experienced by the agent, typically tuples of (State :math:`S`, Action :math:`A`, Reward :math:`R`, Next State :math:`S'`, Done flag :math:`d`). During training, we sample mini-batches of these transitions from the buffer to update the agent's policy or value function.

The standard approach is to sample transitions *uniformly* at random from the replay buffer. If the buffer contains :math:`N` transitions, each transition has a probability of :math:`1/N` (or :math:`b/N` for a mini-batch of size :math:`b`) of being selected. While simple and effective in breaking correlations between consecutive experiences, uniform sampling treats all transitions as equally important. However, some transitions might be much more informative or surprising to the agent than others, potentially offering a greater learning opportunity. Uniform sampling means these crucial transitions might be sampled rarely, especially in large buffers, potentially slowing down learning. This post explores Prioritized Experience Replay (PER), a technique designed to address this by sampling important transitions more frequently, using the mathematical framework of Importance Sampling.

.. TEASER_END

As mentioned, the replay buffer stores transitions :math:`(S_t, A_t, R_{t+1}, S_{t+1}, d_{t+1})`. Uniform sampling gives every stored experience an equal chance of being used for learning updates. Consider a scenario where the agent encounters a rare but highly informative event (e.g., receiving an unexpectedly large reward or penalty). Such transitions can significantly impact the agent's understanding of the environment. However, if the buffer holds thousands or millions of transitions, these critical experiences might only be sampled occasionally under a uniform strategy, hindering efficient learning. We want a way to focus the learning process on the transitions that offer the most potential for improvement.

Importance Sampling is a technique that allows us to estimate the expectation of a function with respect to one probability distribution (:math:`p(x)`), while drawing samples from a *different* probability distribution (:math:`q(x)`).

Suppose we want to compute the expected value of a function :math:`f(x)` where :math:`x` is drawn from distribution :math:`p(x)`:

.. math::

    E_{x \sim p}[f(x)] = \sum_x p(x)f(x) \quad \text{(for discrete x)}

If we have another distribution :math:`q(x)` defined over the same domain, such that :math:`q(x) > 0` whenever :math:`p(x)f(x) \neq 0`, we can rewrite the expectation:

.. math::

    E_{x \sim p}[f(x)] &= \sum_x p(x)f(x) \\
                      &= \sum_x \frac{q(x)}{q(x)} p(x)f(x) \\
                      &= \sum_x q(x) \frac{p(x)}{q(x)} f(x) \\
                      &= E_{x \sim q}\left[ \frac{p(x)}{q(x)} f(x) \right]

The term :math:`w(x) = \frac{p(x)}{q(x)}` is called the **importance weight**. It corrects for the bias introduced by sampling from :math:`q(x)` instead of :math:`p(x)`.

We can estimate these expectations using samples from :math:`p` or :math:`q`:

*   Sampling from :math:`p`: :math:`E_{x \sim p}[f(x)] \approx \frac{1}{n} \sum_{i=1}^n f(x_i)`, where :math:`x_i \sim p`.
*   Sampling from :math:`q`: :math:`E_{x \sim p}[f(x)] \approx \frac{1}{n} \sum_{i=1}^n \frac{p(x_i)}{q(x_i)} f(x_i) = \frac{1}{n} \sum_{i=1}^n w(x_i) f(x_i)`, where :math:`x_i \sim q`.

This gives us a tool to sample transitions non-uniformly (:math:`q`) while still correctly estimating the objective function defined under uniform sampling (:math:`p`). The next step is to define a suitable non-uniform distribution :math:`q` for our replay buffer.

PER aims to sample transitions from the replay buffer based on their "importance" or "priority". A common measure of importance is the magnitude of the **Temporal Difference (TD) error**, which reflects how "surprising" a transition is to the current value function estimate. For a transition :math:`i = (s, a, r, s')`, the TD error :math:`\delta_i` in DQN is:

.. math::

    \delta_i = r + \gamma \max_{a'} Q(s', a'; \theta^{-}) - Q(s, a; \theta)

where:

*   :math:`Q(s, a; \theta)` is the Q-value estimated by the main network with parameters :math:`\theta`.
*   :math:`Q(s', a'; \theta^{-})` is the Q-value estimated by the target network with parameters :math:`\theta^{-}`.
*   :math:`\gamma` is the discount factor.
*   A large absolute TD error :math:`|\delta_i|` suggests that the Q-value prediction for :math:`(s, a)` was inaccurate and the transition offers a significant learning opportunity.

If you unfamiliar with all the terms above, i'm highly recommend you to watch the video of `Value Function Approximation <https://www.youtube.com/watch?v=UoPei5o4fps>`__ by David Silver, great video. 

Given the TD error :math:`|\delta_i|` for each transition :math:`i` in the buffer, we need to convert these errors into sampling probabilities :math:`q(i)`. Two common methods proposed by DeepMind are:

1.  **Proportional Prioritization:** The priority :math:`p_i` of transition :math:`i` is directly related to its TD error:

    .. math::

        p_i = |\delta_i| + \epsilon

    where :math:`\epsilon` is a small positive constant to ensure that all transitions have a non-zero priority. 

2.  **Rank-Based Prioritization:** Priorities are assigned based on the rank of the transition when sorted by :math:`|\delta_i|` in descending order:

    .. math::

        p_i = \frac{1}{\text{rank}(i)}

    where :math:`\text{rank}(i)` is the rank of transition :math:`i` (starting from 1 for the highest :math:`|\delta_i|`). This method is less sensitive to outliers in TD error magnitudes compared to the proportional method.

Once priorities :math:`p_i` are assigned to all :math:`N` transitions in the buffer, the probability :math:`q(i)` of sampling transition :math:`i` is calculated by normalizing the priorities:

.. math::

    q(i) = \frac{p_i}{\sum_{j=1}^N p_j}

Sampling is typically done using these probabilities, often implemented efficiently using data structures like SumTrees.


Now we put everything together. The standard DQN objective minimizes the expected squared TD error, assuming uniform sampling (:math:`p(i) = 1/N`):

.. math::

    L(\theta) = E_{(s,a,r,s') \sim U(D)} [ \delta_i^2 ] = E_{i \sim p} [ \delta_i^2 ]

When sampling with non-uniform probabilities :math:`q(i)` from PER, we must use importance sampling weights to correct the bias. The loss function becomes:

.. math::

    L(\theta) = E_{i \sim q} [ w_i \delta_i^2 ]

The importance weight :math:`w_i` for transition :math:`i` is:

.. math::

    w_i = \frac{p(i)}{q(i)} = \frac{1/N}{q(i)} = \frac{1}{N \cdot q(i)}

The gradient update for the DQN parameters :math:`\theta` using a mini-batch of size :math:`b` sampled according to :math:`q(i)` is then:

.. math::

    \Delta \theta = \frac{1}{b} \sum_{i \in \text{batch}} w_i \delta_i \nabla_\theta Q(s_i, a_i; \theta)

We then update the parameters of the model using the gradient above with some optimizer (e.g., Adam, RMSProp). But there are a few things to note:
Some time the magnitude of TD-error can be very large, which can lead to large importance weights. This can cause instability in training. To mitigate this, we can use a parameter :math:`\alpha` to scale the importance weights where :math:`\alpha \in [0, 1]`:

.. math::

    p_i = |\delta_i|^\alpha + \epsilon

For the importance weights, we can do the same trick with a parameter :math:`\beta` to scale the importance weights where :math:`\beta \in [0, 1]`:

.. math::

    w_i = \left( \frac{p(i)}{q(i)} \right)^\beta


Prioritized Experience Replay provides a mechanism to focus learning on the most informative transitions by sampling them more frequently than uniform random sampling would dictate. By combining this prioritized sampling strategy with Importance Sampling weights, PER can significantly accelerate learning and improve the performance of Deep Reinforcement Learning agents like DQN, demonstrating the power of moving beyond simple uniform sampling in experience replay.

In the future, there might be a post on how to implement PER in PyTorch.

|H2| Further Reading |H2e|

*   Original PER Paper: Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2015). Prioritized Experience Replay. `arXiv:1511.05952 <https://arxiv.org/abs/1511.05952>`__.
*   Wikipedia: `Importance Sampling <https://en.wikipedia.org/wiki/Importance_sampling>`__

|br|