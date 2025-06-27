# Calories Burnt Prediction Analysis

This notebook analyzes the relationship between various physical attributes and calories burned during exercise.

## Setup and Data Loading
```python
# Cell 1: Import necessary libraries
- pandas: For data manipulation
- numpy: For numerical operations
- matplotlib.pyplot: For data visualization
- seaborn: For statistical visualization
- sklearn components: For model training and evaluation
```

```python
# Cell 2: Load and display data
- Reads the merged exercise data CSV file
- Displays first few rows
- Shows total number of rows in dataset
```

## Data Cleaning and Exploration
```python
# Cell 3-4: Clean data and check dimensions
- Removes rows with missing calorie values
- Displays shape of cleaned dataset
```

```python
# Cell 5-6: Statistical Analysis
- Displays summary statistics of numerical columns
- Shows dataset information including data types
```

## Data Visualization
```python
# Cell 7: Height vs Weight Analysis
- Creates a scatter plot comparing height and weight
```

```python
# Cell 8: Feature Analysis
- Creates 4 scatter plots showing relationships between:
  * Age vs Calories
  * Height vs Calories
  * Weight vs Calories
  * Duration vs Calories
- Uses random sample of 1000 points for better visualization
```

```python
# Cell 9: Distribution Analysis
- Creates distribution plots for all numerical features
- Shows the spread of values across different variables
```

## Model Training and Evaluation
```python
# Cell 10: Data Preparation
- Separates features and target variable
- Splits data into training (90%) and validation (10%) sets
```

```python
# Cell 11: Model Training
- Performs one-hot encoding on categorical variables
- Trains a Linear Regression model
- Evaluates model performance using Mean Absolute Error on:
  * Training data
  * Validation data
```

### Key Features
- Uses sci-kit learn's LinearRegression
- Handles categorical variables through one-hot encoding
- Implements train-test split for validation
- Includes comprehensive data visualization
- Provides error metrics for model evaluation

### Dataset Columns
- User_ID: Unique identifier for each user
- Age: User's age
- Height: User's height
- Weight: User's weight
- Duration: Exercise duration
- Gender: User's gender
- Calories: Target variable (calories burned)