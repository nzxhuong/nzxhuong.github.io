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

During the time I’m learning about Deep Q-Learning (DQN), I was stumbling on one thought: with experience replay, we sample transitions in the buffer uniformly. But the way we append *every* transition means it's likely that most of the transitions are 'bad' experiences, especially early on. Like in the cliff walking problem, early in training we're just running around randomly and falling off the cliff a lot. This leads to the buffer being mostly filled with bad outcomes. Even when we *do* finally reach the goal and get a good transition, it's drowned out by the huge amount of bad stuff we already stored. This means most of the time we're sampling 'bad' experiences during training updates, and that doesn't feel very efficient.

So I started thinking... is there a way to sample more of the 'good' stuff? That's when I found Prioritized Experience Replay (PER), proposed by DeepMind.

.. TEASER_END

|H2| What Makes an Experience 'Good' (or 'Bad')? |H2e|

But what *is* a 'good' or 'bad' experience? We need a metric to measure this. You could define this however you want, really, but we'll stick to the one proposed by DeepMind: the magnitude of the TD-error. (There are other cool ideas, like using entropy as proposed in "Uncertainty Prioritized Experience Replay" - sounds neat, maybe a future post topic!).

The TD-error for standard DQN is:

.. math::

    \delta_i = r_t + \gamma \max_{a'} Q_{\theta^-}(s_{t+1}, a') - Q_{\theta}(s_t, a_t)
    \tag{1}

(Unfamiliar with this equation? Check out David Silver's lecture on `Value Function Approximation <https://www.youtube.com/watch?v=UoPei5o4fps>`__ – it's great!)

We then just take the absolute value (magnitude) of the TD-error to get the priority for a transition `i`. We add a small constant `ϵ` to ensure no transition has zero probability of being sampled:

.. math::

    p_i = |\delta_i| + \epsilon
    \tag{2}

This method is called "proportional" prioritization. There's another way called "rank-based", but we won't cover it here.

|H3| From Priority to Probability |H3e|

Okay, now we have priorities `p_i` for each transition. We need a way to actually *sample* based on these priorities, meaning we need a probability distribution. A simple way to construct one is:

.. math::

    P(i) = \frac{p_i^\alpha}{\sum_k p_k^\alpha}
    \tag{3}

Here, `0 <= α <= 1` is a hyperparameter that controls how much prioritization we use. If `α = 0`, we get back to uniform sampling. If `α = 1`, we sample purely based on the priorities `p_i`. Using a value between 0 and 1 helps smooth things out, ensuring that transitions with very high priority don't completely dominate the sampling process.

|H2| Oops, We Introduced Bias! Enter Importance Sampling |H2e|

Now we're sampling the 'good' (high TD-error) transitions more often. Awesome! But... this introduces bias. Because we're *not* sampling uniformly anymore, the updates we make might skew towards these high-error transitions, potentially leading the network to not generalize well across all possible scenarios it might encounter. We've changed the distribution we're drawing samples from!

Luckily, there's a standard technique to correct for this kind of bias: Importance Sampling (IS).

Importance Sampling is a technique that lets us estimate the expected value of a function `f(x)` under one probability distribution `p(x)`, even when we're drawing samples `x` from a *different* probability distribution `q(x)`.

Suppose we want to compute `E_p[f(x)]` (the expected value of `f(x)` where `x` is drawn from `p(x)`), assuming discrete `x` for simplicity:

.. math::

    E_p[f(x)] = \sum_x p(x) f(x)

Here's the trick: we multiply and divide by `q(x)` inside the sum:

.. math::

    E_p[f(x)] &= \sum_x p(x) f(x) \\
              &= \sum_x \frac{q(x)}{q(x)} p(x) f(x) \\
              &= \sum_x q(x) \frac{p(x)}{q(x)} f(x) \\
              &= E_q\left[ \frac{p(x)}{q(x)} f(x) \right]
    \tag{4}

