from manim import *
import numpy as np


CUSTOM_OFF_WHITE_1 = "#EEEEEE"
CUSTOM_YELLOW = "#FFD369"
CUSTOM_LIGHT_BLUE_1 = "#83B4FF"
CUSTOM_LIGHT_PINK_1 = "#FF4191"
CUSTOM_LIGHT_GREEN_1 = "#16FF00"

CUSTOM_BLUE_1 = "#3A6D8C"
CUSTOM_BLUE_2 = "#6A9AB0"
CUSTOM_BLUE_3 = "#001F3F"
CUSTOM_RED_1 = "#F95454"
CUSTOM_GREY_1 = "#D8D2C2"


class SIMPLE_MLP(Scene):
    def construct(self):
        # Title for the Scene
        title = Text("A simple MLP structure", color=CUSTOM_OFF_WHITE_1).to_edge(UP)
        self.add(title)

        # Step 1: Neural Network Diagram with Highlighted Layers
        # ------ Input Layer
        input_neurons = (
            VGroup(
                Circle(radius=0.3, color=CUSTOM_LIGHT_BLUE_1),  # Input neuron 1
                Circle(radius=0.3, color=CUSTOM_LIGHT_BLUE_1),  # Input neuron 2
                Circle(radius=0.3, color=CUSTOM_LIGHT_BLUE_1),  # Input neuron 3
            )
            .arrange(DOWN, buff=0.5)
            .shift(LEFT * 3)  # Move neurons to the left by 3 units
        )

        # Label for the input layer
        input_label = (
            Text("Input Layer", color=CUSTOM_LIGHT_BLUE_1).scale(0.7).next_to(input_neurons, LEFT * 2)
        )

        # Rectangle around the input neurons
        input_box = SurroundingRectangle(input_neurons, color=CUSTOM_LIGHT_BLUE_1, buff=0.2)
        input_box.set_stroke(color=CUSTOM_LIGHT_BLUE_1, width=1, opacity=0.5)

        # Animate the neurons, label, and dashed box
        self.play(FadeIn(input_neurons), Write(input_label), Create(input_box))

        # ------ Hidden Layer
        hidden_neurons = (
            VGroup(
                Circle(radius=0.3, color=CUSTOM_LIGHT_PINK_1),  # Hidden neuron 1
                Circle(radius=0.3, color=CUSTOM_LIGHT_PINK_1),  # Hidden neuron 2
                Circle(radius=0.3, color=CUSTOM_LIGHT_PINK_1),  # Hidden neuron 3
            )
            .arrange(DOWN, buff=0.5)
            .move_to(ORIGIN)
        )

        hidden_label = (
            Text("Hidden Layers", color=CUSTOM_LIGHT_PINK_1).scale(0.7).next_to(hidden_neurons, UP)
        )

        #  Rectangle around the hidden neurons
        input_box = SurroundingRectangle(hidden_neurons, color=CUSTOM_LIGHT_PINK_1, buff=0.2)
        input_box.set_stroke(color=CUSTOM_LIGHT_PINK_1, width=1, opacity=0.5)

        connections_input_hidden = VGroup()
        for input_neuron in input_neurons:
            for hidden_neuron in hidden_neurons:
                connections_input_hidden.add(
                    Line(
                        input_neuron.get_right(),
                        hidden_neuron.get_left(),
                        color=CUSTOM_OFF_WHITE_1,  # Changed from white to CUSTOM_OFF_WHITE_1
                    )
                )

        self.play(
            FadeIn(hidden_neurons),
            Write(hidden_label),
            Create(connections_input_hidden),
            Create(input_box),
        )

        #  ------- Output Layer
        output_neurons = (
            VGroup(
                Circle(radius=0.3, color=CUSTOM_LIGHT_GREEN_1),  # Output neuron 1
                Circle(radius=0.3, color=CUSTOM_LIGHT_GREEN_1),  # Output neuron 2
            )
            .arrange(DOWN, buff=0.5)
            .shift(RIGHT * 3)
        )

        output_label = (
            Text("Output Layer", color=CUSTOM_LIGHT_GREEN_1).scale(0.7).next_to(output_neurons, RIGHT)
        )

        #  Rectangle around the output neurons
        input_box = SurroundingRectangle(output_neurons, color=CUSTOM_LIGHT_GREEN_1, buff=0.2)
        input_box.set_stroke(color=CUSTOM_LIGHT_GREEN_1, width=1, opacity=0.5)

        connections_hidden_output = VGroup()
        for hidden_neuron in hidden_neurons:
            for output_neuron in output_neurons:
                connections_hidden_output.add(
                    Line(
                        hidden_neuron.get_right(),
                        output_neuron.get_left(),
                        color=CUSTOM_LIGHT_GREEN_1,  
                    )
                )

        self.play(
            FadeIn(output_neurons),
            Write(output_label),
            Create(connections_hidden_output),
            Create(input_box),
        )
        self.wait(3)
