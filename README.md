# Price Alert Application

## Overview

This application provides a price alert system for cryptocurrencies. Users can set alerts for specific prices of coins, and the application will notify users via email when the price reaches or exceeds the target price.

## Features

- Create and manage price alerts via API endpoints
- Real-time price tracking using Binance WebSocket
- Email notifications when alerts are triggered
- Redis caching for alert management
- Dockerized application

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/price-alert-app.git
    cd price-alert-app
    ```

2. Build and start the application with Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. The application will be accessible at `http://localhost:8000`.

## API Endpoints

### Create Alert

- `POST /alerts/create/`
- Request Body:
    ```json
    {
        "coin_symbol": "BTCUSDT",
        "target_price": 33000
    }
    ```

### Delete Alert

- `DELETE /alerts/delete/{alert_id}`

### Get Alerts

- `GET /alerts/`
- Query Parameters:
    - `status` (optional): Filter alerts by status

## Configuration

- MySQL Database
- Redis for caching
- SMTP for email notifications (configure `EMAIL_HOST`, `EMAIL_USER`, and `EMAIL_PASSWORD` in `docker-compose.yml`)

## Notes

- Ensure that the email service credentials are correctly set in `docker-compose.yml`.
- The real-time price tracking is set up to listen to Binance WebSocket and check alerts accordingly.
