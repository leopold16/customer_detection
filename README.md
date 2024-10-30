# In-Store Customer Detection System

Welcome to the **In-Store Customer Detection System** project! This experimental application enables food store customers to voluntarily access their past orders through facial recognition. By scanning their face, returning customers can view order history, enhancing personalized experiences in-store.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

---

## Project Overview
The **In-Store Customer Detection System** is an opt-in facial recognition system designed for use in food retail environments. This system allows customers who have consented to facial recognition to:
1. Automatically access their order history upon returning to the store.
2. Enhance their shopping experience with personalized order recommendations.

This project is designed as an experimental proof-of-concept to explore how technology can improve in-store service while respecting customer privacy.

---

## Features
- **Facial Recognition**: Recognizes customers upon entering the store, leveraging face recognition technology.
- **Order History Access**: Links each recognized customer to their previous order history, enabling them to view past purchases.
- **Privacy-Focused**: Operates on a voluntary, opt-in basis to respect customer privacy.

---

## System Architecture
The system architecture comprises the following main components:
- **Customer Registration Module**: Manages the registration of customers opting into the facial recognition system, storing face data securely.
- **Face Recognition Module**: Detects and identifies customers using a trained face recognition model.
- **Order History Database**: Stores customer order histories, which can be queried upon successful recognition.
- **User Interface**: Simple UI to display past orders and allow customers to interact with their history.

---

## Technologies Used
- **Python** for backend and facial recognition
- **OpenCV** and **DeepFace** for face detection and recognition
- **SQLite** for order history database (for simplicity, but can be replaced with other databases)
- **Flask** for a lightweight web interface (optional)
- **Docker** for containerization (optional)

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/in-store-customer-detection.git
   cd in-store-customer-detection
