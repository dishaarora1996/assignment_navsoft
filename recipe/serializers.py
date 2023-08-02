

class IngredientSerializer(serializers.ModelSerializer):
    """Serializers for ingredients."""

    class Meta:
        model = Ingredient
        fields=['id', 'name']
        read_only_fields = ['id']

