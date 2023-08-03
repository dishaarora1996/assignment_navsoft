def test_create_tag_on_update(self):
    """Test creating tag when updating a recipe"""
    recipe = create_recipe(user=self.user)
    
    payload = {
        'tags': [{'name:' 'Lunch'}]
    }

    url = detail_url(recipe.id)
    res = self.client.patch(url, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    new_tag = Tag.objects.get(user=self.user, name='Lunch')
    self.assertIn(new_tag, recipe.tags.all())


def test_update_recipe_assign_tag(self):
    """Test assigning an existing tag when updating a recipe"""
    tag_breakfast = Tag.objects.create(user=self.user, name='Breakfast')
    recipe = create_recipe(user=self.user)
    recipe.tags.add(tag_breakfast)

    tag_lunch = Tag.objects.create(user=self.user, name='Lunch')
    payload = {
        'tags': [{'name': 'Lunch'}]
    }

    url = detail_url(recipe.id)
    res = self.client.patch(url, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertIn(tag_lunch, recipe.tags.all())
    self.assertNotIn(tag_breakfast, recipe.tags.all())


def test_clear_recipe_tags(self):
    """Test clearing a recipe tags"""
    tag = Tag.objects.create(user=self.user, name='Dessert')
    recipe = create_recipe(user=self.user)
    recipe.tags.add(tag)

    payload ={
        'tags': []
    }

    url = detail_url(recipe.id)
    res = self.client.patch(url, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(recipe.tags.count(), 0)

#03-08-2023

def test_create_recipe_with_new_ingredients(self):
    """Test creating recipe with new ingredients."""
    payload ={
        'title': 'Cauliflower Tacos',
        'time_minutes': 60,
        'price': Decimal('4.30'),
        'ingredients': [{'name': 'Cauliflower'}, {'name': 'Salt'}],
    }

    res = self.client.post(RECIPES_URL, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipes = Recipe.objects.filter(user=self.user)
    self.assertEqual(recipes.count(), 1)
    recipe = recipes[0]
    self.assertEqual(recipe.ingredients.count(), 2)
    for ingredient in payload['ingredients']:
        exists = recipe.ingredients.filter(
            name=ingredient['name'],
            user=self.user
        ).exists()
        self.assertTrue(exists)

def test_create_recipe_with_existing_ingredients(self):
    """Test creating a new recipe with existing ingredient."""
    ingredient = Ingredient.objects.create(user=self.user, name="Lemon")
    payload = {
        'title': 'Vietnamese Soup',
        'time_minutes': '25',
        'price': '2.55',
        'ingredients': [{'name': 'Lemon'}, {'name': 'Fish Sauce'}]
    }
    res = self.client.post(RECIPES_URL, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipes = Recipe.objects.filter(user=self.user)
    self.assertEqual(recipes.count(), 1)
    recipe = recipes[0]
    self.assertEqual(recipe.ingredients.count(), 2)
    self.assertIn(ingredient, recipe.ingredients.all())
    for ingredient in payload['ingredients']:
        exists = recipe.ingredients.filter(
            name=ingredient['name'],
            user=self.user
        ).exists()
        self.assertTrue(exists)

    
