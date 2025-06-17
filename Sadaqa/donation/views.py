from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Donation
from django.contrib import messages
from projects.models import Project
from django.utils import timezone

# REST framework imports
from rest_framework import generics, permissions
from .serializers import DonationSerializer

# -------------------- Web Views --------------------

@login_required
def create_donation(request):
    if request.method == 'POST':
        project_id = request.POST.get('project')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        
        try:
            # Handle default projects
            if project_id in ['gaza', 'somalia']:
                project_title = 'مشروع غزة' if project_id == 'gaza' else 'مشروع الصومال'
                # Create a temporary project if it doesn't exist
                project, created = Project.objects.get_or_create(
                    title=project_title,
                    defaults={
                        'user': request.user,
                        'details': f'تبرع ل{project_title}',
                        'total_target': 1000000,  # 1 million
                        'start_date': timezone.now(),
                        'end_date': timezone.now() + timezone.timedelta(days=365),
                        'status': 'active'
                    }
                )
            else:
                project = Project.objects.get(id=project_id, status='active', is_cancelled=False)
            
            if amount and currency:
                donation = Donation.objects.create(
                    donor=request.user,
                    project=project,
                    amount=amount,
                    currency=currency
                )
                messages.success(request, "تم استلام تبرعك بنجاح!")
                return redirect('donation:success')
            else:
                messages.error(request, "يرجى ملء جميع الحقول المطلوبة")
        except Project.DoesNotExist:
            messages.error(request, "المشروع غير موجود أو غير نشط")
    
    # Get all active projects for the form
    projects = Project.objects.filter(status='active', is_cancelled=False)
    # Add default projects to the context
    context = {
        'projects': projects,
        'show_default_projects': True  # This will be used in the template
    }
    return render(request, 'donation/donate.html', context)


@login_required
def donation_success(request):
    return render(request, 'donation/success.html')


@login_required
def donation_history(request):
    donations = Donation.objects.filter(donor=request.user).order_by('-donation_date')
    return render(request, 'donation/history.html', {'donations': donations})


# -------------------- REST API Views --------------------

class DonationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


class DonationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(donor=self.request.user)
