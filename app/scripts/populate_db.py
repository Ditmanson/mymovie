import os
import django
from datetime import datetime
import sys


# Add the base directory to the PYTHONPATH
sys.path.append('V:\\movie_app')

#print(sys.path)
# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# Import the Movie model
from app.models import Movie


# Import your models after Django setup
from app.models import Movie  # Ensure that 'app' is the correct name of your app

# Function to populate the database
def populate_database():
    movie_directory = "V:\\Movies"  # Update this to your movie directory
    for filename in os.listdir(movie_directory):
        if filename.endswith(('.mp4', '.mkv', '.avi')):  # Add other extensions as needed
            movie = Movie(title=filename)  # Assuming your Movie model has a title field
            movie.save()

if __name__ == "__main__":
    populate_database()

