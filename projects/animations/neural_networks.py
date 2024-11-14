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
            Text("Input Layer", color=CUSTOM_LIGHT_BLUE_1)
            .scale(0.7)
            .next_to(input_neurons, LEFT * 2)
        )

        # Rectangle around the input neurons
        input_box = SurroundingRectangle(
            input_neurons, color=CUSTOM_LIGHT_BLUE_1, buff=0.2
        )
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
            Text("Hidden Layers", color=CUSTOM_LIGHT_PINK_1)
            .scale(0.7)
            .next_to(hidden_neurons, UP)
        )

        #  Rectangle around the hidden neurons
        input_box = SurroundingRectangle(
            hidden_neurons, color=CUSTOM_LIGHT_PINK_1, buff=0.2
        )
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
            Text("Output Layer", color=CUSTOM_LIGHT_GREEN_1)
            .scale(0.7)
            .next_to(output_neurons, RIGHT)
        )

        #  Rectangle around the output neurons
        input_box = SurroundingRectangle(
            output_neurons, color=CUSTOM_LIGHT_GREEN_1, buff=0.2
        )
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


class BLACK_BOX_MLP(Scene):
    def construct(self):
        # Create black box with reduced width
        black_box = Rectangle(
            height=3, width=5, fill_color=GRAY_D, fill_opacity=0.8, stroke_color=WHITE
        )
        black_box_label = (
            Text("Neural Network", color=WHITE).scale(0.8).next_to(black_box, UP)
        )

        # Adjust input and output arrows
        input_arrow = Arrow(LEFT * 5, LEFT * 2.5, buff=0, color=CUSTOM_OFF_WHITE_1)
        output_arrow = Arrow(RIGHT * 2.5, RIGHT * 5, buff=0, color=CUSTOM_OFF_WHITE_1)

        # Create the equation with separate parts
        equation = (
            MathTex(
                r"z^{(l)}",
                "=",
                r"W^{(l)}",
                r"\cdot",
                r"a^{(l-1)}",
                "+",
                r"b^{(l)}",
                color=CUSTOM_OFF_WHITE_1,
            )
            .scale(0.8)
            .next_to(black_box, DOWN, buff=0.5)
        )

        # Create input shapes
        shapes = (
            VGroup(
                Circle(radius=0.5, fill_color=RED, fill_opacity=1, stroke_width=0),
                Square(side_length=1, fill_color=BLUE, fill_opacity=1, stroke_width=0),
                Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0),
            )
            .arrange(DOWN, buff=0.7)
            .scale(0.6)
            .next_to(input_arrow, LEFT, buff=0.5)
        )

        # Define a list of colors corresponding to the predictions
        prediction_colors = [RED, BLUE, GREEN]

        # Create output predictions
        predictions = (
            VGroup(
                Text("Red", color=RED),
                Text("Blue", color=BLUE),
                Text("Green", color=GREEN),
            )
            .arrange(DOWN, buff=0.7)
            .scale(0.6)
            .next_to(output_arrow, RIGHT, buff=0.5)
        )

        # Add input and output labels
        input_label = Text("Input", color=CUSTOM_OFF_WHITE_1).next_to(
            black_box_label, 6 * LEFT, buff=0.5
        )
        output_label = Text("Output", color=CUSTOM_OFF_WHITE_1).next_to(
            black_box_label, 6 * RIGHT, buff=0.5
        )

        # Animate black box representation
        self.play(
            Create(black_box),
            Write(black_box_label),
            GrowArrow(input_arrow),
            GrowArrow(output_arrow),
            Write(input_label),
            Write(output_label),
        )
        self.wait(1)
        self.play(Write(equation))
        self.wait(2)

        # Show input shapes and predictions
        for index, (shape, prediction) in enumerate(zip(shapes, predictions)):
            color = prediction_colors[index]  # Use the index to get the color
            input_text = MathTex("a^{(l-1)}", color=shape.get_color()).next_to(
                input_arrow, UP
            )
            output_text = MathTex("z^{(l)}").next_to(output_arrow, UP)
            # Ensure output_text is added to the scene
            self.play(
                FadeIn(shape),
                Write(input_text),
                shape.animate.next_to(input_arrow, LEFT, buff=0.5),
                run_time=0.5,
            )
            explanation_text = Tex(
                r"We now multiply our value ",
                r"$a^{(l-1)}$",
                r" by the weight ",
                r"$W^{(l)}$",
                r" and sum the bias ",
                r"$b^{(l)}$",
                color=CUSTOM_OFF_WHITE_1,
                font_size=36,
            ).next_to(equation, DOWN)
            self.play(Write(explanation_text))
            self.wait(2)
            self.play(
                equation.get_part_by_tex(r"a^{(l-1)}").animate.set_color(
                    shape.get_color()
                ),
                explanation_text[1].animate.set_color(shape.get_color()),
            )
            self.wait(2)
            self.play(
                shape.animate.move_to(black_box.get_left() + RIGHT * 0.5), run_time=1
            )

            self.play(
                Indicate(input_text, color=CUSTOM_OFF_WHITE_1),
                Indicate(
                    equation.get_part_by_tex(r"a^{(l-1)}"), color=CUSTOM_OFF_WHITE_1
                ),
                equation.get_part_by_tex(r"W^{(l)}").animate.set_color(YELLOW),
                equation.get_part_by_tex(r"b^{(l)}").animate.set_color(YELLOW),
                explanation_text[3].animate.set_color(YELLOW),
                explanation_text[5].animate.set_color(YELLOW),
            )
            self.wait(2)
            second_explanation_text = Tex(
                r"Once we calculated the value from the equation we obtain the value ",
                r"$z^{(l)}$",
                color=CUSTOM_OFF_WHITE_1,
                font_size=36,
            ).next_to(equation, 2.5 * DOWN)
            second_explanation_text[1].set_color(color)
            self.play(Write(second_explanation_text))
            self.wait(2)
            self.play(
                Write(output_text),
            )
            self.wait(2)
            self.play(
                Indicate(
                    equation.get_part_by_tex(r"z^{(l)}").set_color(color),
                    color=CUSTOM_OFF_WHITE_1,
                ),
                Indicate(output_text.set_color(color), color=CUSTOM_OFF_WHITE_1),
            )
            self.wait(2)

            # Animate prediction text from output arrow
            prediction.move_to(output_arrow.get_center() + RIGHT * 0.5)
            self.play(prediction.animate.next_to(output_arrow, RIGHT, buff=0.5))
            self.wait(2)

            # Reset colors to CUSTOM_OFF_WHITE_1 before the next iteration
            self.play(
                equation.get_part_by_tex(r"a^{(l-1)}").animate.set_color(
                    CUSTOM_OFF_WHITE_1
                ),
                equation.get_part_by_tex(r"W^{(l)}").animate.set_color(
                    CUSTOM_OFF_WHITE_1
                ),
                equation.get_part_by_tex(r"b^{(l)}").animate.set_color(
                    CUSTOM_OFF_WHITE_1
                ),
                equation.get_part_by_tex(r"z^{(l)}").animate.set_color(
                    CUSTOM_OFF_WHITE_1
                ),
                output_text.animate.set_color(CUSTOM_OFF_WHITE_1),
            )
            self.wait(1)

            # Fade out objects and phrases before the next iteration
            self.play(
                FadeOut(input_text),
                FadeOut(output_text),
                FadeOut(shape),
                FadeOut(explanation_text),  # Fade out the first explanation text
                FadeOut(
                    second_explanation_text
                ),  # Fade out the second explanation text
                FadeOut(prediction),  # Fade out the prediction text
            )
            self.wait(1)

        self.wait(2)


