from qiskit import QuantumCircuit

def create_teleportation_circuit():
    """Create quantum teleportation circuit"""
    qc = QuantumCircuit(3, 3, name="Teleportation")
    
    # Alice prepares qubit to teleport
    qc.h(0)
    qc.barrier()
    
    # Create entanglement between Alice and Bob
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    
    # Bell measurement
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.barrier()
    
    # Correction operations
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    return qc

def create_noisy_circuit():
    """Create noisy teleportation circuit"""
    qc = create_teleportation_circuit()
    qc.name = "Noisy Teleportation"
    # Add some noise gates
    qc.x(0)
    qc.z(1)
    qc.y(2)
    return qc

def create_entangled_circuit():
    """Create pre-entangled circuit"""
    qc = QuantumCircuit(3, 3, name="Pre-entangled")
    # Create GHZ state
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.barrier()
    
    # Teleportation operations
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.barrier()
    qc.cx(1, 2)
    qc.cz(0, 2)
    return qc

def create_custom_circuit(circuit_type="teleport"):
    """Circuit selector with multiple options"""
    circuit_map = {
        "teleport": create_teleportation_circuit,
        "noisy": create_noisy_circuit,
        "entangled": create_entangled_circuit
    }
    return circuit_map.get(circuit_type, create_teleportation_circuit)()