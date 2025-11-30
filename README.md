# 🎵 Audio Manager - Full-Stack Django Application

A comprehensive full-stack web application built with Django and Django REST Framework that allows users to manage their audio files with upload, playback, edit, and delete functionalities.

## 📋 Features

### Backend (Django REST API)
- **User Management**: Create, read, update, and delete user profiles
- **Audio File Management**: Upload, retrieve, update, and delete audio files
- **RESTful API**: Well-structured REST API endpoints
- **File Storage**: Local file storage with proper organization
- **Data Validation**: File type validation (MP3, WAV, OGG, M4A, FLAC)
- **Database**: SQLite database for easy setup and portability

### Frontend
- **User Dashboard**: View all users with their details
- **User Creation**: Form to create new users
- **User Detail Page**: Display user information and their audio files
- **Audio Upload**: Upload audio files with title and description
- **Audio Playback**: Built-in HTML5 audio player
- **Audio Management**: Edit metadata and replace audio files
- **Delete Functionality**: Remove audio files with confirmation
- **Download Option**: Download audio files to local device
- **Responsive Design**: Beautiful gradient UI that works on all devices

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework 3.14.0
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Storage**: Local file system
- **CORS**: django-cors-headers for API access

## 📁 Project Structure

```
Codaemon_Assignment/
│
├── audio_manager/              # Main Django project
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                      # Users app
│   ├── __init__.py
│   ├── admin.py               # Admin interface configuration
│   ├── apps.py
│   ├── models.py              # User and AudioFile models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   ├── frontend_views.py      # Template views
│   ├── urls.py                # API URL patterns
│   └── frontend_urls.py       # Frontend URL patterns
│
├── templates/                  # HTML templates
│   ├── home.html              # User list and creation page
│   └── user_detail.html       # User detail and audio management page
│
├── media/                      # Uploaded audio files (created automatically)
│   └── audio/
│       └── [username]/        # User-specific folders
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```powershell
   cd "e:\03 Abhishek\Projects\Codaemon_Assignment"
   ```

2. **Create a virtual environment (recommended)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```powershell
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Run the development server**
   ```powershell
   python manage.py runserver
   ```

7. **Access the application**
   - Frontend: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - API Root: http://localhost:8000/api/

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api/
```

### User Endpoints

#### Get All Users
```http
GET /api/users/
```
**Response:**
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "bio": "Music enthusiast",
    "phone": "+1234567890",
    "created_at": "2025-11-30T10:00:00Z",
    "updated_at": "2025-11-30T10:00:00Z"
  }
]
```

#### Get Specific User
```http
GET /api/users/{id}/
```
**Response:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "bio": "Music enthusiast",
  "phone": "+1234567890",
  "created_at": "2025-11-30T10:00:00Z",
  "updated_at": "2025-11-30T10:00:00Z",
  "audio_files": [...],
  "audio_count": 5
}
```

#### Create User
```http
POST /api/users/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "bio": "Music enthusiast",
  "phone": "+1234567890"
}
```

#### Update User
```http
PUT /api/users/{id}/
PATCH /api/users/{id}/  (for partial updates)
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "bio": "Updated bio"
}
```

#### Delete User
```http
DELETE /api/users/{id}/
```

### Audio File Endpoints

#### Get All Audio Files
```http
GET /api/audio/
GET /api/audio/?user_id={user_id}  (filter by user)
```
**Response:**
```json
[
  {
    "id": 1,
    "title": "My Song",
    "description": "A beautiful melody",
    "audio_file": "/media/audio/john_doe/song.mp3",
    "audio_url": "http://localhost:8000/media/audio/john_doe/song.mp3",
    "duration": null,
    "file_size": 5242880,
    "file_size_display": "5.00 MB",
    "uploaded_at": "2025-11-30T10:00:00Z",
    "updated_at": "2025-11-30T10:00:00Z",
    "is_active": true
  }
]
```

#### Get Specific Audio File
```http
GET /api/audio/{id}/
```

#### Upload Audio File
```http
POST /api/audio/
Content-Type: multipart/form-data

user_id: 1
title: "My Song"
description: "A beautiful melody"
audio_file: [binary file data]
```

#### Update Audio File
```http
PUT /api/audio/{id}/
PATCH /api/audio/{id}/  (for partial updates)
Content-Type: multipart/form-data

