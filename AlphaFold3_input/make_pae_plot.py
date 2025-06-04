import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

def plot_pae_af3_style(pae_matrix, protein_length, na_length, output_folder):
    matrix_size, _ = pae_matrix.shape
    expected_size = protein_length + na_length

    if matrix_size != expected_size:
        raise ValueError(
            f"PAE matrix size {matrix_size} does not match expected size {expected_size}."
        )

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Define desired pixel dimensions and DPI
    pixel_width = 447
    pixel_height = 576
    dpi = 100
    figsize = (pixel_width / dpi, pixel_height / dpi)

    # Create a custom colormap from white to green
    custom_cmap = LinearSegmentedColormap.from_list("white_to_green", ["green", "white"])

    # Plot the PAE matrix
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    im = ax.imshow(pae_matrix, cmap=custom_cmap, interpolation="nearest")

    # Create a colorbar that matches the x-axis width
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("bottom", size="5%", pad=0.5)
    cbar = plt.colorbar(im, cax=cax, orientation="horizontal")
    cbar.set_label("Expected Position Error (Ångströms)")

    ax.set_title("")
    ax.set_xlabel("Scored Residue")
    ax.set_ylabel("Aligned Residue")
    plt.tight_layout()


    # Extract the last three elements of the input file path
    path_parts = json_file.strip("/").split("/")  # Split path into parts
    last_three_parts = "_".join(path_parts[-5:-4])  # Join the last three elements with "_"
    # Construct output filename
    output_filename = os.path.join(output_folder, f"{last_three_parts}_pae_plot.png")
    plt.savefig(output_filename, dpi=dpi)
    print(f"PAE plot saved as {output_filename}")
    plt.close(fig)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python make_pae_plot.py <json_file> <protein_length> <na_length> <output_folder>")
        sys.exit(1)

    json_file = sys.argv[1]
    protein_length = int(sys.argv[2])
    na_length = int(sys.argv[3])
    output_folder = sys.argv[4]

    # Load data from JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the PAE matrix from the JSON file
    if "pae" not in data:
        raise KeyError("The JSON file must contain a 'pae' key with the PAE matrix.")
    
    pae_matrix = np.array(data["pae"])
    print(f"PAE type: {type(pae_matrix)}")
    print(f"PAE dtype: {pae_matrix.dtype}")
    print(f"PAE shape: {pae_matrix.shape}")
    print(f"PAE sample data: {pae_matrix[:5, :5]}")  # Display sample data from the matrix

    plot_pae_af3_style(pae_matrix, protein_length, na_length, output_folder)
