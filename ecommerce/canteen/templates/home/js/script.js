function toggleMenu(type) {
    const vegSection = document.getElementById('veg-items');
    const nonVegSection = document.getElementById('nonveg-items');
    
    if (type === 'veg') {
        vegSection.classList.remove('hidden');
        nonVegSection.classList.add('hidden');
    } else {
        nonVegSection.classList.remove('hidden');
        vegSection.classList.add('hidden');
    }
}