title: "Updated Title"
description: "Updated description"
audio_file: [binary file data]  (optional)
```

#### Delete Audio File (Soft Delete)
```http
DELETE /api/audio/{id}/
```
Sets `is_active` to `False` but keeps the file.

#### Permanently Delete Audio File
```http
DELETE /api/audio/{id}/hard_delete/
```
Removes the file from storage permanently.

#### Get User's Audio Files
```http
GET /api/users/{id}/audio_files/
```

## 🎨 Frontend Features

### Home Page (/)
- View all registered users
- Create new users with form validation
- Click on user cards to view details
- Responsive grid layout

### User Detail Page (/user/{id}/)
- Display user information
- Upload new audio files
- View all audio files for the user
- Audio player with playback controls
- Edit audio metadata
- Replace audio files
- Delete audio files
- Download audio files

## 🔧 Configuration

### Settings (audio_manager/settings.py)
- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Change this in production
- `ALLOWED_HOSTS`: Configure for your domain
- `MEDIA_ROOT`: Location for uploaded files
- `MEDIA_URL`: URL path for media files

### Allowed Audio Formats
- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)
- M4A (.m4a)
- FLAC (.flac)

## 🔐 Security Considerations

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Change the `SECRET_KEY` to a secure random value
3. Configure `ALLOWED_HOSTS` properly
4. Use a production database (PostgreSQL, MySQL)
5. Set up proper file storage (AWS S3, etc.)
6. Enable HTTPS
7. Configure CORS properly
8. Add authentication/authorization
9. Implement rate limiting
10. Add input validation and sanitization

## 🧪 Testing the Application

### Using the Frontend
1. Navigate to http://localhost:8000/
2. Create a new user using the form
3. Click on the user card to go to their detail page
4. Upload an audio file
5. Play the audio using the built-in player
6. Edit or delete the audio file

### Using the API (with curl or Postman)

**Create a User:**
```powershell
curl -X POST http://localhost:8000/api/users/ -H "Content-Type: application/json" -d '{\"username\":\"test_user\",\"email\":\"test@example.com\",\"first_name\":\"Test\",\"last_name\":\"User\"}'
```

**Upload Audio:**
```powershell
curl -X POST http://localhost:8000/api/audio/ -F "user_id=1" -F "title=Test Song" -F "description=A test audio" -F "audio_file=@path/to/audio.mp3"
```

## 📊 Database Schema

### User Model
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `first_name`: First name
- `last_name`: Last name
- `bio`: Biography (optional)
- `phone`: Phone number (optional)
- `created_at`: Timestamp
- `updated_at`: Timestamp

### AudioFile Model
- `id`: Primary key
- `user`: Foreign key to User
- `title`: Audio title
- `description`: Description (optional)
- `audio_file`: File field
- `duration`: Duration in seconds (optional)
- `file_size`: Size in bytes
- `uploaded_at`: Timestamp
- `updated_at`: Timestamp
- `is_active`: Boolean flag

## 🎯 Additional Features Implemented

1. **File Organization**: Audio files are organized in user-specific folders
2. **File Size Display**: Human-readable file sizes (KB/MB)
3. **Soft Delete**: Audio files can be deactivated without permanent deletion
4. **Hard Delete**: Option to permanently remove files
5. **File Validation**: Only allowed audio formats can be uploaded
6. **Responsive Design**: Works on mobile, tablet, and desktop
7. **Beautiful UI**: Modern gradient design with smooth animations
8. **Error Handling**: Comprehensive error messages
9. **Admin Interface**: Full Django admin for data management
10. **Download Feature**: Users can download their audio files

## 🐛 Troubleshooting

### Port Already in Use
```powershell
# Kill the process using port 8000
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process
```

### Database Issues
```powershell
# Delete db.sqlite3 and migrations, then:
python manage.py makemigrations
python manage.py migrate
```

### Media Files Not Showing
- Ensure `MEDIA_URL` and `MEDIA_ROOT` are properly configured
- Check if the development server is serving media files
- Verify file permissions

### Audio Files Not Visible After Upload
If audio files upload successfully but don't appear in the UI:
```powershell
# Check audio files status
python manage.py check_audio

# Reactivate inactive audio files
python manage.py check_audio --activate
```

This issue occurs when audio files are soft-deleted (set to inactive). The command above will help identify and fix the issue.
