# Sadaqa - Crowd Funding Web Application

## Donation App

The Donation app is a core component of the Sadaqa platform, enabling users to make donations to various projects. It features a modern, dark-themed interface with a focus on user experience and secure transaction handling.

### Features

- **Project-Based Donations**: Users can donate to specific projects with different funding goals
- **Multiple Currency Support**: Donations can be made in various currencies (USD, EUR, GBP, etc.)
- **Donation History**: Track all donations with detailed records
- **User Authentication**: Secure donation process with user authentication
- **Responsive Design**: Modern dark theme with Bootstrap styling
- **Form Validation**: Client and server-side validation for secure transactions

### Models

#### Donation Model
```python
class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    donation_date = models.DateTimeField(auto_now_add=True)
```

#### Project Model
```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
```

### Key Features Implementation

1. **Dark Theme Styling**
   - Custom CSS variables for consistent theming
   - Responsive design with Bootstrap integration
   - Form controls with dark background and light text

2. **Donation Process**
   - Secure form handling with Django forms
   - Real-time validation
   - Currency conversion support
   - Transaction history tracking

3. **User Interface**
   - Clean and intuitive donation form
   - Project selection dropdown
   - Amount input with currency selection
   - Success/error message handling

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Galal36/Django_Donation_Jalal_App.git
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database settings in `settings.py`

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

### Dependencies

- Django
- django-crispy-forms
- Bootstrap 5
- PostgreSQL (database)

### Contributing

This project is part of a larger crowd-funding platform where different components are developed by different team members. The donation app is maintained by Jalal.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
