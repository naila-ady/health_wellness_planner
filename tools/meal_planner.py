from agents import function_tool
@function_tool
async def meal_planner(meal_plan:str) -> str:
    """
    A very simple and basic  Asian meal plans for difffernt diet types like
    vegeterians, vegans , Gluten_free and high_protien/low crab diets.
    """
    plan_key = meal_plan.lower().replace( " " ,"_")
    plans = {
        "vegetarian": [
            "Day 1: cabbage Soup + curd",
            "Day 2: Daal chawal + salad",
            "Day 3: Vegetable pulao + raita",
            "Day 4: Bhindi + chapati",
            "Day 5: Chana masala + rice",
            "Day 6: Matar paneer + roti",
            "Day 7: Mix veg curry + brown rice"
        ],
        "nonveg": [
            "Day 1: Boiled egg + paratha",
            "Day 2: Chicken curry + rice",
            "Day 3: Fish fry + chapati",
            "Day 4: Egg bhurji + roti",
            "Day 5: Chicken biryani + salad",
            "Day 6: Keema + chapati",
            "Day 7: Grilled fish + sautéed vegetables"
        ],
        "vegan": [
            "Day 1: Vegetable rice + coconut chutney",
            "Day 2: Daal + brown rice + salad",
            "Day 3: vegetable pasta + tomato sauce ",
            "Day 4: Chickpea curry + roti (no ghee)",
            "Day 5: Baingan bharta + bajra roti",
            "Day 6: Veg pulao + mint chutney",
            "Day 7: Masoor daal + steamed rice"
        ],
        "gluten free": [
            "Day 1: Boiled egg + fruit",
            "Day 2: Daal + rice + salad",
            "Day 3: Grilled chicken + spinach",
            "Day 4: Besan roti + mint chutney",
            "Day 5: Fish curry + rice",
            "Day 6: chickenStake + mashed potatoes",
            "Day 7: Moong daal soup + salad"
        ],
        "high protein": [
            "Day 1: Egg omelet + sautéed spinach",
            "Day 2: Grilled chicken + stir-fried cabbage",
            "Day 3: Boiled lentils + cucumber salad",
            "Day 4: Keema (minced meat) + green beans",
            "Day 5: Tandoori fish + mixed veggies",
            "Day 6: Scrambled paneer + salad",
            "Day 7: Chicken tikka + low-carb roti"
        ]
    }
    
    if plan_key in plans:
        return "\n".join(plans[plan_key])
    else:
        return "❌ Invalid diet type. Please choose from vegetarian, nonveg, vegan, gluten_free, high_protein."
