from django.core.management.base import BaseCommand 
from faker import Faker
import faker.providers
from courses.models import Programming, Business, Design, Management



PROGRAMMING_BOOKS = [
    'Python for beginners',
    'Python for data science',
    'Python for data analysis',
    'Python for data visualization',
    'Python for data engineering',
    'javascript for beginners',
    'DOM for beginners',
    'CSS for beginners',
    'HTML for beginners',
    'Java for beginners',
    'C++ for beginners',
    'C for beginners',
]

DESIGN_BOOK =[ 
    'Photoshop for beginners',
    'Illustrator for beginners',
    'InDesign for beginners',
    'After Effects for beginners',
    'Premiere for beginners',
    'Lightroom for beginners',
    'Premiere Pro for beginners',
    'After Effects CC for beginners',
]


BUSINESS_BOOK = [
    'Business for beginners',
    'Business for data science',
    'Business for data analysis',
    'Business for data visualization',
    'Business for data engineering',
    'Business for data modeling',
    'Business for data mining',
    'Business for data visualization',
    'Business for data engineering',
    'Business for data modeling',
    'Business for data mining',
]

MANAGEMENT_BOOK = [
    'Management for beginners',
    'Management for data science',
    'Management for data analysis',
    'Management for data visualization',
    'Management for data engineering',
]


class Provider(faker.providers.BaseProvider):
    def programming_book(self):
        return self.random_element(PROGRAMMING_BOOKS)

    def design_book(self):
        return self.random_element(DESIGN_BOOK)

    def business_book(self):
        return self.random_element(BUSINESS_BOOK)

    def management_book(self):
        return self.random_element(MANAGEMENT_BOOK)


class Command(BaseCommand):
    """
        creates command 

    Args:   
        BaseCommand (_type_): _description_
    """ 
    help = "Creates data for the courses app"

    def handle(self, *args, **kwargs):
        fake = Faker() # a class to initialize the fake data
        fake.add_provider(Provider) # add the provider to the fake data
        for _ in range(5):
            d = fake.unique.management_book()
            
            Management.objects.create(
                name=d,
                description=fake.text(),
                image=fake.image_url(),
                is_enroll=fake.boolean(),
                slug=fake.slug()
            )
        
    
        # for i in range(10):