.. title: Understanding Shannon Information and Entropy
.. slug: understanding-shannon-information-and-entropy
.. date: 2025-04-02 00:11:30 UTC+07:00
.. tags: probability, entropy, mathjax, information theory
.. category: 
.. link: 
.. description: A introduction to Shannon Information and Entropy.
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

Many materials on this topic start with Claude Shannon’s concept of information. So let’s start with that. |br|
Information, in Shannon's theory, is defined in the context of transferring a message from a source (transmitter) to a receiver over a channel. Imagine tossing a coin. In this scenario, the coin toss outcome acts as the source (transmitter), and you, observing the outcome, are the receiver.

.. TEASER_END

For simplicity, let's assume the coin is fair (equal probability of heads or tails), cannot land on its edge, and is tossed 10 times. We'll also assume that we toss this coin in an ideal environment (so that we will not have noise in the probability distribution of head or tail).

Suppose you initially believe the coin is rigged to land heads 90% of the time. So, when we finish tossing the fair coin, we observe approximately 5 heads and 5 tails. This outcome differs from our initial belief, which makes it surprising and thus, conveys more information to us. As you can imagine, if the coin were actually rigged as believed, the outcome would align with expectations and therefore convey less information.

|H2| Defining Information |H2e|

With that in mind, we can construct a function that quantifies the information of an event, let's call it :math:`I(e)`. This function should have certain desirable properties:

*   It should yield a higher value when the probability of the event :math:`p` is low (more surprise) and a lower value when the probability is high (less surprise).
*   For two independent events, the information gained from observing both should be the sum of the information gained from each individually.

A function that satisfies these properties is the logarithm of the reciprocal of the probability:

.. math::

    I(p) = \log(1/p) = -\log(p) \tag{1}

The base of the logarithm determines the units of information (e.g., base 2 gives bits, base :math:`e` gives nats).

|H2| Defining Entropy |H2e|

Entropy is simply the expected information over all possible events in a probability distribution. For a given discrete probability distribution for a random variable :math:`X` with possible outcomes :math:`x_1, x_2, \ldots, x_n` having probabilities :math:`p_1, p_2, \ldots, p_n`, we define the entropy of :math:`X`, denoted as :math:`H[X]`.

.. math::

    H[X] &= E[I(X)] \\
         &= \sum_{i=1}^n P(x_i)I(x_i) \quad \text{(definition of expected value)} \\
         &= \sum_{i=1}^n p_i \log(1/p_i) \\
         &= -\sum_{i=1}^n p_i \log(p_i) \quad \text{(since } \log(1/p_i) = -\log(p_i) \text{)} \tag{2}

Note: By convention, :math:`0 \log(0) = 0`.

Entropy, then, measures the average unpredictability (or average surprise) of a random variable's outcomes. Higher entropy signifies greater uncertainty, making the outcomes harder to predict on average.