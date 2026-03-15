from django.core.management.base import BaseCommand
from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification
from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping

class Command(BaseCommand):
    help = 'Seeds the database with initial sample data'

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        # Create Vendors
        vendor1, _ = Vendor.objects.get_or_create(code="VND001", defaults={"name": "Tech Vendor A", "description": "Leading tech provider"})
        vendor2, _ = Vendor.objects.get_or_create(code="VND002", defaults={"name": "Edu Vendor B", "description": "Education materials provider"})

        # Create Products
        prod1, _ = Product.objects.get_or_create(code="PRD001", defaults={"name": "Cloud Computing Basics", "description": "Intro to cloud"})
        prod2, _ = Product.objects.get_or_create(code="PRD002", defaults={"name": "Data Science Fundamentals", "description": "Intro to DS"})

        # Create Courses
        course1, _ = Course.objects.get_or_create(code="CRS001", defaults={"name": "AWS Solutions Architect", "description": "AWS prep course"})
        course2, _ = Course.objects.get_or_create(code="CRS002", defaults={"name": "Python for Data Science", "description": "Python data tools"})

        # Create Certifications
        cert1, _ = Certification.objects.get_or_create(code="CRT001", defaults={"name": "AWS Certified Architect", "description": "AWS certification"})
        cert2, _ = Certification.objects.get_or_create(code="CRT002", defaults={"name": "Data Science Associate", "description": "DS certification"})

        # Mappings
        vpm1, created1 = VendorProductMapping.objects.get_or_create(vendor=vendor1, product=prod1, defaults={"primary_mapping": True})
        vpm2, created2 = VendorProductMapping.objects.get_or_create(vendor=vendor2, product=prod2, defaults={"primary_mapping": True})

        pcm1, created3 = ProductCourseMapping.objects.get_or_create(product=prod1, course=course1, defaults={"primary_mapping": True})
        pcm2, created4 = ProductCourseMapping.objects.get_or_create(product=prod2, course=course2, defaults={"primary_mapping": True})

        ccm1, created5 = CourseCertificationMapping.objects.get_or_create(course=course1, certification=cert1, defaults={"primary_mapping": True})
        ccm2, created6 = CourseCertificationMapping.objects.get_or_create(course=course2, certification=cert2, defaults={"primary_mapping": True})

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
