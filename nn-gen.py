import numpy as np

number_layers = int(input("How many layers are there?"))
neurons = {}
for layer in range(number_layers):
    number_neurons = int(input(f"How many neurons in layer {layer}?"))
    neurons[layer] = [(2*layer,i+0.5-number_neurons/2) for i in range(number_neurons)] 
    
string = r"\begin{tikzpicture}"+"\n"
for layer in range(number_layers):
    for x_neuron, y_neuron in neurons[layer]:
        string += f"\draw ({x_neuron}, {y_neuron}) circle (0.5);\n"
        string += "\\node at (%f,%f) {\(%.2f\)};\n" % (x_neuron, y_neuron, np.random.random())
for layer_out in range(number_layers-1):
    layer_in = layer_out + 1
    for x_neuron_out, y_neuron_out in neurons[layer_out]:
        for x_neuron_in, y_neuron_in in neurons[layer_in]:
            string += f"\draw[->] ({x_neuron_out+0.5},{y_neuron_out}) -- ({x_neuron_in-0.5},{y_neuron_in});\n"

string += r"\end{tikzpicture}"
with open("output.txt","w") as file:
    file.write(string)
print(string)

