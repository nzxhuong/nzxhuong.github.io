.. title: Variational Autoencoders
.. slug: variational-autoencoders
.. date: 2025-04-12 14:35:36 UTC-04:00
.. tags: mathjax, variational-autoencoders, generative-models
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

This is my learning note from `L4 Latent Variable Models <https://www.youtube.com/watch?v=FMuvUZXMzKM>`__ by Pieter Abbeel. The idea of being able to generate (potentially new) images, songs, or any data type you want with generative models always amazes me. And I just want to share my thoughts on it (mostly Latent Variable Models, LVMs).

.. TEASER_END

Imagine this: we have a bunch of clock pictures. Each with a different background, different time, different number font, etc. And I want to create a model that can generate a picture that seems 'real', like it's part of those original clock pictures. But here is the catch: we need to have a 'seeable' image, so its size should be at least 224x224 grayscale, which is already a huge number of pixels (dimensions). But we might want the model to scale to even Full HD (1920x1080)! Creating a model that learns the distribution :math:`p(x)` over *all* these pixels directly is not effective, maybe even intractable, because we don't know the true form of :math:`p(x)`.

Let’s think about the image in another way. What features does the clock image show? Background, time, number font... How about we just learn those underlying factors, and then recreate the image based on this information? This is the motivation behind Latent Variable Models. We want to learn some low-dimensional latent variables :math:`z` (our hidden factors). The idea is that we can then easily sample :math:`z \sim p(z)` (where :math:`z` is a vector) and use this sampled :math:`z` to sample our data :math:`x \sim p_{\theta}(x|z)`. Nice.


|H2| How Do We Train This Thing? The Log-Likelihood Approach |H2e|

As with many other generative models, we'll use maximum log-likelihood as the objective to maximize over the model parameters :math:`\theta`. We want to maximize the probability of seeing our training data :math:`X = \{x^{(1)}, ..., x^{(N)}\}`:

.. math::

    \max_{\theta} \sum_{i=1}^N \log p_{\theta}(x^{(i)})
    \tag{1}

The probability of a single data point :math:`x` involves marginalizing out the latent variable :math:`z`:

.. math::

    p_{\theta}(x) = \int p_{\theta}(x, z) dz = \int p_{\theta}(x|z) p(z) dz
    \tag{2}

This integral leads to two scenarios for computing the log-likelihood:

1.  **Small `z` range:** If :math:`z` can only take a few discrete values, we can compute the exact likelihood by summing over all possible :math:`z`. The calculation involves computing :math:`\sum_z p_{\theta}(x|z) p(z)`:

    .. math::

        \log p_{\theta}(x) = \log \sum_z p_{\theta}(x|z) p(z)
        \tag{3}

    But this is only possible if we know exactly what :math:`z` represents *and* its range is small. For example, with the clock, maybe we manually define :math:`z_1=1` if it's a wall clock, :math:`z_2=1` if it's broken, etc. (assuming :math:`z` components are binary).

2.  **Large or Continuous `z` range:** In reality, we often need many latent dimensions (:math:`z` might be a 200-dimensional continuous vector!) to capture the richness of the data. Now, the sum (or integral) involving :math:`p_{\theta}(x|z) p(z)` becomes intractable to compute directly.

|H3| The Problem with Naive Monte Carlo Estimation |H3e|

When the sum/integral is intractable, we can try to estimate it using Monte Carlo sampling. We sample :math:`M` values :math:`z^{(m)}` from the prior :math:`p(z)` and approximate the likelihood:

.. math::

    p_{\theta}(x) = E_{z \sim p(z)}[p_{\theta}(x|z)] \approx \frac{1}{M} \sum_{m=1}^M p_{\theta}(x|z^{(m)})
    \tag{4}

So the objective becomes:

.. math::

    \max_{\theta} \sum_{i=1}^N \log \left( \frac{1}{M} \sum_{m=1}^M p_{\theta}(x^{(i)}|z^{(m)}) \right) \quad \text{where } z^{(m)} \sim p(z)
    \tag{5}

