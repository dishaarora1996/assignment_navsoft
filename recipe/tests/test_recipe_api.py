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
    
