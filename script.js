function scrollToElement(elementSelector, instance = 0){
    // select all elements that match the given selector
    const elements = document.querySelectorAll(elementSelector);
    // Check if there are elements matching the selector and if the requested instance esist
    if(elements.length > instance){
        // Scroll to the specified instance of the element
        elements[instance].scrollIntoView({ behavior: 'smooth'});
    }
}

