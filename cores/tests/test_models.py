def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)




def test_create_tag(self):
    """Test creating a tag is successful"""
    user = create_user()
    tag= Tag.objects.create(user=user, name="Tag1")

    self.assertEqual(str(tag), tag.name)
    
