from manim import *

class PerceptronTraining(Scene):
    def construct(self):
        # Crear un gráfico de dispersión inicial
        self.graph = Axes(
            x_range=[3.5, 7.5, 1],
            y_range=[1.5, 5.5, 1],
            axis_config={"include_numbers": True},
        )
        self.add(self.graph)

        # Puntos de datos
        data_points = [
            (5.1, 3.5, 0), (4.9, 3.0, 0), (4.7, 3.2, 0),
            (5.0, 3.6, 0), (6.4, 3.2, 1), (6.9, 3.1, 1),
            (5.5, 2.3, 1), (6.5, 2.8, 1), (5.7, 2.8, 1)
        ]
        colors = [RED, BLUE]

        # Añadir puntos al gráfico
        points = []
        for x, y, label in data_points:
            point = Dot(self.graph.coords_to_point(x, y), color=colors[label])
            points.append(point)
            self.add(point)

        # Añadir la línea de decisión
        self.line = self.graph.plot_line_graph(
            x_values=[3.5, 7.5],
            y_values=[3.5, 1.5],
            add_vertex_dots=False,
            line_color=YELLOW,
        )
        self.add(self.line)

        # Animar el proceso de entrenamiento
        for epoch in range(10):  # Simulación de 10 épocas
            self.play(self.update_line(epoch))
            self.wait(0.5)

    def update_line(self, epoch):
        # Función de actualización de la línea de decisión
        new_slope = -0.5 + epoch * 0.1
        new_intercept = 3.5 - epoch * 0.2
        new_line = self.graph.plot_line_graph(
            x_values=[3.5, 7.5],
            y_values=[new_slope * 3.5 + new_intercept, new_slope * 7.5 + new_intercept],
            add_vertex_dots=False,
            line_color=YELLOW,
            stroke_width=5,
        )
        return Transform(self.line, new_line)

if __name__ == "__main__":
    from manim import config, tempconfig
    config.media_width = "100%"
    config.verbosity = "WARNING"
    import sys
    from manim import *

    scene = PerceptronTraining()
    scene.render()
