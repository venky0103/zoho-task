from flask import Blueprint, request, jsonify
from api.models import db, MenuItemModel, CategoryModel, MealModel

app = Blueprint('api', __name__)

@app.route('/meal/<string:meal_name>', methods=['GET'])
def get_meal(meal_name):
    meal = MealModel.query.filter_by(name=meal_name).first()
    if meal:
        categories = {cat.name: [item.name for item in cat.items] for cat in meal.categories}
        return jsonify({"name": meal.name, "categories": categories}), 200
    return jsonify({"error": "Meal not found"}), 404

@app.route('/meal/<string:meal_name>/category', methods=['POST'])
def add_category(meal_name):
    data = request.json
    category_name = data.get('name')
    meal = MealModel.query.filter_by(name=meal_name).first()
    if not meal:
        meal = MealModel(name=meal_name)
        db.session.add(meal)
    category = CategoryModel(name=category_name, meal=meal)
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category added"}), 201

@app.route('/meal/<string:meal_name>/item', methods=['POST'])
def add_menu_item(meal_name):
    data = request.json
    category_name = data.get('category')
    item_name = data.get('name')
    item_description = data.get('description')
    meal = MealModel.query.filter_by(name=meal_name).first()
    if not meal:
        return jsonify({"error": "Meal not found"}), 404
    category = CategoryModel.query.filter_by(name=category_name, meal_id=meal.id).first()
    if not category:
        return jsonify({"error": "Category not found"}), 404
    menu_item = MenuItemModel(name=item_name, description=item_description, category=category)
    db.session.add(menu_item)
    db.session.commit()
    return jsonify({"message": "Menu item added"}), 201

@app.route('/meal/<string:meal_name>/category/<string:category_name>', methods=['GET'])
def get_category(meal_name, category_name):
    meal = MealModel.query.filter_by(name=meal_name).first()
    if meal:
        category = CategoryModel.query.filter_by(name=category_name, meal_id=meal.id).first()
        if category:
            items = [item.name for item in category.items]
            return jsonify({"name": category.name, "items": items}), 200
        return jsonify({"error": "Category not found"}), 404
    return jsonify({"error": "Meal not found"}), 404
