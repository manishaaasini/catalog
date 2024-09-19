const fs = require('fs');

const decodeValue = (base, encodedValue) => parseInt(encodedValue, base);

const lagrangeInterpolation = (xValues, yValues) => {
    const k = xValues.length;
    let constantTerm = 0;
    
    for (let i = 0; i < k; i++) {
        let L_i = 1;
        for (let j = 0; j < k; j++) {
            if (i !== j) {
                L_i *= (0 - xValues[j]) / (xValues[i] - xValues[j]);
            }
        }
        constantTerm += yValues[i] * L_i;
    }
    
    return Math.round(constantTerm);
};

const findConstantTerm = (data) => {
    const n = data.keys.n;
    const k = data.keys.k;
    
    const xValues = [];
    const yValues = [];
    
    for (const key in data) {
        if (key !== "keys") {
            const x = parseInt(key);
            const base = parseInt(data[key].base);
            const encodedValue = data[key].value;
            const y = decodeValue(base, encodedValue);
            
            xValues.push(x);
            yValues.push(y);
        }
    }
    
    if (xValues.length < k) {
        throw new Error("Not enough points to reconstruct the polynomial");
    }
    
    return lagrangeInterpolation(xValues.slice(0, k), yValues.slice(0, k));
};

// Read JSON file and process
fs.readFile('testcase1.json', 'utf8', (err, data) => {
    if (err) throw err;
    const jsonData = JSON.parse(data);
    console.log(findConstantTerm(jsonData));
});
fs.readFile('testcase2.json', 'utf8', (err, data) => {
    if (err) throw err;
    const jsonData = JSON.parse(data);
    console.log(findConstantTerm(jsonData));
});
