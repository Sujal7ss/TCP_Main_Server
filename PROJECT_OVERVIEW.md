# TCP Mentorship Platform - Complete Project Overview

## 🎯 Project Overview
This is a comprehensive mentorship management platform built with Django REST API, designed to facilitate mentor-mentee relationships, team management, and progress tracking for a technical mentorship program.

## 🏗️ Architecture & Tech Stack

### Backend Architecture
- **Framework**: Django 4.2.4 with Django REST Framework 3.14.0
- **Database**: SQLite3 (development) with PostgreSQL support (production-ready)
- **API**: RESTful API with JSON responses
- **Authentication**: Session-based authentication with email/password
- **CORS**: django-cors-headers for cross-origin requests

### Key Dependencies
```
Django==4.2.4
djangorestframework==3.14.0
django-cors-headers==4.2.0
Pillow==10.0.0
drf-yasg==1.21.4 (API documentation)
psycopg2-binary (PostgreSQL adapter)
```

### Development Environment
- **Debug Mode**: True (development)
- **Time Zone**: Asia/Kolkata
- **Allowed Hosts**: Multiple domains including localhost, production IPs
- **CORS**: Configured for multiple frontend origins

## 📊 Data Models & Architecture

### Core Entities

#### 1. **Mentor Model**
```python
Fields:
- Personal: name, email, password, phone_number, image
- Academic: branch, semester
- Platform IDs: codechefID, codeforcesID, leetcodeID, gfgID, hackerrankID, linkedinID
- Performance: score, total_q, topic_count, Qlevel_count
- Relationships: Mentorteam (ForeignKey to Team)
```

#### 2. **Mentee Model**
```python
Fields:
- Personal: name, email, username, password, phone_number, image
- Academic: branch, semester
- Platform IDs: Same as Mentor
- Performance: score, total_q, solvedQ, topic_count, Qlevel_count, cumHour_diff, Mentee_rank
- Relationships: mentor_id, Menteeteam (ForeignKey to Team)
```

#### 3. **Team Model**
```python
Fields:
- team_name (unique)
- alloted_mentor (ForeignKey to Mentor)
- team_members (ManyToManyField to Mentee)
- team_score, cumHour_diff, team_rank
```

#### 4. **TeamMember Model** (Organizational)
```python
Fields:
- name, branch, image, member_type, year, domain
- Social links: linkedin, instagram, email
```

## 🔄 Data Flow Architecture

### User Registration Flow
1. **Mentor Registration**: Direct creation via admin panel
2. **Mentee Registration**: 
   - Mentee signs up with mentor's email
   - System assigns mentor_id based on email
   - Optionally adds to mentor's team if exists

### Team Formation Flow
1. **Mentor creates team** → Team linked to mentor
2. **Mentees assigned** → All mentees with same mentor_id added to team
3. **Performance tracking** → Individual and team scores calculated

### Authentication Flow
- **Login**: Email + password validation
- **Session Management**: Django session framework
- **Profile Updates**: Partial updates supported

## 🌐 API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/server/mentor_login` | Mentor login with email/password |
| POST | `/server/mentee_login` | Mentee login with email/password |
| POST | `/server/mentee_signup` | Mentee registration |

### Team Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/server/getTeams/` | Get all teams with details |
| POST | `/server/createteam` | Create new team |
| POST | `/server/updateteam` | Update team details |
| GET | `/server/get-team-mentor/<id>` | Get teams for specific mentor |
| GET | `/server/get-team-mentee/<id>` | Get team for specific mentee |

### User Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/server/update_mentee` | Update mentee profile |
| POST | `/server/update_mentor` | Update mentor profile |
| GET | `/server/getMentees/` | Get all mentees |
| GET | `/server/getMentee/<menteeId>` | Get specific mentee details |
| GET | `/server/getMentor/<mentorId>` | Get specific mentor details |

## 📈 Performance Tracking System

### Individual Metrics
- **Score**: Overall performance score
- **Total Questions**: Questions attempted
- **Solved Questions**: Questions successfully solved
- **Topic-wise Count**: JSON field tracking performance by topic
- **Difficulty Level Count**: Questions solved by difficulty
- **Cumulative Hours**: Time spent (cumHour_diff)

### Team Metrics
- **Team Score**: Combined team performance
- **Team Rank**: Ranking among all teams
- **Cumulative Hours**: Combined time spent by team

### Branches Supported
- CSE, IT, ECE, ELEC, MECH, CHEM, CIVIL, META, MIN, BIOMED, BIOTECH, MCA

## 🗄️ Database Schema Relationships

### Primary Relationships
```
Mentor 1:N Mentee (via mentor_id)
Mentor 1:N Team (via alloted_mentor)
Team N:M Mentee (via team_members ManyToMany)
```

### Data Integrity
- **Unique Constraints**: email (Mentor), username (Mentee), team_name (Team)
- **Foreign Keys**: CASCADE on delete for team relationships
- **Validation**: Phone number uniqueness, password minimum length (8 chars)

## 🚀 Deployment Configuration

### Server Settings
- **Admin URL**: `/server/admin/`
- **Media Files**: Served from root directory
- **Static Files**: Collected to `./static`
- **CORS**: Configured for multiple origins including production domains

### Production Domains
- `codeutsava.nitrr.ac.in`
- `tcpmentorship.nitrr.ac.in`
- `tcpmentorship.netlify.app`
- IP-based access: `13.49.223.25`, `16.171.64.245`

## 📋 Key Features

### 1. **User Management**
- Separate login for mentors and mentees
- Profile management with platform integration
- Image upload support

### 2. **Team Management**
- Dynamic team creation and assignment
- Mentor-mentee relationship mapping
- Team performance tracking

### 3. **Progress Tracking**
- Individual performance metrics
- Team-based rankings
- Topic-wise progress analysis

### 4. **Platform Integration**
- Support for multiple coding platforms
- Unified progress tracking
- Social media integration

## 📊 API Response Format

### Standard Response Structure
```json
{
  "data": {...},
  "message": "Success message",
  "status_code": 200
}
```

### Error Response Structure
```json
{
  "status_message": "Error message",
  "status_code": 403
}
```

## 🎯 Use Cases

1. **Mentor Dashboard**: View assigned teams and mentee progress
2. **Mentee Portal**: Track individual progress and team affiliation
3. **Admin Management**: Create teams, assign mentors, monitor performance
4. **Analytics**: Performance tracking across branches and teams

## 🔐 Security Features

- Password validation (minimum 8 characters)
- Email uniqueness validation
- Phone number uniqueness
- CORS protection for API endpoints
- CSRF token validation

## 📱 Frontend Integration

- RESTful API design for easy frontend integration
- JSON responses for all endpoints
- CORS configured for multiple frontend origins
- Image upload support for user profiles

