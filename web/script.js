document.addEventListener('DOMContentLoaded', () => {
    // UI Elements
    const runBtn = document.getElementById('run-btn');
    const resetBtn = document.getElementById('reset-btn');
    const themeBtn = document.getElementById('theme-btn');
    const errorDiv = document.getElementById('error');
    const statusDiv = document.getElementById('status');
    const statusText = document.getElementById('status-text');
    const circuitDiagram = document.getElementById('circuit-diagram');
    const histogramImg = document.getElementById('histogram');
    
    // Initialize UI
    function resetUI() {
        errorDiv.classList.add('hidden');
        statusDiv.classList.add('hidden');
        circuitDiagram.src = '';
        histogramImg.src = '';
        document.getElementById('shots').value = '1024';
        document.getElementById('circuit-select').selectedIndex = 0;
    }
    
    resetUI();
    
    // Event Listeners
    runBtn.addEventListener('click', async () => {
        const shots = document.getElementById('shots').value;
        const circuitType = document.getElementById('circuit-select').value;
        
        // Validate input
        if (!shots || isNaN(shots) || shots <= 0) {
            showError('Please enter a valid number of shots');
            return;
        }
        
        // Reset UI and show status
        errorDiv.classList.add('hidden');
        circuitDiagram.src = '';
        histogramImg.src = '';
        statusText.textContent = 'Running quantum simulation...';
        statusDiv.classList.remove('hidden');
        
        try {
            const result = await eel.run_quantum_simulation(circuitType, shots)();
            statusDiv.classList.add('hidden');
            
            if (result.error) {
                showError(result.error);
            } else {
                if (result.circuit) {
                    circuitDiagram.src = `data:image/png;base64,${result.circuit}`;
                }
                if (result.histogram) {
                    histogramImg.src = `data:image/png;base64,${result.histogram}`;
                }
            }
        } catch (e) {
            statusDiv.classList.add('hidden');
            showError(`Communication error: ${e.message}`);
        }
    });
    
    resetBtn.addEventListener('click', resetUI);
    
    themeBtn.addEventListener('click', () => {
        const isDarkMode = document.body.classList.contains('dark-mode');
        document.body.classList.toggle('dark-mode', !isDarkMode);
        document.body.classList.toggle('light-mode', isDarkMode);
        themeBtn.textContent = isDarkMode ? '🌙 Dark Mode' : '☀️ Light Mode';
    });
    
    // Helper functions
    function showError(message) {
        errorDiv.textContent = message;
        errorDiv.classList.remove('hidden');
    }
});