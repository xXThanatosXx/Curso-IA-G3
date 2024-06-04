from manim import *

class PerceptronUpdate(Scene):
    def construct(self):
        # Dibujar la neurona
        neuron = Circle(radius=0.5, color=BLUE)
        neuron.move_to(ORIGIN)
        self.add(neuron)
        
        # Dibujar las entradas
        input1 = Dot(LEFT * 3 + UP, color=RED)
        input2 = Dot(LEFT * 3 + DOWN, color=RED)
        self.add(input1, input2)
        
        # Conectar entradas a la neurona
        input1_arrow = Arrow(input1.get_center(), neuron.get_left(), buff=0.1)
        input2_arrow = Arrow(input2.get_center(), neuron.get_left(), buff=0.1)
        self.add(input1_arrow, input2_arrow)
        
        # Etiquetas de las entradas
        input1_label = MathTex("x_1").next_to(input1, LEFT)
        input2_label = MathTex("x_2").next_to(input2, LEFT)
        self.add(input1_label, input2_label)
        
        # Etiquetas de los pesos
        weight1_label = MathTex("w_1").next_to(input1_arrow, UP)
        weight2_label = MathTex("w_2").next_to(input2_arrow, DOWN)
        self.add(weight1_label, weight2_label)
        
        # Salida de la neurona
        output = Dot(RIGHT * 3, color=GREEN)
        output_arrow = Arrow(neuron.get_right(), output.get_center(), buff=0.1)
        self.add(output, output_arrow)
        
        # Etiqueta de la salida
        output_label = MathTex("y").next_to(output, RIGHT)
        self.add(output_label)
        
        # Mostrar la fórmula de la salida
        output_formula = MathTex("y = \\sigma(w_1 x_1 + w_2 x_2 + b)")
        output_formula.to_edge(UP)
        self.add(output_formula)
        
        # Simulación de actualización de pesos
        for epoch in range(1, 6):
            new_weight1 = MathTex(f"w_1^{epoch}").next_to(input1_arrow, UP)
            new_weight2 = MathTex(f"w_2^{epoch}").next_to(input2_arrow, DOWN)
            self.play(Transform(weight1_label, new_weight1), Transform(weight2_label, new_weight2))
            self.wait(1)
            
        # Mostrar la fórmula de actualización de pesos
        update_formula = MathTex(
            "\\Delta w_i = \\eta (y_{true} - y_{pred}) x_i"
        )
        update_formula.next_to(output_formula, DOWN)
        self.add(update_formula)
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    import sys
    from manim import *
    
    scene = PerceptronUpdate()
    scene.render()
