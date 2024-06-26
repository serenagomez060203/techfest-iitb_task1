import os  # Import the os module for interacting with the operating system
from flask import Flask, request, render_template, send_from_directory  # Import necessary Flask modules
import pandas as pd  # Import pandas for data manipulation

app = Flask(__name__)  # Create a Flask application instance
UPLOAD_FOLDER = 'uploads'  # Define the upload folder name
ALLOCATION_FOLDER = 'allocations'  # Define the allocation folder name

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configure Flask app to use UPLOAD_FOLDER for file uploads
app.config['ALLOCATION_FOLDER'] = ALLOCATION_FOLDER  # Configure Flask app to use ALLOCATION_FOLDER for allocations

if not os.path.exists(UPLOAD_FOLDER):  # Check if UPLOAD_FOLDER directory exists
    os.makedirs(UPLOAD_FOLDER)  # Create UPLOAD_FOLDER directory if it doesn't exist
if not os.path.exists(ALLOCATION_FOLDER):  # Check if ALLOCATION_FOLDER directory exists
    os.makedirs(ALLOCATION_FOLDER)  # Create ALLOCATION_FOLDER directory if it doesn't exist

@app.route('/')  # Route decorator for the index page
def index():
    return render_template('index.html')  # Render the index.html template on accessing the root URL

@app.route('/upload', methods=['POST'])  # Route decorator for handling file uploads via POST method
def upload_files():
    group_file = request.files['group_file']  # Get the uploaded group CSV file
    hostel_file = request.files['hostel_file']  # Get the uploaded hostel CSV file
    
    group_file_path = os.path.join(app.config['UPLOAD_FOLDER'], group_file.filename)  # Define path to save group CSV file
    hostel_file_path = os.path.join(app.config['UPLOAD_FOLDER'], hostel_file.filename)  # Define path to save hostel CSV file
    
    group_file.save(group_file_path)  # Save the group CSV file to UPLOAD_FOLDER
    hostel_file.save(hostel_file_path)  # Save the hostel CSV file to UPLOAD_FOLDER
    
    allocation_df = allocate_rooms(group_file_path, hostel_file_path)  # Call function to allocate rooms based on CSV data
    
    allocation_file_path = os.path.join(app.config['ALLOCATION_FOLDER'], 'allocation.csv')  # Define path for allocation CSV file
    allocation_df.to_csv(allocation_file_path, index=False)  # Save allocation data to allocation.csv
    
    return send_from_directory(directory=app.config['ALLOCATION_FOLDER'], filename='allocation.csv', as_attachment=True)  # Serve the allocation.csv file for download

def allocate_rooms(group_file_path, hostel_file_path):
    group_df = pd.read_csv(group_file_path)  # Read the group CSV file into a pandas DataFrame
    hostel_df = pd.read_csv(hostel_file_path)  # Read the hostel CSV file into a pandas DataFrame
    
    allocation_list = []  # Initialize an empty list to store allocation results
    
    for _, group in group_df.iterrows():  # Iterate through each row in the group DataFrame
        group_id = group['Group ID']  # Get the group ID
        members = group['Members']  # Get the number of group members
        gender = group['Gender']  # Get the gender of the group
        
        # Filter available rooms based on capacity and gender
        available_rooms = hostel_df[(hostel_df['Capacity'] >= members) & (hostel_df['Gender'] == gender)]
        
        if not available_rooms.empty:  # If there are available rooms that meet criteria
            room = available_rooms.iloc[0]  # Select the first available room
            allocation_list.append({  # Append allocation details to the list
                'Group ID': group_id,
                'Hostel Name': room['Hostel Name'],
                'Room Number': room['Room Number'],
                'Members Allocated': members
            })
            hostel_df.drop(room.name, inplace=True)  # Remove allocated room from hostel DataFrame
    
    allocation_df = pd.DataFrame(allocation_list)  # Create DataFrame from allocation_list
    return allocation_df  # Return DataFrame with allocation results

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode if this script is executed directly