If you found that a little bit hard to follow, just remember the expectation formula: :math:`E_{z \sim p(z)}[f(z)] = \int f(z)p(z) dz \approx \frac{1}{M}\sum f(z^{(m)})` for :math:`z^{(m)} \sim p(z)`. Here, :math:`f(z) = p_{\theta}(x|z)`.

This looks convenient at first sight, but in fact, sampling :math:`z` from the *prior* :math:`p(z)` will mostly result in :math:`p_{\theta}(x|z)` being very close to zero for a *specific* :math:`x`! This makes the gradient of the log-likelihood with respect to :math:`\theta` also close to zero, leading to very slow or no learning.

For a more concrete example, let's revisit the MNIST digits (0-9). Imagine our data :math:`x` is an image of a '7'. Our latent :math:`z` ideally encodes "this is a 7". If we just sample :math:`z` randomly from its prior distribution :math:`p(z)` (say, a standard Gaussian), what's the chance that the sampled :math:`z` actually corresponds to a '7'? Probably very low. Most random :math:`z` values will generate images that look nothing like our specific '7', meaning :math:`p_{\theta}(x=\text{'7'}|z_{\text{random}})` will be tiny. The :math:`z` values that *do* generate a '7' live in a very small region of the latent space.

You might say, "So what? Just sample more :math:`z` values!" But remember:
1.  The latent space :math:`z` can be high-dimensional (e.g., 200 dimensions). If each dimension needs to be 'just right' to reconstruct :math:`x`, the probability of randomly sampling a 'good' :math:`z` becomes vanishingly small. If :math:`z` was 200 binary dimensions and each needed to match perfectly with probability 0.5, the chance is :math:`0.5^{200}`, which is practically zero.
2.  We're working with samples to estimate the likelihood. If the chance of sampling a 'good' :math:`z` (one that gives non-negligible :math:`p_{\theta}(x|z)`) is nearly impossible, our likelihood estimate (and its gradient) will be terrible. Ineffective learning is a big no-no in deep learning.

|H2| A Better Way: Focusing the Sampling |H2e|

Now what can we do? The problem is that we're sampling :math:`z` blindly from the prior :math:`p(z)`. What we *really* want are :math:`z` values that are likely to have generated our specific :math:`x`.

|H3| Idea 1: Importance Sampling (Briefly) |H3e|

We could introduce a *proposal* distribution :math:`q(z)` that is designed to give us :math:`z` values relevant to :math:`x`. Then we use importance sampling (for more details, you can refer to my older blog post on PER, though the application is slightly different here). The objective would look like:

.. math::

    \log p_{\theta}(x) &= \log \int p_{\theta}(x|z) p(z) dz \\
                     &= \log \int p_{\theta}(x|z) p(z) \frac{q(z)}{q(z)} dz \\
                     &= \log E_{z \sim q(z)} \left[ \frac{p(z)}{q(z)} p_{\theta}(x|z) \right] \\
                     &\approx \log \left( \frac{1}{M} \sum_{m=1}^M \frac{p(z^{(m)})}{q(z^{(m)})} p_{\theta}(x|z^{(m)}) \right) \quad \text{where } z^{(m)} \sim q(z)
    \tag{6}

So now we ask: which :math:`q(z)` should we choose?

|H3| Idea 2: Variational Inference and the ELBO |H3e|

The intuitive answer is: we want :math:`q(z)` to be close to the true *posterior* distribution :math:`p_{\theta}(z|x) = p_{\theta}(x|z)p(z) / p_{\theta}(x)`. The posterior tells us exactly which :math:`z` values are likely given :math:`x`.

The problem? We can't easily compute or sample from :math:`p_{\theta}(z|x)` because it depends on :math:`p_{\theta}(x)` in the denominator, which is the very intractable quantity we started with!

So, instead of finding the *exact* posterior, we *approximate* it using a simpler, tractable distribution :math:`q(z)`, typically a Gaussian: :math:`q(z) \approx p_{\theta}(z|x)`. We want to make :math:`q(z)` as close as possible to the true posterior, usually by minimizing the Kullback-Leibler (KL) divergence between them: :math:`KL(q(z) || p_{\theta}(z|x))`.

