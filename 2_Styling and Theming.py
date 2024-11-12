from bokeh.plotting import figure, show

# Création d'une figure
p = figure(title="Styling Example", x_axis_label='X-Axis', y_axis_label='Y-Axis')

# Ajouter une ligne avec des styles personnalisés
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5],
       line_color="blue", line_width=3, line_dash="dashed")

# Personnaliser le titre
p.title.text_font_size = "20pt"
p.title.align = "center"
p.title.text_color = "darkred"

# Personnaliser les axes
p.xaxis.axis_label_text_color = "green"
p.yaxis.axis_label_text_font = "times"
p.yaxis.axis_label_text_font_style = "italic"

# Afficher le tracé
show(p)