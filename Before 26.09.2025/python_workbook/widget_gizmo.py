widget = int(input("How many widgets do you want? "))
gizmo = int(input("How many gizmos do you want? "))

weight_widget = 75
weight_gizmo = 112

print("Total weight of your order: %0.1f grams." %(widget*weight_widget + gizmo*weight_gizmo))
