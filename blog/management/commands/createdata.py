from django.core.management.base import BaseCommand, CommandError
from users.models import User
from blog.models import Post, Tags, Comments
from django.utils import timezone
# from django.core.files.images import ImageFile
from faker import Faker



class Command(BaseCommand):
    help = "helper blog"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(1, 50):
            user = User.objects.create(
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password='12345678',
                active=True,
                staff=True,
                superuser=False,
                timestamp=timezone.now()

            )
            for j in range(1, 10):
                post = Post.objects.create(
                    title=fake.sentence(),
                    content=fake.text(),
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    image = fake.image_url(),
                    # image = ImageFile(open('/home/ubuntu/workspace/blog/media/images/1.jpg', 'rb')),
                    # likes.set(),
                    # use like set() to add many users
                    # likes=Likes.set(),
                    author=user
                )
                for k in range(1, 10):
                    tags = Tags.objects.create(
                        name=fake.word()
                    )
                    post.tags.add(tags)
                for l in range(1, 10):
                    comments = Comments.objects.create(
                        content=fake.text(),
                        created_at=timezone.now(),
                        updated_at=timezone.now(),
                        post=post,
                        author=user
                    )
                    comments.save()

