# K-Nearest Neighbors (KNN) Classifier for Student Draft Selection

## Overview
This project implements a K-Nearest Neighbors (KNN) classification model to predict whether a student will be drafted based on their speed and agility. The model is trained using a dataset stored in an Excel file and provides predictions based on user input.

## Features
- Uses the **KNN algorithm** from `scikit-learn` to classify students.
- Reads data from an Excel file (`Dataset_1_KNN.xlsx`).
- Converts categorical values ('yes'/'no') to numerical values (1/0).
- Accepts user input for **speed** and **agility** and predicts draft selection.

## Prerequisites
Ensure you have Python installed along with the following dependencies:

```bash
pip install pandas numpy scikit-learn openpyxl
```

## How to Use
1. **Prepare the dataset:** Ensure `Dataset_1_KNN.xlsx` is in the same directory as the script.
2. **Run the script:**
   ```bash
   python knn_classifier.py
   ```
3. **Provide user input** when prompted:
   - Enter speed value.
   - Enter agility value.
4. **View the output**, which will indicate whether the student is selected or not.

## Code Explanation
1. **Data Preprocessing:**
   - Reads dataset using `pandas`.
   - Converts 'Draft' column ('yes' -> 1, 'no' -> 0).
2. **Feature Selection:**
   - Uses `Speed` and `Agility` as predictor variables (`X`).
   - Uses `Draft` as the target variable (`y`).
3. **Model Training:**
   - Implements KNN with `k=3` neighbors.
   - Trains the model with given data.
4. **Prediction:**
   - Accepts user input.
   - Predicts draft selection using the trained KNN model.

## Example Output
```
Enter the value of speed to be predicted: 8.5
Enter the value of agility to be predicted: 7.2
Predicted class for the student with speed=8.5 and agility=7.2: Selected
```

## Notes
- Ensure the dataset is formatted correctly before running the script.
- You can change the value of `k` in `KNeighborsClassifier(n_neighbors=k)` to optimize performance.

## License
This project is licensed under the MIT License.

---

Feel free to contribute by submitting pull requests or reporting issues!

