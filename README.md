# Movie Genre Prediction

## Overview
This project aims to classify movies into their respective genres based solely on their descriptions. Leveraging Natural Language Processing (NLP) techniques and machine learning models, this tool can predict genres like Action, Comedy, Drama, and more based on textual data.

## Features
- **Automated Genre Prediction**: Input a movie description, and the model predicts its genre(s).
- **Natural Language Processing**: Utilizes advanced text preprocessing techniques.
- **Machine Learning Models**: Includes both traditional ML models and modern deep learning approaches.
- **Scalable Framework**: Easily extendable to include additional genres or refine predictions.

## Technologies Used
- **Programming Language**: Python
- **Libraries and Frameworks**:
  - Pandas, NumPy: Data manipulation and analysis
  - Scikit-learn: Traditional machine learning models
  - NLTK/Spacy: Text preprocessing and tokenization

## Dataset
The project uses a dataset containing:
- Movie descriptions (text)

      https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb/data

You can use publicly available datasets such as the [IMDb Dataset](https://www.imdb.com/interfaces/) or create your own dataset.

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Movie-Genre-Prediction-.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Movie-Genre-Prediction-
   ```

3. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Prepare the Dataset**: Place your dataset in the `data` folder (e.g., `data/movie_dataset.csv`).

2. **Run the Preprocessing Script**:
   ```bash
   python Prediction.py
   ```

3. **Train the Model**:
   ```bash
   python Model_Creation.py
   ```

4. **Make Predictions**:
   Use the trained model to predict genres for new descriptions:

## Folder Structure
```
Movie-Genre-Prediction-/
|-- data/              # Dataset files
|-- models/            # Saved models
|-- Model_Creation.py  # Model training script
|-- Prediction.py      # Prediction script
|-- requirements.txt   # Project dependencies
|-- README.md          # Project documentation
```

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Submit a pull request.

## Acknowledgments
- Datasets: https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb/data .
- Tutorials and community contributions that inspired this project.

## Contact
If you have any questions or suggestions, feel free to reach out:
- **Email**: rcjadhav005@gmail.com.com
- **GitHub**: [Rohit Chandrakant Jadhav]((https://github.com/Rohit-C-Jadhav-28))
---

Happy coding and enjoy exploring the world of movie genres! 🎬

