# Hospitality Digitalization

## Overview
This Flask application aims to digitalize the hospitality process for group accommodation. It allows users to upload two CSV files: one containing group information and another with hostel information. The application then allocates rooms based on specified criteria and generates an allocation CSV file for download.

## Logic
### File Upload
Users upload two CSV files:
- **Group CSV**: Contains information about groups, including Group ID, number of members, and gender (boys or girls).
- **Hostel CSV**: Provides details about hostel rooms, such as Hostel Name, Room Number, Capacity, and Gender accommodation (boys or girls).
### Room Allocation
Upon file upload, the application reads these CSV files using pandas:
- It iterates through each group from the Group CSV.
- Filters available hostel rooms based on group size and gender requirements.
- Allocates rooms to groups while ensuring members with the same Group ID stay together and adhere to hostel capacities and gender-specific accommodations.
### Output
After allocation, the application generates an allocation CSV file:
- This file lists each allocated group with details of the assigned hostel and room number.
- Users can download this file to view allocation details.

## Usage
- **Upload**: Navigate to the application URL and upload the required CSV files.
- **Allocation**: The application automatically allocates rooms based on uploaded data.
- **Download**: After allocation, download the generated allocation CSV file for reference.

## Instructions to Run the Application
1. **Clone Repository**: Clone the public GitHub repository containing the Flask application code.

   git clone <repository_url>

   cd <repository_directory>

2. **Set Up Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

  python -m venv venv

  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**: Install the necessary Python packages.

pip install -r requirements.txt

4. **Run the Application**: Start the Flask application.

python app.py

5. **Access the Application**: Open a web browser and go to http://localhost:5000 (or any generated port that shows after running the command).

6. **Upload CSV Files**: Follow the on-screen instructions to upload the Group CSV and Hostel CSV files (example files are available in the "uploads" directory).

7. **Download Allocation**: After processing, download the generated allocation.csv file to view room allocations (Note: The downloaded file may show an error message; instead, check the "allocations" directory where the result is saved).




