# Practice task — Credit card fraud detection

Same format as the device traffic classification task: set a timer for 60 minutes before reading past this line if you want the timed version, no AI coding assistant. If you're short on time, this works just as well as an untimed walkthrough whenever you pick it back up.

## Data provenance
`credit_card_fraud_10k.csv`, downloaded from Kaggle (`miadul/credit-card-fraud-detection-dataset`, Apache-2.0 license). Despite being a real download, the data itself is **synthetically generated** by the dataset's author, not real transactions — worth knowing going in, but it doesn't change how you should approach the task.

## Scenario
You work at a payments company. For each of 10,000 credit card transactions, you have transaction- and cardholder-level features. You want to flag which transactions are fraudulent.

## Data
`credit_card_fraud_10k.csv`, one row per transaction, columns:
- `transaction_id` — unique identifier (not a feature)
- `amount` — transaction amount
- `transaction_hour` — hour of day (0-23)
- `merchant_category` — categorical: Food, Clothing, Travel, Grocery, Electronics
- `foreign_transaction` — 0/1, international transaction
- `location_mismatch` — 0/1, billing vs. transaction location mismatch
- `device_trust_score` — 0-100 trust score of the device used
- `velocity_last_24h` — number of transactions by this cardholder in the last 24h
- `cardholder_age` — age of the cardholder
- `is_fraud` — target: 0 = normal, 1 = fraud (**~1.5% positive — more extreme imbalance than the device traffic task's device-type classes**)

## Task
1. Explore the data. Note anything worth flagging (there's no missing data or injected outliers this time — check that assumption rather than taking it on faith).
2. Build a model to predict `is_fraud`.
3. Evaluate it properly given the class imbalance — think carefully about which metric(s) actually tell you something useful here, and why accuracy alone would be misleading on a ~1.5%-positive target.
4. Handle `merchant_category` properly — this is the first practice dataset with a real categorical feature, so it's a chance to actually use a one-hot encoding step instead of just numeric columns.
5. Identify which features matter most.
6. Prepare a short (5-bullet) summary as if presenting to a team: approach, headline result, one limitation, one thing you'd do with more time.

## Constraints
Stick to the 60-minute budget if doing the timed version. Stop wherever you are and write the summary with what you have.

## After
Come back and walk through it the same way we did for the device traffic classification task.
