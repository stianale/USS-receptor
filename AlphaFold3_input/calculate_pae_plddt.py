import json
import numpy as np
import sys

def flatten(nested_list):
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def calculate_average_pae(json_file):
    try:
        # Load the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Extract the "pae" values
        pae_values = data.get("pae", [])
        
        if not pae_values:
            print("No 'pae' values found in the JSON file.")
            return None
        
        # If pae_values is a list of lists, flatten it
        if isinstance(pae_values[0], list):
            pae_values = flatten(pae_values)
        
        # Calculate the average
        average_pae = sum(pae_values) / len(pae_values)
        
        return average_pae
    
    except Exception as e:
        print(f"An error occurred while calculating PAE: {e}")
        return None

def calculate_average_plddt(file_path, chains=None):
    try:
        # Load the JSON data from the file
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Extract atom_chain_ids and atom_plddts
        atom_chain_ids = np.array(data['atom_chain_ids'])
        atom_plddts = np.array(data['atom_plddts'])
        
        if chains:
            # Filter the atom_plddts for the specified chains
            mask = np.isin(atom_chain_ids, chains)
            selected_plddts = atom_plddts[mask]
        else:
            # Use all atom_plddts if no specific chains are provided
            selected_plddts = atom_plddts
        
        # Calculate the average plDDT
        average_plddt = np.mean(selected_plddts)
        return average_plddt
    
    except Exception as e:
        print(f"An error occurred while calculating plDDT: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calculate_pae_plddt.py json_file [chain1 chain2 ...]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    chains = sys.argv[2:] if len(sys.argv) > 2 else None
    
    # Calculate the average pae
    avg_pae = calculate_average_pae(file_path)
    avg_plddt = calculate_average_plddt(file_path, chains)
    if avg_pae is not None and avg_plddt is not None:
        print(f"{avg_pae}\t{avg_plddt}")
