# Volunteering App

## Project Overview

The Volunteering App is a web application designed to connect volunteers with projects and causes in Kenya. It facilitates the process of finding volunteer opportunities, signing up for events, tracking volunteer hours, and making donations.

## Project Structure

The project appears to be built using Django, a Python web framework. Here's an overview of the main components:

### Backend (Django)

- `urls.py`: Defines the URL patterns for the application
- `views.py`: Contains the view functions that handle requests and return responses
- `models.py`: Defines the data models for the application
- `forms.py`: Contains form classes for handling user input
- `admin.py`: Configures the Django admin interface
- `apps.py`: Contains app configuration
- `tests.py`: Contains test cases for the application

### Frontend

- `templates/`: Directory containing HTML templates
    - `donate.html`: Template for donation page
    - `donations.html`: Template for listing donation options
    - `event-form.html`: Template for event submission form
    - `events.html`: Template for listing events
    - `home.html`: Template for the home page
    - `index.html`: Template for the landing/registration page
    - `login.html`: Template for the login page
    - `opportunityvolunteer.html`: Template for volunteer opportunities
    - `organizationtype.html`: Template for filtering by organization type
    - `profile.html`: Template for user profile
    - `volunteerform.html`: Template for volunteer registration form
- `static/`:
    - `CSS/`: Directory containing CSS files for styling
        - `donations.css`, `event-form.css`, `events.css`, `home.css`, `index.css`, `opportunity-volunteer.css`, `profile.css`, `sign-in.css`, `volunteerform.css`
    - `js/`: Directory containing JavaScript files
        - `event.js`, `home.js`, `volunteerform.js`

### Media

- `media/`: Directory for storing user-uploaded files

## Main Features

Based on the URL patterns and template files, the app includes the following features:

1. User Authentication
    - Registration (`index.html`)
    - Login (`login.html`)
2. Home Page (`home.html`)
3. Events
    - Viewing events (`events.html`)
    - Event submission form (`event-form.html`)
4. User Profile (`profile.html`)
    - Viewing and updating profile
    - Tracking volunteer hours
5. Volunteer Opportunities
    - Browsing opportunities (`opportunityvolunteer.html`)
    - Submitting volunteer form (`volunteerform.html`)
6. Donations
    - Viewing donation options (`donations.html`)
    - Making donations (`donate.html`)
7. Organization Types
    - Filtering by organization type (`organizationtype.html`)

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Steps

1. Clone the repository:
    
    ```
    git clone <https://github.com/janicefoi/volunteering-app.git>
    cd volunteering-app
    
    ```
    
2. Create and activate a virtual environment:
    
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    
    ```
    
3. Install the required packages:
    
    ```
    pip install -r requirements.txt
    
    ```
    
4. Set up the database:
    
    ```
    python manage.py migrate
    
    ```
    
5. Create a superuser (admin account):
    
    ```
    python manage.py createsuperuser
    
    ```
    
6. Collect static files:
    
    ```
    python manage.py collectstatic
    
    ```
    

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated.
2. Start the Django development server:
    
    ```
    python manage.py runserver
    
    ```
    
3. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.
4. To access the admin interface, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

## Testing

To run the tests for the application:

```
python manage.py test

```
## Pictures
![WhatsApp Image 2024-08-08 at 16 48 22_94950c8b](https://github.com/user-attachments/assets/67f8dc35-4689-475e-9031-9664687ab6a7)
![WhatsApp Image 2024-08-08 at 16 48 21_e3df4444](https://github.com/user-attachments/assets/23714133-9da8-46fc-b7c5-19aebacd8e76)
![WhatsApp Image 2024-08-08 at 16 48 19_a44e6e1e](https://github.com/user-attachments/assets/8bc071b3-529e-4f69-8155-5e1bc343d4fe)
![WhatsApp Image 2024-08-08 at 16 48 18_291aaa62](https://github.com/user-attachments/assets/ee733dad-36c4-4cc7-afb6-aa1810f25814)
![WhatsApp Image 2024-08-08 at 16 48 17_6ec280cd](https://github.com/user-attachments/assets/10948555-11d1-400f-8a6e-e721639dcd1f)
![WhatsApp Image 2024-08-08 at 16 48 16_0b7c73f5](https://github.com/user-attachments/assets/23bc8a31-f885-448c-88e7-a1487e1a9579)
![WhatsApp Image 2024-08-08 at 16 48 15_1c69a53c](https://github.com/user-attachments/assets/d1233879-2b06-4d5d-8333-4c888bd1d6eb)
![WhatsApp Image 2024-08-08 at 16 48 14_651908e2](https://github.com/user-attachments/assets/f71cc952-c1a8-4b70-a931-3a2435194a3f)
![WhatsApp Image 2024-08-08 at 16 48 13_c6ae3e12](https://github.com/user-attachments/assets/81de1545-45bb-45e2-a499-861c6b62c7e5)
![WhatsApp Image 2024-08-08 at 16 48 13_b7e12825](https://github.com/user-attachments/assets/7b34627c-5033-41be-9533-cbe1cdd00b8e)
![WhatsApp Image 2024-08-08 at 16 48 12_41829d8f](https://github.com/user-attachments/assets/750580f4-e7c6-4a12-afe8-985787365333)
![WhatsApp Image 2024-08-08 at 16 48 11_4173768a](https://github.com/user-attachments/assets/c5b3923d-a722-4a23-be9e-9f4ed6ec347a)
![WhatsApp Image 2024-08-08 at 16 48 11_38e149b9](https://github.com/user-attachments/assets/8883de34-4403-4b28-8a33-77e93f720aad)
![WhatsApp Image 2024-08-08 at 16 48 10_161efe96](https://github.com/user-attachments/assets/edfef8c9-b104-4e9e-9524-1860caf7d3d2)
![WhatsApp Image 2024-08-08 at 16 48 09_4fae563e](https://github.com/user-attachments/assets/1d7cbf80-0340-42eb-9504-9d4e976d15d2)
![WhatsApp Image 2024-08-08 at 16 48 08_3b7f4342](https://github.com/user-attachments/assets/5d060805-1fda-4aad-b112-811f88359cd3)
![WhatsApp Image 2024-08-08 at 16 48 07_dc1dd0d0](https://github.com/user-attachments/assets/64550529-55d0-49f8-9a1d-0d3dbc447448)
![WhatsApp Image 2024-08-08 at 16 48 06_f42c2758](https://github.com/user-attachments/assets/38ad12d5-b084-4682-b23d-36579be730b9)
![WhatsApp Image 2024-08-08 at 16 48 05_333a867f](https://github.com/user-attachments/assets/937b01ed-cf72-4a19-bb12-18c40a235016)
![WhatsApp Image 2024-08-08 at 16 48 23_4ee3e0c7](https://github.com/user-attachments/assets/abbc58f6-3bfb-40c2-880c-32bee4b33f45)


