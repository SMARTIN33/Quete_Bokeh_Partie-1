from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Données d'origine
data = {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 2, 4, 5]}

# Transformation des données : ici on multiplie les valeurs de y par 2
data['y_transformed'] = [val * 2 for val in data['y']]

# Créer une source de données avec les données transformées
source = ColumnDataSource(data=data)

# Créer un graphique et lier la source de données
p = figure(title="Exemple d'utilisation de ColumnDataSource avec transformation", x_axis_label='X-Axis', y_axis_label='Y-Axis')

# Ajouter une ligne pour les données originales
p.line('x', 'y', source=source, line_width=2, color="blue", legend_label="Données originales")
# Ajouter une ligne pour les données transformées
p.line('x', 'y_transformed', source=source, line_width=2, color="green", legend_label="Données transformées")

# Afficher le tracé
show(p)