def print_histogram(counts):
    """
    Renders a clean ASCII bar chart of quantum simulation results.
    """
    total_shots = sum(counts.values())
    print("\n--- QUANTUM PROBABILITY DISTRIBUTION ---")
    
    # Sort by bitstring (e.g., '0' before '1')
    for state in sorted(counts.keys()):
        count = counts[state]
        percentage = (count / total_shots) * 100
        
        # Create a bar: 20 characters max
        bar_length = int((percentage / 100) * 20)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        
        print(f"|{state}> {bar} {percentage:>5.1f}% ({count} shots)")
    print("-" * 41 + "\n")