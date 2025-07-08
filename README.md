# 🌌 Quantum Teleportation GUI
Python GUI for quantum teleportation simulation using Qiskit and Eel


[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Qiskit](https://img.shields.io/badge/Qiskit-2.0.2-purple?logo=qiskit)](https://qiskit.org)
[![Eel](https://img.shields.io/badge/Eel-0.18.2-green)](https://github.com/python-eel/Eel)
[![License](https://img.shields.io/badge/License-MIT-gold)](LICENSE)

A Python GUI for simulating quantum teleportation circuits with real-time visualization.
## DEMO
![Basic Teleportation](image.png)
![Noisy channel](image-1.png)
![Pre Entangled state](image-2.png)
## ✨ Features

- **Interactive quantum circuit simulation**
  - Teleportation protocol implementation
  - Multiple circuit types (Basic/Noisy/Entangled)
- **Professional visualization**
  - Live circuit diagrams
  - Measurement histograms
- **Modern GUI**
  - Dark/light mode toggle
  - Responsive design
- **Error handling**
  - Quantum simulation validation
  - User input sanitization

## 🛠️ Installation
```bash
pip install -r requirements.txt  
python main.py


## 🎮 Usage
Select circuit type from dropdown

Enter number of shots (e.g., 1024)

Click "Run Simulation"

View results:

Left panel: Quantum circuit diagram

Right panel: Measurement histogram


## 🌌 Quantum Basics  
This implements the 3-step teleportation protocol:  
1. **Entanglement** - Creates Bell pair between qubits  
2. **Measurement** - Bell state measurement  
3. **Correction** - Applies X/Z gates based on results  