If we did this by finding a separate :math:`q(z)` for *each* data point :math:`x^{(i)}`, it would be computationally expensive. So, people introduced **Amortized Inference**: we use a single neural network, often called the **encoder** or **inference network**, parameterized by :math:`\phi`, to predict the parameters of :math:`q` for *any* given :math:`x`. We denote this distribution as :math:`q_{\phi}(z|x)`. Now our goal is to minimize the KL divergence *on average* over our data:

.. math::

    \min_{\phi, \theta} \sum_{i=1}^N KL(q_{\phi}(z|x^{(i)}) || p_{\theta}(z|x^{(i)}))
    \tag{7}

(If you find it confusing due to the different :math:`q`'s: :math:`q(z)` was the general idea, :math:`q_{\phi}(z|x)` is the practical neural network implementation that approximates the true posterior :math:`p_{\theta}(z|x)`, which we can't compute directly).

Using a single :math:`q_{\phi}(z|x)` network is faster, but it comes with a catch: it's an approximation. We're making two approximations:
1.  The family of distributions for :math:`q` (e.g., Gaussian) might not match the true posterior's shape.
2.  We're using the *same* parameters :math:`\phi` (in the network) to generate :math:`q` for all :math:`x`, which might limit flexibility compared to finding an optimal :math:`q` for each :math:`x` individually.

Now, let's expand the KL divergence (dropping the sum over :math:`i` and :math:`(i)` superscripts for now, just considering one :math:`x`):

.. math::

    KL(q_{\phi}(z|x) || p_{\theta}(z|x)) &= E_{z \sim q_{\phi}(z|x)} \left[ \log \frac{q_{\phi}(z|x)}{p_{\theta}(z|x)} \right] \\
    &= E_{z \sim q_{\phi}} \left[ \log q_{\phi}(z|x) - \log p_{\theta}(z|x) \right] \\
    &= E_{z \sim q_{\phi}} \left[ \log q_{\phi}(z|x) - \log \frac{p_{\theta}(x|z)p(z)}{p_{\theta}(x)} \right] \\
    &= E_{z \sim q_{\phi}} \left[ \log q_{\phi}(z|x) - \log p_{\theta}(x|z) - \log p(z) + \log p_{\theta}(x) \right] \\
    &= E_{z \sim q_{\phi}} \left[ \log q_{\phi}(z|x) - \log p_{\theta}(x|z) - \log p(z) \right] + \log p_{\theta}(x)
    \tag{8}

We pulled :math:`\log p_{\theta}(x)` out of the expectation because it doesn't depend on :math:`z`. Now rearrange this equation to isolate the intractable log-likelihood :math:`\log p_{\theta}(x)`:

.. math::

    \log p_{\theta}(x) = E_{z \sim q_{\phi}} \left[ \log p_{\theta}(x|z) \right] - E_{z \sim q_{\phi}} \left[ \log q_{\phi}(z|x) - \log p(z) \right] + KL(q_{\phi}(z|x) || p_{\theta}(z|x))
    \tag{9}

Recognize the second expectation term as another KL divergence:

.. math::

    E_{z \sim q_{\phi}} \left[ \log \frac{q_{\phi}(z|x)}{p(z)} \right] = KL(q_{\phi}(z|x) || p(z))
    \tag{10}

So we have:

.. math::

    \log p_{\theta}(x) = \underbrace{E_{z \sim q_{\phi}} \left[ \log p_{\theta}(x|z) \right] - KL(q_{\phi}(z|x) || p(z))}_{\text{ELBO}(x; \theta, \phi)} + KL(q_{\phi}(z|x) || p_{\theta}(z|x))
    \tag{11}

Since KL divergence is always non-negative (:math:`KL(...) \ge 0`), we have:

.. math::

    \log p_{\theta}(x) \ge E_{z \sim q_{\phi}} \left[ \log p_{\theta}(x|z) \right] - KL(q_{\phi}(z|x) || p(z))
    \tag{12}

The right-hand side is called the **Evidence Lower Bound (ELBO)**. Maximizing the ELBO with respect to both :math:`\theta` (decoder parameters) and :math:`\phi` (encoder parameters) serves two purposes:
1.  It pushes up the lower bound on the true log-likelihood :math:`\log p_{\theta}(x)`, which is what we originally wanted to maximize.
2.  It implicitly minimizes the :math:`KL(q_{\phi}(z|x) || p_{\theta}(z|x))` term, making our approximation :math:`q_{\phi}` closer to the true posterior.

