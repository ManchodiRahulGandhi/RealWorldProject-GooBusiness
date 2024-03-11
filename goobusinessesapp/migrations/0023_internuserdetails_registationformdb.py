# Generated by Django 5.0 on 2023-12-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0022_alter_aboutdb_imagepic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternUserDetails',
            fields=[
                ('slID', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('totalInternshipApply', models.IntegerField(default=0)),
                ('totalInternshipCompleted', models.IntegerField(default=0)),
                ('totalPaymentReceived', models.IntegerField(blank=True, default=0, null=True)),
                ('lastInterndate', models.DateField(auto_now=True)),
                ('joiningdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistationFormDB',
            fields=[
                ('slID', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('ChooseJobOrInternship', models.CharField(max_length=50)),
                ('ChooseFieldOfInterest', models.CharField(max_length=50)),
                ('HighestQualification', models.CharField(max_length=50)),
                ('CollegeName', models.CharField(max_length=100)),
                ('MajorFieldOfStudy', models.CharField(max_length=50)),
                ('YearOfGraduation', models.IntegerField(blank=True, null=True)),
                ('WorkExperienceIfAny', models.TextField(blank=True, null=True)),
                ('GitHubProfile', models.URLField(blank=True, default='')),
                ('LinkedInProfile', models.URLField(blank=True, default='')),
                ('ResumePDF', models.FileField(blank=True, null=True, upload_to='Resumes')),
                ('otp', models.IntegerField()),
                ('otpStatus', models.CharField(max_length=50)),
                ('peymentStatus', models.CharField(max_length=50)),
                ('odrTime', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
