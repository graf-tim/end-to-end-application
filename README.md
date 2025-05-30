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
TODO
| Feature | Description |
|---------|-------------|
| room_per_m2 | Room / area |
| price_per_m2 | Price / area (not used!) |
| Luxurious, temporary, furnished | Extracted binary feature from description_raw if luxurious, temporary, furnished |
| area_cat, area_cat_encoded | Encoded area into three groups:<br>0: 0 – 49 m²<br>1: 50 – 99 m²<br>2: 100 – 500 m² |
| (LOFT), (POOL), (ATTIKA), (EXKLUSIV), (SEESICHT), (LUXURIÖS) | One hot encoding of feature Luxurious depending on type of luxurious |
| Kreis 1-12 | One hot encoding of apartments in the city Zurich |
| zurich_city | Binary feature if apartment is in the city Zurich |

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
