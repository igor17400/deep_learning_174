from manim import *

# Custom colors
CUSTOM_FIRST = ManimColor("#384B70")
CUSTOM_SECOND = ManimColor("#507687")
CUSTOM_THIRD = ManimColor("#FCFAEE")
CUSTOM_FOURTH = ManimColor("#B8001F")

# Define the scene for the neural network forward pass visualization
class NeuralNetworkForwardPass(Scene):
    def construct(self):
        # Create the layers
        input_neurons = self.create_layer([-5, 1.5, 0], 3, "x")
        hidden_neurons = self.create_layer([0, 1.5, 0], 3, "h")
        output_neurons = self.create_layer([5, 1.5, 0], 1, "z")

        # Add layer labels
        self.add_layer_labels(input_neurons, hidden_neurons, output_neurons)

        # Connect layers with arrows and display equations
        self.connect_layers(input_neurons, hidden_neurons, "w_1", "b_1")
        self.connect_layers(hidden_neurons, output_neurons, "w_2", "b_2")

        # Animate forward pass
        self.play_forward_pass(input_neurons, hidden_neurons, output_neurons)

    def create_layer(self, position, num_neurons, label, has_y=False):
        """Create a layer of neurons at a specific position with labels."""
        neurons = VGroup()
        for i in range(num_neurons):
            neuron = Circle(radius=0.3, color=WHITE).move_to(
                position + np.array([0, -i * 1.5, 0])
            )
            neurons.add(neuron)
            neuron_label = MathTex(f"{label}_{{{i + 1}}}").move_to(neuron.get_center())
            self.add(neuron_label)
        self.add(neurons)
        return neurons

    def connect_layers(self, layer1, layer2, weight_label, bias_label):
        """Connect two layers of neurons with arrows and display equations."""
        for neuron1 in layer1:
            for neuron2 in layer2:
                arrow = Arrow(
                    neuron1.get_center(),
                    neuron2.get_center(),
                    stroke_width=3,  # Adjusts the thickness of the arrow
                    buff=0.3,  # Reduces the distance between the arrow and the neurons
                    color=CUSTOM_THIRD,
                    max_tip_length_to_length_ratio=0.05,  # Reduces the arrowhead size
                )
                self.add(arrow)

        # Add weight and bias labels
        mid_point = (layer1.get_center() + layer2.get_center()) / 2
        weight_eq = MathTex(f"W_{{{weight_label}}} y_{{1}} + {bias_label}").move_to(
            mid_point
        )
        self.add(weight_eq)

    def add_layer_labels(self, input_neurons, hidden_neurons, output_neurons):
        """Add labels for input, hidden, and output layers."""
        input_label = Text("Input Layer").next_to(input_neurons, UP)
        hidden_label = Text("Hidden Layer").next_to(hidden_neurons, UP)
        output_label = Text("Output Layer").next_to(output_neurons, UP)
        self.add(input_label, hidden_label, output_label)

    def play_forward_pass(self, input_neurons, hidden_neurons, output_neurons):
        """Animate forward pass through the network."""
        # Highlight input neurons
        self.play(
            *[neuron.animate.set_fill(YELLOW, opacity=0.8) for neuron in input_neurons]
        )
        self.wait(0.5)

        # Animate arrows between input and hidden layers
        self.play(
            *[neuron.animate.set_fill(ORANGE, opacity=0.8) for neuron in hidden_neurons]
        )
        self.wait(0.5)

        # Animate hidden-to-output connections
        self.play(output_neurons[0].animate.set_fill(RED, opacity=0.8))
        self.wait(1)
