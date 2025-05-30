# Car Price Prediction

## Project Description
Predicts Used Car Prices of cars in the USA.

## Results
TODO

### Name & URL
| Name          | URL |
|--------------|----|
| Huggingface  | [Huggingface Space]() |
| Code         | [GitHub Repository](https://github.com/graf-tim/end-to-end-application) |

## Data Sources and Features Used Per Source
| Data Source | Features |
|-------------|----------|
| [Kaggle Craigslist Car Sales Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) | test1, test2 |
| [Kaggle Car Features and MSRP](https://www.kaggle.com/datasets/CooperUnion/cardataset) | test1, test2 |

## Features Created
| Feature | Description |
|---------|-------------|
| manufacturer | One hot encoding of feature manufacturer |
| model | One hot encoding of feature model |
| Engine HP | Horsepower of the car. Merged with other dataset |
| price_per_hp | Price / hp (not used!) |
| age | 2025 - year (not used!) |
| age_cat_encoded | age splitted into groups |
| condition_good | one hot encoding of condition. (not used!) |
| model_group | grouping of only top 20 models (not used!) |
| type | one hot encoding of type. Coupe, SUV, etc.. |
| transmission | one hot encoding of transmission. Automatic / manual / other |

## Model Training
### Amount of Data
- Total of 100'000 Car Listings, limited by Car Feature Dataset to 4592

### Data Splitting Method (Train/Validation/Test)
- 80/20 Train/Test split.

### performance
| It. Nr | Model | Performance | Features | Description |
|--------|--------|-------------|------------|---------------|
| 1 | Linear Regression | Train: 0.09, Test: 0.10, <br>Train RMSE: 10810, Test RMSE: 10630 | `year, odometer` | TODO |
| 2 | Random Forest | Train: 0.86, Test: 0.36, <br>Train RMSE: 4093, Test RMSE: 8954 | Same as It. 1 | TODO |
| 3 | Linear Regression | Train: 0.59, Test: 0.44, <br>Train RMSE: 7192, Test RMSE: 8405 | Added `manufacturer, model` | TODO |
| 4 | Random Forest | Train: 0.94, Test: 0.67, <br>Train RMSE: 2618, Test RMSE: 6447 | Same as lt. 3 | TODO |
| 5 | Random Forest | Mean RMSE: -6584.2 | Same as It. 3 | TODO |
| 6 | Random Forest | Mean RMSE: -6445.6| Added `Engine HP` | TODO |
| 7 | Random Forest | Mean RMSE: -706.0 | Added `price_per_hp` | Used price_per_hp, making it unrealistic |
| 8 | Random Forest | Mean RMSE: -6452.2 | Added `age` | leicht verschlechtert, wieder entfernt|
| 9 | Random Forest | Mean RMSE: -6437.2 | Added `age_cat_encoded` | leicht verbessert |
| 10 | Random Forest | Mean RMSE: -6439.6 | Added `condition_good` | leicht verschlechtert, wieder entfernt |
| 11 | Random Forest | Mean RMSE: -6462.2 | Added `model_grouped` | leicht verschlechtert, wieder entfernt |
| 12 | Random Forest | Mean RMSE: -6345.2 | Added `type` | verbessert |
| 13 | Random Forest | Mean RMSE: -6253.2 | Added `transmission` | verbessert |

## References
![Feature Importance](doc/feature_importances.png "Feature Importance")<span id="fig1"></span>
