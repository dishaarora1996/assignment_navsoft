
class Recipe(models.Model):
    tag = models.ManyToManyField('Tag')





class tag(models.Model):
    """Tag for filtering recipes"""
    name = models.CharField(max_lenght=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name
    

run docker-compose run --rm app sh -c "python manage.py makemigrations"

type yes for test_dev_db

register models in admin.py