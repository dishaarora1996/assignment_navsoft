

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model =[
            'ingredients'
        ]

    def _get_or_create_ingredients(self, ingredients, recipe):
        """Handle getting or ceating ingredients as needed."""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, create = Ingredient.objects.get_or_create(
                user=auth_user,
                **ingredient
            )
            recipe.ingredients.add(ingredient_obj)


    def create(self, **validated_data):
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_ingredients(ingredients, recipe)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializers for ingredients."""

    class Meta:
        model = Ingredient
        fields=['id', 'name']
        read_only_fields = ['id']

