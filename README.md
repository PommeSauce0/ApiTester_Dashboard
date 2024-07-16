# Dashboard API Tester

Welcome to the **Dashboard API Tester** project. This project is designed to test various APIs and provide a user-friendly dashboard for visualizing test results.  
This project has been created to visualize and analyze the results of the [ApiTester](https://github.com/ASauvage/ApiTester) project.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Authors](#authors)

## Description

**Dashboard API Tester** is a web application developed with Flask. It allows users to test various APIs and visualize the test results in a dashboard format. The dashboard displays information such as test success rates, tested services, and encountered errors.

## Features

- Search test results by `session_id`, `service`, `status`, `environment` or with a `MongoDB query`.
- Display recent sessions with visual indicators (weather icons).
- Calculate and display success rates by service.
- Detailed view of test results with associated errors.
- Responsive and intuitive user interface.

## Prerequisites

Before installing and running this application, make sure you have the following installed:

- Python 3.9+
- MongoDB

## Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/ASauvage/ApiTester_Dashboard.git
    cd ApiTester_Dashboard
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure the MongoDB database:

    Ensure MongoDB is running on your machine or on an accessible server. Modify the necessary configurations in your application to point to your MongoDB instance.


5. Run the application:

    ```sh
    python main.py # if debug add --debug
    ```

    Access the application by opening your browser and navigating to `http://127.0.0.1:5000`.

## Usage

### Home Page

The home page displays recent sessions and service success rates. You can click on a session to view detailed test results.

### Session Search

Use the search form to filter test results by `session_id`, `service`, `status`, `environment` or with a `MongoDB query`. Click the "Search" button to initiate the search.

### Detailed Test Results

Click on a session in the results list to view the full details of the tests, including any encountered errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- **ASauvage** - [GitHub](https://github.com/ASauvage)
- **PommeSauce0** - [GitHub](https://github.com/PommeSauce0)

