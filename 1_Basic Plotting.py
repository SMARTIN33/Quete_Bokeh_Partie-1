from bokeh.plotting import figure, show

# Préparer les données
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Créer une figure
p = figure(title="Basic Line Plot", x_axis_label='X-Axis', y_axis_label='Y-Axis')

# Ajouter une ligne au graphique
p.line(x, y, legend_label="Line", line_width=2)

# Afficher le graphique
show(p)