class DetailedMLP(Scene):
    def construct(self):
        # Scale down the entire scene
        scale_factor = 1

        # Create black box with reduced width
        black_box = Rectangle(
            height=4 * scale_factor,
            width=8 * scale_factor,
            fill_color=GRAY_D,
            fill_opacity=0.8,
            stroke_color=WHITE,
        )
        black_box_label = (
            Text("Neural Network", color=WHITE)
            .scale(0.8 * scale_factor)
            .next_to(black_box, UP)
        )

        # Add input and output labels
        input_label = (
            Text("Input", color=CUSTOM_OFF_WHITE_1)
            .scale(scale_factor)
            .next_to(black_box_label, 6 * LEFT * scale_factor, buff=0.5 * scale_factor)
        )
        output_label = (
            Text("Output", color=CUSTOM_OFF_WHITE_1)
            .scale(scale_factor)
            .next_to(black_box_label, 6 * RIGHT * scale_factor, buff=0.5 * scale_factor)
        )

        # Create neurons for input, hidden, and output layers
        input_neurons = (
            VGroup(
                *[
                    Circle(radius=0.3 * scale_factor, color=CUSTOM_LIGHT_BLUE_1)
                    for _ in range(3)
                ]
            )
            .arrange(DOWN, buff=0.5 * scale_factor)
            .shift(LEFT * 3 * scale_factor)
        )

        hidden_neurons = VGroup(
            *[
                Circle(radius=0.3 * scale_factor, color=CUSTOM_LIGHT_PINK_1)
                for _ in range(3)
            ]
        ).arrange(DOWN, buff=0.5 * scale_factor)

        output_neurons = (
            VGroup(
                *[
                    Circle(radius=0.3 * scale_factor, color=CUSTOM_LIGHT_GREEN_1)
                    for _ in range(3)
                ]
            )
            .arrange(DOWN, buff=0.5 * scale_factor)
            .shift(RIGHT * 3 * scale_factor)
        )

        # Add notation to neurons
        input_labels = VGroup(
            *[
                MathTex(f"a_{{{i+1}}}^{{(0)}}")
                .scale(0.5 * scale_factor)
                .next_to(neuron, UR + LEFT, buff=0.1 * scale_factor)
                for i, neuron in enumerate(input_neurons)
            ]
        )

        hidden_labels = VGroup(
            *[
                MathTex(f"a_{{{i+1}}}^{{(1)}}")
                .scale(0.5 * scale_factor)
                .next_to(neuron, UR + LEFT, buff=0.1 * scale_factor)
                for i, neuron in enumerate(hidden_neurons)
            ]
        )

        output_labels = VGroup(
            *[
                MathTex(f"a_{{{i+1}}}^{{(2)}}")
                .scale(0.5 * scale_factor)
                .next_to(neuron, UR + LEFT, buff=0.1 * scale_factor)
                for i, neuron in enumerate(output_neurons)
            ]
        )

        # Connections between layers
        connections_input_hidden = VGroup(
            *[
                Line(i.get_right(), h.get_left(), color=CUSTOM_OFF_WHITE_1)
                for i in input_neurons
                for h in hidden_neurons
            ]
        )

        connections_hidden_output = VGroup(
            *[
                Line(h.get_right(), o.get_left(), color=CUSTOM_OFF_WHITE_1)
                for h in hidden_neurons
                for o in output_neurons
            ]
        )

        # Group all elements to move them together
        scene_elements = VGroup(
            black_box,
            black_box_label,
            input_label,
            output_label,
            input_neurons,
            hidden_neurons,
            output_neurons,
            input_labels,
            hidden_labels,
            output_labels,
            connections_input_hidden,
            connections_hidden_output,
        )

        # Center the entire scene
        scene_elements.move_to(ORIGIN)

        # Animate the scene
        self.play(
            Create(black_box),
            Write(black_box_label),
            Write(input_label),
            Write(output_label),
            FadeIn(input_neurons),
            FadeIn(hidden_neurons),
            FadeIn(output_neurons),
            Create(connections_input_hidden),
            Create(connections_hidden_output),
            FadeIn(input_labels),
            FadeIn(hidden_labels),
            FadeIn(output_labels),
        )
        self.wait(1)

        # Define a common starting point for the connections
        common_start_point = DOWN*0.3 + LEFT * 5 * scale_factor

        # Create connections from the common start point to each input neuron
        input_connections = VGroup(
            *[
                Line(common_start_point, neuron.get_left(), color=CUSTOM_OFF_WHITE_1)
                for neuron in input_neurons
            ]
        )

        # Animate connections
        self.play(Create(input_connections))
        self.wait(1)

        input_connections_animation = VGroup(
            *[
                Line(common_start_point, neuron.get_center(), color=CUSTOM_OFF_WHITE_1)
                for neuron in input_neurons
            ]
        )

        # Create a static circle at the common start point
        static_circle = Circle(
            radius=0.2 * scale_factor,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=0,
        ).move_to(common_start_point)

        # Add the static circle to the scene
        self.add(static_circle)

        # Create input shapes (copies of the static circle)
        shapes = VGroup(
            *[
                static_circle.copy()
                for _ in range(3)
            ]
        )

        # Animate each shape moving along its connection to the input neurons
        self.play(
            *[
                MoveAlongPath(shape, connection)
                for shape, connection in zip(shapes, input_connections_animation)
            ],
            run_time=2,
        )

        self.wait(2)

        # Transition for the first neuron a^(0)_0
        first_neuron = input_neurons[0]
        self.play(Indicate(first_neuron, color=YELLOW))

        # Add a value of 1.0 inside the first neuron if the shape is red
        if static_circle.get_fill_color() == RED:
            value_text = MathTex("1.0").move_to(first_neuron.get_center())
            self.play(Write(value_text))

        self.wait(1)

        # Add final text below the box
        final_text = Text(
            "Computation for the first neuron a^{(0)}_0 is complete.",
            color=CUSTOM_OFF_WHITE_1,
            font_size=20 * scale_factor
        ).next_to(black_box, DOWN, buff=0.5 * scale_factor)

        self.play(Write(final_text))
        self.wait(2)


