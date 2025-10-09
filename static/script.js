document.addEventListener('DOMContentLoaded', () => {
    const symptomsInput = document.getElementById('symptoms-input');
    const checkButton = document.getElementById('check-button');
    const resultsContainer = document.getElementById('results-container');

    // UPDATED function to format the AI's response
    // In static/script.js

    function formatResponse(text) {
        // Separate the disclaimer from the rest of the text
        const disclaimerHeading = 'IMPORTANT DISCLAIMER:';
        let disclaimerPart = '';
        let restOfText = text;
        if (text.includes(disclaimerHeading)) {
            const splitIndex = text.indexOf('\n\n');
            if (splitIndex !== -1) {
                disclaimerPart = text.substring(0, splitIndex);
                restOfText = text.substring(splitIndex);
            }
        }

        // Format for bolding
        // In static/script.js
        restOfText = restOfText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // --- NEW: Format for Severity Indicators ---
        restOfText = restOfText.replace(/\(Mild\)/g, '<div class="indicator mild"><span class="icon">!</span> Mild</div>');
        restOfText = restOfText.replace(/\(Moderate\)/g, '<div class="indicator moderate"><span class="icon">!</span> Moderate</div>');
        restOfText = restOfText.replace(/\(Serious\)/g, '<div class="indicator serious"><span class="icon">!</span> Serious</div>');

        return `<div class="disclaimer">${disclaimerPart}</div>${restOfText}`;
    }

    checkButton.addEventListener('click', async () => {
        const symptoms = symptomsInput.value.trim();

        if (symptoms.length < 1) {
            resultsContainer.innerHTML = '<p class="error">Please provide a more detailed description of your symptoms.</p>';
            return;
        }

        checkButton.disabled = true;
        resultsContainer.innerHTML = '<p class="loading">Analyzing symptoms, please wait...</p>';

        try {
            const response = await fetch('/check-symptoms', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ symptoms: symptoms }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'An unknown error occurred.');
            }

            const data = await response.json();
            resultsContainer.innerHTML = formatResponse(data.result);

        } catch (error) {
            resultsContainer.innerHTML = `<p class="error">Error: ${error.message}</p>`;
        } finally {
            checkButton.disabled = false;
        }
    });
});