# ETL Pipeline Project

This project is a full-stack application that demonstrates an ETL (Extract, Transform, Load) pipeline using Python for the backend, PostgreSQL for the database, and React JS for the frontend. The project is containerized using Docker and orchestrated with Docker Compose.

## Project Structure

etl-pipeline-project/
├── backend/              # Python backend for ETL and API
│   ├── Dockerfile
│   ├── main.py           # Entry point for ETL and API
│   ├── etl/              # ETL logic
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   └── requirements.txt  # Python dependencies
├── database/             # PostgreSQL setup
│   ├── Dockerfile
│   └── init.sql          # Schema initialization
├── frontend/             # React JS frontend
│   ├── Dockerfile
│   ├── public/
│   └── src/
├── docker-compose.yml    # Orchestrates services
└── README.md



## Summary

### Backend

The backend is a Python application that performs the ETL process and serves an API endpoint to provide the transformed data. It uses Flask for the API and SQLAlchemy for database interactions.

- **extract.py**: Extracts data from an external API.
- **transform.py**: Transforms the extracted data into a desired format.
- **load.py**: Loads the transformed data into a PostgreSQL database.
- **main.py**: Entry point for running the ETL process and starting the Flask API.

### Database

The database service uses PostgreSQL. The `init.sql` file initializes the database schema.

- **init.sql**: Creates the `etl_db` database and the `weather_data` table.

### Frontend

The frontend is a React JS application that fetches data from the backend API and displays it in a table.

- **App.js**: Main React component that fetches data from the backend and displays it.
- **index.js**: Entry point for the React application.

### Docker Compose

The `docker-compose.yml` file orchestrates the backend, database, and frontend services.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/winbalf/etl-pipeline-project.git
   cd etl-pipeline-project