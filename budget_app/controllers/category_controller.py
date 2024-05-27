from models.category import Category

class CategoryController:
    def add_category(self, name, subcategories):
        category = Category(name, subcategories)
        category.save()
    
    def get_all_categories(self):
        return Category.get_all()
