
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset
import time
import math
size = 100000
a = np.arange(size)
b = np.arange(size)
c = a + b


training_examples = {'a':a, 'b':b}
training_targets=c

size = 1000
a = np.random.randint(size, size=size)
b = np.random.randint(size, size=size)
c = a + b


training_examples = {'a':a, 'b':b}
training_targets=c
session = tf.Session()
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):

    ds = tf.data.Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)
    # ds = ds.shuffle(10000)
    features, labels = ds.make_one_shot_iterator().get_next()
    # print(session.run(ds.make_one_shot_iterator().get_next()))
    return features, labels
    # Shuffle the data, if specified.


construct_feature_columns = set(
    [tf.feature_column.numeric_column(my_feature) for my_feature in ["a", "b"]]
)

my_input_fn(training_examples, training_targets, 1)
def train_model(
    learning_rate,
    steps,
    batch_size,
    training_examples,
    training_targets,
    validation_examples,
    validation_targets,
):

    # Create a linear regressor object.
   
    # # session_config = tf.ConfigProto( device_count={'GPU': 0})
    # # run_config = tf.estimator.RunConfig().replace(session_config=session_config)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_feature_columns,
        # config=run_config
    )
    #   session_config = tf.ConfigProto(log_device_placement=True)
    #   run_config = tf.estimator.RunConfig().replace(session_config=session_config)

    # Create input functions.
    training_input_fn = lambda: my_input_fn(
        training_examples, training_targets, batch_size=batch_size
    )

    # Train the model, but do so inside a loop so that we can periodically assess
    # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    print(time.time())
    for _ in range(2):
        linear_regressor.train(input_fn=training_input_fn, steps=steps)
    print(time.time())
    print("Model training finished.")

    return linear_regressor


linear_regressor = train_model(
    learning_rate=0.000001,
    steps=100000,
    batch_size=20,
    training_examples=training_examples,
    training_targets=training_targets,
    validation_examples=training_examples,
    validation_targets=training_targets,
)


size = 10
a = np.random.randint(size, size=size)
b = np.random.randint(size, size=size)
c = a + b



test_examples = {"a":a,"b":b}
predict_test_input_fn = lambda: my_input_fn(
      test_examples, 
      c, 
      num_epochs=1, 
      shuffle=False)

test_predictions = linear_regressor.predict(input_fn=predict_test_input_fn)
# print([v for v in test_predictions])

test_predictions = np.array([item['predictions'][0] for item in test_predictions])
print(c)
print(test_predictions)
root_mean_squared_error = math.sqrt(
    metrics.mean_squared_error(test_predictions, c))

print("Final RMSE (on test data): %0.2f" % root_mean_squared_error)