class NeuronComputationScene(Scene):
    def __init__(self, weight, bias, input_value, color, **kwargs):
        super().__init__(**kwargs)
        self.weight = weight
        self.bias = bias
        self.input_value = input_value
        self.color = color

    def construct(self):
        # Create a group to hold all elements
        computation_group = VGroup()

        # Left side: Display initial values
        left_title = (
            Text("Initial Conditions", color=WHITE)
            .scale(0.8)
            .to_edge(LEFT)
            .shift(UP * 3.5)
        )
        weight_text = (
            MathTex(r"w^{(2)}_0 = ", f"{self.weight}")
            .scale(0.8)
            .to_edge(LEFT)
            .shift(UP * 2.8)
        )
        bias_text = (
            MathTex(r"b^{(2)}_0 = ", f"{self.bias}")
            .scale(0.8)
            .next_to(weight_text, DOWN, aligned_edge=LEFT)
        )
        input_text = (
            MathTex(r"a^{(0)} = ", f"{self.input_value}")
            .scale(0.8)
            .next_to(bias_text, DOWN, aligned_edge=LEFT)
        )
        input_object = Circle(
            radius=0.3, fill_color=self.color, fill_opacity=1
        ).next_to(input_text, RIGHT)

        computation_group.add(
            left_title, weight_text, bias_text, input_text, input_object
        )

        # Bottom left: Show Sigmoid activation function graph
        axes = (
            Axes(
                x_range=[-2, 2, 0.5], y_range=[0, 1, 0.2], axis_config={"color": WHITE}
            )
            .scale(0.3)
            .to_edge(LEFT)
            .shift(DOWN * 2.5 + RIGHT * 0.5)
        )  # Adjust the graph position to the left

        sigmoid_graph = axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=YELLOW)
        activation_function_text = (
            Text("Activation Function: Sigmoid", font_size=36)
            .scale(0.8)
            .next_to(input_text, DOWN, aligned_edge=LEFT)
            .shift(DOWN * 1)
        )
        sigmoid_label = (
            MathTex(r"\sigma(x) = \frac{1}{1 + e^{-x}}")
            .scale(0.8)
            .next_to(activation_function_text, DOWN, aligned_edge=LEFT)
        )

        computation_group.add(
            axes, sigmoid_graph, activation_function_text, sigmoid_label
        )

        # Divider between left and right sections
        divider = Line(
            start=UP * 3 + LEFT * 1.5, end=DOWN * 3 + LEFT * 1.5, color=WHITE
        )
        computation_group.add(divider)

        # Right side: Display equation with symbols
        right_title = (
            Text("Calculations", color=WHITE)
            .to_edge(RIGHT)
            .shift(UP * 3.5 + LEFT * 0.5)
        )
        equation_symbols = (
            MathTex(
                r"z^{(2)}_0",
                "=",
                r"w^{(2)}_0",
                r"\cdot",
                r"a^{(0)}",
                "+",
                r"b^{(2)}_0",
                color=CUSTOM_OFF_WHITE_1,
            )
            .to_edge(RIGHT)
            .shift(UP * 2 + LEFT * 0.5)
        )

        # Color the symbols
        equation_symbols.set_color_by_tex(r"w^{(2)}_0", YELLOW)
        equation_symbols.set_color_by_tex(r"a^{(0)}", BLUE)
        equation_symbols.set_color_by_tex(r"b^{(2)}_0", GREEN)

        computation_group.add(right_title, equation_symbols)

        # Calculate the weighted sum
        weighted_sum = np.dot(self.weight, self.input_value) + self.bias

        # Calculate the output using the sigmoid function
        output_value = 1 / (1 + np.exp(-weighted_sum))

        # Show the result of w * a + b
        weighted_sum_text = MathTex(
            r"z^{(2)}_0 = ",
            f"{self.weight}",
            r"\cdot",
            f"{self.input_value}",
            r"+",
            f"{self.bias}",
            "=",
            f"{weighted_sum:.2f}",
        ).next_to(equation_symbols, DOWN)

        # Color the components
        weighted_sum_text.set_color_by_tex(str(self.weight), YELLOW)
        weighted_sum_text.set_color_by_tex(str(self.input_value), BLUE)
        weighted_sum_text.set_color_by_tex(str(self.bias), GREEN)

        computation_group.add(weighted_sum_text)

        # Indicate that the result is being passed to the activation function
        activation_step_text = Text("Activation Function", color=WHITE).next_to(
            weighted_sum_text, DOWN * 2.0
        )
        computation_group.add(activation_step_text)

        # Show the output of the Sigmoid function
        sigmoid_output_text = MathTex(
            r"a^{(2)}_0 = \sigma(",
            f"{weighted_sum:.2f}",
            r")",
        ).next_to(activation_step_text, DOWN * 2.5)

        computation_group.add(sigmoid_output_text)

        point = Dot(axes.c2p(weighted_sum, 1 / (1 + np.exp(-weighted_sum))), color=RED)
        computation_group.add(point)

        # Add an arrow from the sigmoid graph to the result
        sigmoid_output_text_result = MathTex(
            r"a^{(2)}_0 = ",
            f"{1 / (1 + np.exp(-weighted_sum)):.2f}",
        ).next_to(sigmoid_output_text, DOWN * 2.5)

        arrow = Arrow(
            start=axes.c2p(weighted_sum, 1 / (1 + np.exp(-weighted_sum))),
            end=sigmoid_output_text_result.get_left(),
            buff=0.1,
            color=WHITE,
        )
        computation_group.add(arrow, sigmoid_output_text_result)

        # Highlight the final result and add a label
        output_label = Text("Output of the neuron", color=WHITE).next_to(
            sigmoid_output_text_result, DOWN
        )
        computation_group.add(output_label)

        # Position the entire computation group inside the scene
        computation_group.move_to(ORIGIN)

        # Play all animations
        self.play(
            Write(left_title),
            Write(weight_text),
            Write(bias_text),
            Write(input_text),
            FadeIn(input_object),
            Write(activation_function_text),
            Write(sigmoid_label),
            Create(axes),
            Create(sigmoid_graph),
            Create(divider),
            Write(right_title),
            Write(equation_symbols),
            Write(weighted_sum_text),
            Write(activation_step_text),
            Write(sigmoid_output_text),
            FadeIn(point),
            Create(arrow),
            Write(sigmoid_output_text_result),
            Indicate(sigmoid_output_text_result, color=GREEN),
            sigmoid_output_text_result.animate.set_color(GREEN),
            Write(output_label),
        )
        self.wait(2)

        # Clean up at the end
        self.play(FadeOut(computation_group))

        # Return the computed output value
        return output_value



