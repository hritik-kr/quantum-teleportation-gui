import sys
import os
import logging
from pathlib import Path
import eel
import simulator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('quantum_gui.log')
    ]
)
logger = logging.getLogger(__name__) 

# Initialize Eel with absolute path
web_path = Path('web').absolute()
if not web_path.exists():
    logger.error(f"Web directory not found at {web_path}")
    sys.exit(1)

eel.init(str(web_path))
logger.info(f"Eel initialized with web path: {web_path}")

@eel.expose
def run_quantum_simulation(circuit_type, num_shots):
    try:
        logger.info(f"Starting simulation: {circuit_type} circuit with {num_shots} shots")
        num_shots = int(num_shots)
        if num_shots <= 0:
            return {"error": "Shots must be positive integer"}
        
        result = simulator.run_simulation(circuit_type, num_shots)
        
        if not result['success']:
            logger.error(f"Simulation failed: {result.get('error', 'Unknown error')}")
            return {"error": result['error']}
        
        circuit_img = simulator.circuit_to_image(result['circuit'])
        histogram_img = simulator.counts_to_histogram(result['counts'])
        
        if not circuit_img or not histogram_img:
            error_msg = "Failed to generate visualization"
            logger.error(error_msg)
            return {"error": error_msg}
        
        logger.info("Simulation completed successfully")
        return {
            "circuit": circuit_img,
            "histogram": histogram_img
        }
    except Exception as e:
        logger.exception("Unexpected error in simulation")
        return {"error": f"Unexpected error: {str(e)}"}

if __name__ == "__main__":
    try:
        logger.info("Starting Quantum Teleportation GUI")
        
        eel.start(
            'index.html',
            size=(1100, 850),
            mode='chrome',
            port=0,  # Let Eel choose a free port automatically
            host='localhost',
            position=(100, 50),
            shutdown_delay=5.0,
            suppress_error=True
        )
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        logger.error("Common fixes:")
        logger.error("1. Make sure Chrome is installed")
        logger.error("2. Try running with --mode=default if Chrome isn't working")
        logger.error("Full error details:", exc_info=True)