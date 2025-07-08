from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import transpile
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from teleportation import create_custom_circuit

def run_simulation(circuit_type="teleport", num_shots=1024):
    """Run the quantum teleportation simulation with Qiskit 2.0.2+ compatibility."""
    try:
        # Create the selected quantum circuit
        qc = create_custom_circuit(circuit_type)
        
        # Add measurement if not already present
        if not qc.num_clbits:
            qc.measure_all()  # Measures all qubits
        elif qc.num_qubits == qc.num_clbits:
            qc.measure(range(qc.num_qubits), range(qc.num_clbits))
        else:
            # Handle case where measurement might already be partially defined
            qc.measure_all(inplace=True)
        
        # Initialize simulator and transpile circuit
        simulator = AerSimulator()
        transpiled_qc = transpile(qc, simulator)
        
        # Run simulation with explicit shots parameter
        job = simulator.run(transpiled_qc, shots=int(num_shots))
        result = job.result()
        counts = result.get_counts()

        return {
            "circuit": qc,
            "counts": counts,
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }

def circuit_to_image(qc):
    """Convert quantum circuit to base64 encoded image."""
    try:
        # Draw circuit with improved styling
        fig = qc.draw(
            output='mpl',
            style='clifford',
            plot_barriers=True,
            cregbundle=False,
            initial_state=True,
            fold=-1  # Prevent line folding
        )
        
        # Save to buffer
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=130)
        plt.close(fig)
        
        return base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Circuit drawing failed: {str(e)}")
        return None

def counts_to_histogram(counts):
    """Convert measurement counts to histogram image."""
    try:
        fig = plot_histogram(counts, color=['#BB86FC'], bar_labels=False)
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        plt.close(fig)
        return base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Histogram generation failed: {str(e)}")
        return None