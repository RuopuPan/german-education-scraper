# German Education Policy Scraper and Topic Clustering

This project collects and analyzes recent education policy headlines from the official website of the German Federal Ministry of Education and Research (BMBF). The goal is to simulate a basic pipeline for multilingual policy monitoring, unsupervised topic clustering, and thematic interpretation using machine learning and text mining tools.

Developed by Ruopu (Anna) Pan as an independent research project.

---

## Project Objectives

- Automate data collection of education-related headlines
- Clean and vectorize the text using TF-IDF
- Apply KMeans clustering to group headlines by thematic similarity
- Visualize the distribution of clusters
- Extract top keywords for each cluster to support interpretation

---

## Methodology

1. **Data Collection**  
   Headlines were scraped from the BMBF official news section using a Python-based scraper.

2. **Preprocessing**  
   The titles were processed using the NLTK library for:
   - Lowercasing
   - Stopword removal
   - Stemming

3. **Feature Extraction**  
   TF-IDF (Term Frequency–Inverse Document Frequency) was used to convert text to numerical vectors.

4. **Clustering**  
   Unsupervised learning with KMeans was used to group the headlines into clusters based on semantic similarity.

5. **Visualization**  
   Cluster frequencies were plotted using Matplotlib.

6. **Keyword Analysis**  
   For each cluster, the top 5 keywords were extracted based on mean TF-IDF scores.

---

## Results

### Cluster Distribution

The figure below shows the number of headlines per cluster:

![Cluster Distribution](cluster_distribution.png)

### Top Keywords per Cluster
These results suggest two dominant themes:

- Cluster 0: Digital transformation and AI in education  
- Cluster 1: Policy funding and teacher-related initiatives

---

## Technologies

- Python 3.13  
- pandas  
- scikit-learn  
- nltk  
- matplotlib  

---

## Files

| Filename                 | Description                                 |
|--------------------------|---------------------------------------------|
| `sample.csv`             | Sample scraped headlines                    |
| `multi_scraper.py`       | Web scraper for BMBF policy headlines       |
| `cluster_titles.py`      | Clustering and visualization script         |
| `cluster_distribution.png` | Output plot showing cluster frequencies     |
| `README.md`              | Project documentation                       |

---

## Author

Ruopu (Anna) Pan  
Temple University  
B.S. in Early Childhood Education (Expected 2027)  
GPA: 3.95 / 4.00  
Aspiring PhD in Marketing Analytics  
GitHub: [github.com/RuopuPan](https://github.com/RuopuPan)

---

## License

This project is for educational and academic purposes only.  
Data sourced from [https://www.bmbf.de](https://www.bmbf.de).
