# The Three Branches of Machine Learning

1. Supervised Learning

Supervised Learning is a type of machine learning where the data includes both inputs and the correct outputs (labels). The model learns by studying these examples and trying to predict the correct answer for new, unseen data. It is mainly used for problems like classification (predicting categories) and regression (predicting numbers).

2. Unsupervised Learning

Unsupervised Learning is used when the data does not have labeled answers. Instead of predicting a specific output, the model tries to discover hidden patterns or group similar data points together. It helps in understanding the structure of the data and is commonly used for clustering and pattern detection.

3. Reinforcement Learning

Reinforcement Learning is a type of learning where an agent interacts with an environment and learns by receiving rewards or penalties based on its actions. The goal is to maximize the total reward over time. This type of learning is commonly used in areas like robotics, gaming, and autonomous systems.

| Learning Type          | Labels Present?                | Main Goal                          | Example Problems                       |
| ---------------------- | ------------------------------ | ---------------------------------- | -------------------------------------- |
| Supervised Learning    | Yes                            | Predict correct output             | Spam Detection, House Price Prediction |
| Unsupervised Learning  | No                             | Find hidden patterns or clusters   | Customer Segmentation, Market Analysis |
| Reinforcement Learning | No fixed labels (uses rewards) | Learn best actions through rewards | Game AI, Self-Driving Cars             |

Real-World Examples

# Supervised Learning

1. Email detection
2. Credit card fraud detection
3. Disease prediction (like diabetes prediction)

# Unsupervised Learning

1. Customer segmentation in marketing
2. Grouping similar news articles
3. Detecting unusual transactions

# Reinforcement Learning

1. Game-playing AI
2. Robot navigation
3. Self-driving car decision systems

# Why Choosing the Wrong Learning Framework Causes Failure ?

Each Machine Learning type is designed for a specific kind of problem. If you choose the wrong one, the model may run but will not solve the actual objective.

Example: Using Unsupervised Learning for Spam Detection

Spam detection is a Supervised Learning problem because we have emails (input) and labels (Spam / Not Spam).
If we use Unsupervised Learning instead, the model will only group similar emails into clusters. It will not understand what “spam” means because no labels are provided.

As a result, the model cannot directly predict whether an email is spam or not - even though it technically works.