This ELBO is the standard objective function used for Variational Autoencoders (VAEs). The derivation might seem long, but understanding it helps see *why* this objective makes sense.

|H3| Why "Autoencoder"? |H3e|

You might wonder why this is called an "Autoencoder". It's because of the structure of the :math:`ELBO` objective:

*   :math:`E_{z \sim q_{\phi}} \left[ \log p_{\theta}(x|z) \right]`: This term encourages the **decoder** :math:`p_{\theta}(x|z)` to reconstruct the original input :math:`x` from the latent code :math:`z` produced by the **encoder** :math:`q_{\phi}(z|x)`. This is often called the **reconstruction loss**. (For continuous data like images with Gaussian likelihood, this term often simplifies to a squared error :math:`||x - \mu_{\text{decoder}}(z)||^2`, ignoring constants).
*   :math:`- KL(q_{\phi}(z|x) || p(z))`: This term acts as a **regularizer**. It encourages the distribution produced by the encoder (:math:`q_{\phi}(z|x)`) to stay close to the prior :math:`p(z)` (usually a standard Gaussian :math:`\mathcal{N}(0, I)`). This prevents the encoder from just assigning a unique delta-function-like :math:`z` to each :math:`x`, forcing the latent space to be somewhat smooth and structured.

|H2| One More Trick: Reparameterization |H2e|

We want to maximize the :math:`ELBO` using gradient ascent (or minimize the negative :math:`ELBO` with gradient descent). Let's look at the objective again:

.. math::

    ELBO = E_{z \sim q_{\phi}(z|x)} \left[ \log p_{\theta}(x|z) \right] - KL(q_{\phi}(z|x) || p(z))
    \tag{13}

We need to compute gradients with respect to :math:`\phi` (encoder) and :math:`\theta` (decoder). The gradient for :math:`\theta` is straightforward: :math:`\nabla_\theta E_{z \sim q_{\phi}}[\log p_{\theta}(x|z)] = E_{z \sim q_{\phi}}[\nabla_\theta \log p_{\theta}(x|z)]`, which can be approximated by sampling :math:`z` from :math:`q_{\phi}`.

But the gradient for :math:`\phi` is tricky! The expectation :math:`E_{z \sim q_{\phi}}[...]` depends on :math:`\phi` *through the distribution we sample from*. Taking the gradient :math:`\nabla_\phi E_{z \sim q_{\phi}}[f(z)]` is hard because the sampling operation :math:`z \sim q_{\phi}` is generally not differentiable.

No worries though, the **reparameterization trick** comes to save us! If :math:`q_{\phi}(z|x)` is a distribution that can be reparameterized (like a Gaussian), we can rewrite the sampling process. For a Gaussian :math:`q_{\phi}(z|x) = \mathcal{N}(z; \mu_{\phi}(x), \Sigma_{\phi}(x))`, instead of sampling :math:`z` directly, we can:
1. Sample a noise variable :math:`\epsilon` from a simple, fixed distribution, like :math:`\epsilon \sim \mathcal{N}(0, I)`.
2. Transform this noise using the parameters predicted by the encoder: :math:`z = \mu_{\phi}(x) + L_{\phi}(x) \epsilon`, where :math:`L_{\phi}(x)` is a matrix such that :math:`L L^T = \Sigma` (e.g., :math:`L = \text{diag}(\sigma_{\phi}(x))` if :math:`\Sigma` is diagonal).

Now the expectation becomes:

.. math::

    E_{z \sim q_{\phi}(z|x)} [f(z)] = E_{\epsilon \sim \mathcal{N}(0,I)} [f(\mu_{\phi}(x) + L_{\phi}(x) \epsilon)]
    \tag{14}

The stochasticity is now outside the function, and we can backpropagate gradients through the deterministic transformation :math:`\mu_{\phi}(x) + L_{\phi}(x) \epsilon` with respect to :math:`\phi`!

