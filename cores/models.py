class Recipe(models.Model):
    ingredients = models.ManyToManyField('Ingredient')


class Ingredient(models.Model):
    """Ingredient for recipes"""
    name = models.CharField(max_length=255)
    user = models.ForeignField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



run command: docker-compose run --rm app sh -c "python manage.py makemigrations"

admin.site.register(Ingredient)

run command: docker-compose run --rm app sh -c "python manage.py run test"
