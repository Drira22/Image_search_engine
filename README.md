# Visual Search Engine

This project is a **Visual Search Engine** designed to find similar images based on either a description or an uploaded image. It utilizes deep learning and powerful search indexing to offer fast and accurate results. The core components include VGG16 for feature extraction, Elasticsearch for efficient indexing and searching, and Flask for the web interface. The project is containerized using Docker for easy deployment and scalability.

---

## 📂 Project Architecture

### Key Components

1. **VGG16 Feature Extraction**
   - The VGG16 deep learning model is employed for extracting feature vectors from images. It is pre-trained on the ImageNet dataset and fine-tuned for the specific task of extracting meaningful features from images for similarity comparison.

2. **Elasticsearch**
   - Elasticsearch is used to index the extracted features from the images. It enables fast, scalable, and efficient searching by storing and querying the image feature vectors in a manner that allows for quick similarity searches.

3. **Flask Web Interface**
   - A simple yet effective frontend built using **Flask** that allows users to upload images or provide descriptions for querying similar images. It interacts with the backend to process the queries and display results in a user-friendly manner.

4. **Docker**
   - Docker containers are used for packaging and deploying Elasticsearch and Kibana. This allows the application to be easily run and maintained across different environments with minimal setup.

---

## 🚀 Getting Started

To run the project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/Drira22/Image_search_engine.git
cd Image_search_engine

### 1. Clone the repository
