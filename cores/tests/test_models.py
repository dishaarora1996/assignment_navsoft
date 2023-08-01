def test_create_ingredient(self):
    """Test creating an ingredient is successful"""
    user = create_user()
    ingredient = Ingredient.objects.create(user=user, name="Ingredient1")
    self.assertEqual(str(ingredient), ingredient.name)
    