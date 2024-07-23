async function calculate(operation) {
    const firstNum = parseFloat(document.getElementById('firstNum').value);
    const secondNum = parseFloat(document.getElementById('secondNum').value);

    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            firstNumber: firstNum,
            secondNumber: secondNum,
            operation: operation,
        }),
    });

    const result = await response.json();
    document.getElementById('result').value = result.result;
}

function clearFields() {
    document.getElementById('firstNum').value = '';
    document.getElementById('secondNum').value = '';
    document.getElementById('result').value = '';
}