The overall flow becomes:
Input :math:`x` -> Encoder :math:`q_{\phi}(z|x)` -> Predict params :math:`\mu, \sigma` (or :math:`L`) -> Sample :math:`\epsilon \sim \mathcal{N}(0,I)` -> Compute :math:`z = \mu + \sigma\epsilon` -> Decoder :math:`p_{\theta}(x|z)` -> Predict reconstruction params (e.g., :math:`\mu_{x|z}`) -> Compute Loss (Reconstruction + KL).

|H2| Implementation Example: MNIST VAE |H2e|

Let's build a VAE trained on MNIST.
*   **Encoder** :math:`q_{\phi}(z|x)`: We'll choose a multivariate Gaussian with a diagonal covariance matrix. The encoder network takes :math:`x` and outputs the mean vector :math:`\mu` and the log of the diagonal variances :math:`\log(\sigma^2)`.
    
    *   Why :math:`\log(\sigma^2)`? We need the variance :math:`\sigma^2` to be positive. By predicting :math:`\log(\sigma^2)`, we can exponentiate it (:math:`\exp(\log(\sigma^2)) = \sigma^2`) to get a positive value, even if the network outputs a negative number. This is numerically more stable than predicting :math:`\sigma` directly and squaring it.

*   **Prior** :math:`p(z)`: Standard Gaussian :math:`\mathcal{N}(0, I)`.
*   **Decoder** :math:`p_{\theta}(x|z)`: Since MNIST pixels are often treated as binary (0 or 1), we can use a Bernoulli distribution for each output pixel :math:`k`. The decoder network takes :math:`z` and outputs a vector :math:`p` of probabilities, where :math:`p_k` is the probability that pixel :math:`k` is 1.

    .. math::

        p_{\theta}(x|z) = \prod_k p_k^{x_k} (1 - p_k)^{1 - x_k}
        \tag{15}

    The reconstruction term in the :math:`ELBO` is :math:`E_{z \sim q_{\phi}}[\log p_{\theta}(x|z)]`. The log-likelihood for a single :math:`x` and :math:`z` is:

    .. math::

        \log p_{\theta}(x|z) = \sum_k \left[ x_k \log p_k + (1 - x_k) \log(1 - p_k) \right]
        \tag{16}
    
    This is exactly the negative of the **Binary Cross-Entropy (BCE)** loss between the input :math:`x` and the reconstructed probabilities :math:`p`. So, maximizing this term is equivalent to minimizing the :math:`BCE` loss.
*   **KL Term**: The KL divergence between the encoder's output :math:`q_{\phi}(z|x) = \mathcal{N}(z; \mu, \text{diag}(\sigma^2))` and the prior :math:`p(z) = \mathcal{N}(z; 0, I)` has a convenient analytical form [1]_:

    .. math::

        KL(q_{\phi}(z|x) || p(z)) = \frac{1}{2} \sum_{j=1}^{\dim(z)} \left( \sigma_j^2 + \mu_j^2 - \log(\sigma_j^2) - 1 \right)
        \tag{17}

*   **Total Loss** (to minimize): :math:`\text{Loss} = \text{BCE}(x, p) + KL(q_{\phi}(z|x) || p(z))`

|br|

I put together a `notebook <https://github.com/nzxhuong/learnin_testin/blob/main/Notebooks/Simple_Pytorch_Variational_Autoencoder.ipynb>`__ (there's a typo in the notebook, just ignore it pls!) using PyTorch to build this VAE. The notebook adapts the implementation by `dfdazac <https://dfdazac.github.io/01-vae.html>`__.

The figure below shows a sample of digits I generated using 20 latent variables (:math:`z`):

.. figure:: /images/vae_samples.png
    :height: 350px
    :alt: MNIST digits generated from a variational autoencoder model
    :align: center

    MNIST digits generated from a variational autoencoder model.

Tbh, my cat could paint better handwriting with a brush. Some of the digits have a decent shape, but most are weird ones (maybe stuck between digit types in the latent space, or just not trained long enough?).

I hope you enjoyed the post, I know I did enjoy writing (and learning) it!

|br|

.. [1] The derivation for the :math:`KL` divergence between two multivariate Gaussians can be found in the original VAE paper or many online resources.
