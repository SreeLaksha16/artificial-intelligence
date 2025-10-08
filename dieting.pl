% ======================================
% SIMPLE DIETING SYSTEM
% ======================================

% ---------- Person Profiles ----------
% person(Name, Age, Weight_kg, HealthGoal, AllergiesList).

person(alice, 25, 60, lose_weight, [nuts]).
person(bob, 35, 85, gain_muscle, []).
person(charlie, 50, 90, maintain_weight, [gluten]).
person(diana, 28, 55, lose_weight, [dairy]).

% ---------- Diet Plans ----------
% diet(DietName, SuitableGoal, FoodsIncluded, FoodsExcluded)

diet(low_carb, lose_weight, [eggs, chicken, fish, vegetables], [bread, rice, pasta]).
diet(high_protein, gain_muscle, [chicken, beef, eggs, beans], [sweets, soda]).
diet(vegetarian, maintain_weight, [vegetables, fruits, beans, grains], [meat, fish]).
diet(keto, lose_weight, [meat, fish, eggs, cheese, vegetables], [bread, pasta, rice, sweets]).

% ---------- Rules ----------
% A diet is suitable if:
% 1. Diet matches the person's health goal
% 2. Diet does not include any foods the person is allergic to

suitable_diet(PersonName, DietName) :-
    person(PersonName, _, _, Goal, Allergies),
    diet(DietName, Goal, IncludedFoods, ExcludedFoods),
    \+ (member(Allergy, Allergies), member(Allergy, IncludedFoods)).

% List all suitable foods for a person
recommended_foods(PersonName, Food) :-
    person(PersonName, _, _, Goal, Allergies),
    diet(DietName, Goal, IncludedFoods, _),
    \+ (member(Allergy, Allergies), member(Allergy, IncludedFoods)),
    member(Food, IncludedFoods).