Look at that! With a simple manipulation, we can now estimate the expectation using samples drawn from `q(x)` instead of `p(x)`. The term `w = p(x) / q(x)` is called the importance weight. It tells us how to adjust the contribution of each sample `x ~ q(x)` to correct for the fact that we didn't sample it from `p(x)`.

|H3| Putting IS into DQN |H3e|

How do we actually *use* this weight `w_i` in DQN? And what *are* `p(x)` and `q(x)` in our case?

*   `q(x)` is the prioritized distribution we sample from, `P(i)` from Equation 3.
*   `p(x)` is the distribution we *should* have been sampling from for an unbiased estimate, which is the uniform distribution over the replay buffer. If the buffer has size `N`, then `p(i) = 1/N` for all `i`.

So, the importance weight for transition `i` is:

.. math::

    w_i = \frac{p(i)}{q(i)} = \frac{1/N}{P(i)} = \frac{1}{N \cdot P(i)}
    \tag{5}

To give us more control, especially during training, another hyperparameter `β` (usually annealed from an initial value `β_0` up to 1 over training) is introduced:

.. math::

    w_i = \left( \frac{1}{N \cdot P(i)} \right)^\beta
    \tag{6}

This `β` controls how much correction we apply. When `β = 1`, we fully correct for the bias. When `β = 0`, we don't correct at all. Annealing `β` towards 1 helps stabilize training early on when estimates might be noisy.

Recall the objective (loss function) of DQN is basically minimizing the expected squared TD-error:

.. math::

    L(\theta) = E\left[ \delta_i^2 \right] = E\left[ (r_t + \gamma \max_{a'} Q_{\theta^-}(s_{t+1}, a') - Q_{\theta}(s_t, a_t))^2 \right]
    \tag{7}

Normally, we'd approximate this expectation using a mini-batch of size `b` sampled *uniformly* and perform gradient descent:

.. math::

    \theta \leftarrow \theta - \eta \nabla_\theta L(\theta)

With PER, we sample according to `P(i)` and use importance sampling weights. The loss for a mini-batch becomes a *weighted* average:

.. math::

    L(\theta) \approx \frac{1}{b} \sum_{i=1}^b w_i \cdot \delta_i^2
    \tag{8}

So, when we calculate the gradient of this loss with respect to the network parameters `θ`, the weight `w_i` just comes along for the ride (treating `w_i` as a constant for this specific gradient step):

.. math::

    \nabla_\theta L(\theta) &\approx \nabla_\theta \left( \frac{1}{b} \sum_{i=1}^b w_i \cdot \delta_i^2 \right) \\
               &= \frac{1}{b} \sum_{i=1}^b w_i \cdot \nabla_\theta (\delta_i^2) \\
               &= \frac{1}{b} \sum_{i=1}^b w_i \cdot 2 \delta_i \cdot \nabla_\theta (\delta_i) \\
               &= \frac{1}{b} \sum_{i=1}^b w_i \cdot 2 \delta_i \cdot \nabla_\theta (r_t + \gamma \max_{a'} Q_{\theta^-}(s_{t+1}, a') - Q_{\theta}(s_t, a_t)) \\
               &= \frac{1}{b} \sum_{i=1}^b w_i \cdot 2 \delta_i \cdot (- \nabla_\theta Q_{\theta}(s_t, a_t)) \\
               &= -\frac{2}{b} \sum_{i=1}^b w_i \delta_i \nabla_\theta Q_{\theta}(s_t, a_t)
    \tag{9}

Comparing this to the gradient for standard DQN (which is the same formula without the `w_i`), we see the only difference is that we multiply the gradient contribution of *each transition* `i` in the mini-batch by its corresponding importance sampling weight `w_i`! Pretty straightforward, right?

|br|
I'll stop here for now. This post just focuses on the math and the core idea behind PER. The implementation details (like how to efficiently sample based on priorities and update them) will be the story for a future post.
